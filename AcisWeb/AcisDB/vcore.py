#! /usr/bin/env python3
# coding=utf-8

"""
Views Core Models-DB Engine
"""

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Q
import json,time,threading,copy,random,heapq,pickle
from pprint import pprint as pp, pformat
import collections
from collections import defaultdict

from .models import Erds,TestCases,TestReports,TestCampaign,ProjectSnapshot

import logging
from . import log

mutex = threading.Lock()

vlog = logging.getLogger(__name__).info
tb_log = logging.getLogger(__name__ + '.income_tracebacker').info

DB_UPDATE = False

def update_db_flag():
    global DB_UPDATE
    mutex.acquire()
    DB_UPDATE = False if DB_UPDATE is True else True
    mutex.release()

def get_update_db_flag():
    global DB_UPDATE
    return DB_UPDATE

GLOBAL_PICK_EXCEL_JIRA = {}
GLOBAL_PICK_JENKINS = collections.OrderedDict()

def get_global_pick_copy_excel_jira():
    global GLOBAL_PICK_EXCEL_JIRA
    if get_update_db_flag() is True:
        GLOBAL_PICK_EXCEL_JIRA = {}
        update_db_flag()
        return (True, None)
    else:
        return (False, copy.deepcopy(GLOBAL_PICK_EXCEL_JIRA))

def fill_global_pick_excel_jira(cookies):
    global GLOBAL_PICK_EXCEL_JIRA
    mutex.acquire()
    GLOBAL_PICK_EXCEL_JIRA.update(cookies)
    mutex.release()

def get_global_pick_copy_jenkins(platform, fw_version):
    global GLOBAL_PICK_JENKINS
    if get_update_db_flag() is True:
        GLOBAL_PICK_JENKINS = collections.OrderedDict()
        update_db_flag()
        return (True, None)
    else:
        return (False, copy.deepcopy(GLOBAL_PICK_JENKINS.get((platform, fw_version), None)))

def fill_global_pick_jenkins(platform, fw_version, cookies):
    global GLOBAL_PICK_JENKINS
    mutex.acquire()
    GLOBAL_PICK_JENKINS.update({(platform, fw_version) : cookies})
    if len(GLOBAL_PICK_JENKINS) > 5:
        drop_item = list(GLOBAL_PICK_JENKINS.keys())[0]
        GLOBAL_PICK_JENKINS.pop(drop_item)
    mutex.release()

class Provider:
    """
    """
    @property
    def formatted_rawdata(self):
        """
        Must implement via SubClass.

        For Excel Data:
        >>> [
        >>> ...
        >>> {
        >>>   "PLATFORM" : "",
        >>>   "ERD_ID" : "",
        >>>   "excel" : {
        >>>     'erd_id' : "",
        >>>     'category' : "",
        >>>     'title' : "",
        >>>     'description' : "",
        >>>     'product_priority' : "",
        >>>     'author' : "",
        >>>     'version' : "",
        >>>     'platform' : "",
        >>>     'project' : "",
        >>>     'component' : "",
        >>> } ...
        >>> ]


        For JIRA Ticket Data:
        >>> [
        >>> ...
        >>> {
        >>>   "PLATFORM" : "",
        >>>   "ERD_ID" : "",
        >>>   "jira" : {
        >>>     'HLD' : "",
        >>>     'status' : "",
        >>>     'l1_jira' : "",
        >>>     'l2_jira' : "",
        >>>     'bug_jiras' : "",
        >>>     'platform' : "",
        >>>     'workload' : "",
        >>>     'milestone' : "",

        >>>     'F_casetree' : [
        >>>                 ...
        >>>                 {
        >>>                     'case_name' : "",
        >>>                     'case_age' : "",
        >>>                     'F_report_path': "",
        >>>                 },
        >>>                 ... ]
        >>>     }
        >>> ...
        >>> ]


        For Jenkins Test Data:
        NOTE: For jenkins data, ONLY one element for list.

        Description:
        IR_report_path - Integration or Regression Test report path.

        >>> [{
        >>>     "PLATFORM" : "",
        >>>     "jenkins" : {
        >>>           'IR_casetree' : {
        >>>                  'ACIS_A_S_Test_Temp_Volt' : {
        >>>                      'fw_version' : "",
        >>>                      'test_result' : "",
        >>>                      'test_log' : "",
        >>>                      'test_date' : "",
        >>>                      'IR_report_path' : "",
        >>>                      },
        >>>                  'ACIS_A_S_Test_Temp_ssss' : {
        >>>                      'fw_version' : "",
        >>>                      'test_result' : "",
        >>>                      'test_log' : "",
        >>>                      'test_date' : "",
        >>>                      'IR_report_path' : "",
        >>>                  },
        >>>                  'ACIS_A_S_Test_Temp_abcd' : {
        >>>                      'fw_version' : "",
        >>>                      'test_result' : "",
        >>>                      'test_log' : "",
        >>>                      'test_date' : "",
        >>>                      'IR_report_path' : "",
        >>>                  },
        >>>                  ... ...
        >>>            }
        >>>     }
        >>> }]


        For UI-Form Data:
        >>> Reserved.Now

        """
        assert False, "Provider sub-class should implement this property [formatted_rawdata]"


class Extractor:
    """
    """
    def __init__(self, platforms, fw_version = "", filter = None):
        """
        input:
        self.ERD_ID_list   : ERD ID list. eg. ["01.01", "01.03", ... ]
        self.extract_types : Data types.  eg. ['excel', 'jira', 'jenkins', 'UIform']

        output:
        self.output_data   : be used to 'splitter', private !
        _get_data          : SubClass should use this method to get the self.output_data copy.
        """

        self.PLATFORM_LIST = platforms
        self.output_data = {}
        self.FW_VERSION = fw_version

        self.filter = filter

    def _get_data(self):
        """
        Ensure that the data is NOT modified, so use a DEEP copy.

        Should NOT use 'self.output_data', this method is a common interface.
        """
        return copy.deepcopy(self.output_data)

def splitter(action, provider = None, extractor = None):
    """
    action: 'save', 'pick_all', 'pick_with_filter'

    provider : instance of Provider, must support 'formatted_rawdata' property.
    extractor: instance of Extractor, must support 'ERD_ID_list', 'extract_types', 'output_data'

    Support Types:
    1. Data from/to Excel
    2. Data from/to JIRA Ticket
    3. Data from/to Jenkins
    4. Data from/to UI Form

    """

    types = {'excel'    : ExcelDataProcesser,
             'jira'     : JiraDataProcesser,
             'jenkins'  : JenkinsDataProcesser,
             'UIform'   : UiFormDataProcesser}

    if action == 'save':
        db_name = "ACIS_DB"
        tp_record = []

        if not provider:
            vlog("[provider] does NOT exist."); return

        for cookie in provider.formatted_rawdata:
            PLATFORM = cookie.get('PLATFORM',"mustExist") # vaild?
            ERD_ID = cookie.get('ERD_ID', "unused")
            description = cookie.get('description', "unused")

            for tp in cookie:
                try:
                    mutex.acquire()
                    if tp in types and cookie[tp]:
                        types[tp](PLATFORM, ERD_ID, cookies = cookie[tp], description = description).doit(action)
                except Exception as e:
                    vlog("> &_& Save action of [{tp}] occurs exception, reason: [{reason}]".format(tp=tp, reason=e.args))
                    #raise
                else:
                    if tp in types and tp not in tp_record:
                        tb_log('Data from [{type_of_data}] to the DB [{db}]'.format(type_of_data=tp, db = db_name))
                        tp_record.append(tp)
                    # Jenkins data just once (save).
                    if tp in types and tp == "jenkins" and cookie[tp]:
                        TestCampaignDealer().save(cookie)
                finally:
                    mutex.release()

        if get_update_db_flag() is False:
            update_db_flag()

    elif action == 'pick_all':

        vlog("IN pick all")
        plog = logging.getLogger(__name__ + '.pick_all').info

        if not extractor:
            vlog("[extractor] does NOT exist.");return

        if not extractor.FW_VERSION:

            update, cookies = get_global_pick_copy_excel_jira()
            if update is False and cookies:
                if not (set(extractor.PLATFORM_LIST) - set(cookies.keys())):
                    print("hook cache for NOT jenkins")
                    extractor.output_data = {c: cookies[c] for c in cookies if c in extractor.PLATFORM_LIST}
                    plog(pformat(extractor.output_data))
                    return extractor.output_data

            platform_list = extractor.PLATFORM_LIST

            for p in platform_list:
                platform_objs = Erds.objects.filter(platform = p) # Erds Table MUST exists!
                extractor.output_data[p] = {}
                ERD_ID_list = []

                for po in platform_objs:
                    if po.erd_id not in ERD_ID_list:
                        ERD_ID_list.append(po.erd_id)

                for ERD_ID in ERD_ID_list:
                    extractor.output_data[p][ERD_ID] = {}
                    for tp in types:
                        if tp != 'jenkins':
                            mutex.acquire()
                            extractor.output_data[p][ERD_ID][tp] = types[tp](p, ERD_ID).doit(action)
                            mutex.release()

            fill_global_pick_excel_jira(extractor.output_data)

        else:

            update, cookies = get_global_pick_copy_jenkins(platform = extractor.PLATFORM_LIST[0],
                                                         fw_version = extractor.FW_VERSION)
            if update is False and cookies:
                print("hook cache for jenkins.")
                extractor.output_data = cookies
                plog(pformat(extractor.output_data))
                return cookies

            platform = extractor.PLATFORM_LIST[0]

            extractor.output_data['platform'] = platform
            extractor.output_data['fw_version'] = extractor.FW_VERSION

            # Jenkins Channel
            mutex.acquire()
            extractor.output_data['IR_casetree'] = types['jenkins'](platform,
                                                                   ERD_ID = 'unused',
                                                                   FW_VERSION = extractor.FW_VERSION).doit(action)
            mutex.release()

            fill_global_pick_jenkins(platform = platform,
                                     fw_version = extractor.FW_VERSION,
                                     cookies = extractor.output_data)

        plog(pformat(extractor.output_data))
        return extractor.output_data


    elif action == 'pick_with_filter':
        vlog("Now, Reserved.[{}]".format(action))

    else:
        vlog("Action NOT support.")

class CookiesProcesser:
    """
    Core Data Processer.

    SubClass should implement those abstract methos.

    Provide some COMMON methods for SubClass.
    """

    def save(self):
        assert False, "Children Should implement this method."

    def pick(self):
        assert False, "Children Should implement this method."

    def doit(self):
        assert False, "Children Should implement this method."

    # Extend Common methods
    def get_lastest_ver(self, objs):

        versions = []
        maps = {}

        if not objs: return None

        for o in objs:
            maps[o] = o.version
            versions.append(o.version)

        lastest = max(versions)
        for m in maps:
            if m.version == lastest:
                return m


class ExcelDataProcesser(CookiesProcesser):
    """
    Processer for Excel Data.
    """

    data_category = ('erd_id',
                     'platform',
                     'category',
                     'title',
                     'description',
                     'product_priority',
                     'author',
                     'version',
                     'project',
                     'component')

    def __init__(self, PLATFORM, ERD_ID, cookies = None, ERD_model = Erds, FW_VERSION = "unused", **kwargs):
        self.platform = PLATFORM
        self.ERD_ID = ERD_ID
        self.cookies = cookies
        self.ERD_model = ERD_model
        self.FW_VERSION = FW_VERSION

    def save(self):
        """
        auto ignore the data outof 'data_category'.
        """

        except_list = []

        if not self.cookies:
            vlog("cookies is empty, do nothing.");return

        for c in self.cookies:
            if c not in ExcelDataProcesser.data_category:
                except_list.append(c)

        for e in except_list:
            self.cookies.pop(e)

        Q_filter_platform = Q(platform = self.platform)
        Q_filter_erd_id   = Q(erd_id = self.ERD_ID)

        #el = Erds.objects.filter(erd_id = self.cookies['erd_id'])
        el = Erds.objects.filter(Q_filter_platform , Q_filter_erd_id)
        if el:
            for e in el:
                if e.version == self.cookies['version']:
                    vlog("ERD [{}] version [{}] is already in DB, ignore it.".format(
                        self.cookies['erd_id'],self.cookies['version']))
                    return

        e = Erds(**self.cookies)
        e.save()
        time.sleep(0.1)

    def pick_all(self):
        """
        """

        Q_filter_platform = Q(platform = self.platform)
        Q_filter_erd_id   = Q(erd_id = self.ERD_ID)

        el = Erds.objects.filter(Q_filter_platform , Q_filter_erd_id)
        if not el:
            vlog("The item about your ERD_ID, doesn't exist.")
            return {}

        out = {}
        for e in el:
            out[e.version] = {}
            for d in ExcelDataProcesser.data_category:
                out[e.version][d] = e.__dict__[d]
        return out

    def pick_with_filter(self):
        pass

    def doit(self,action):
        if action == 'save':
            self.save()
        elif action == 'pick_all':
            return self.pick_all()
        elif action == 'pick_with_filter':
            return self.pick_with_filter()


class JiraDataProcesser(CookiesProcesser):
    """
    Processer for JIRA Ticket Data.
    """

    data_category = ('HLD',
                     'status',
                     'l1_jira',
                     'l2_jira',
                     'bug_jiras',
                     'workload',
                     'milestone',
                     'F_casetree',)


    def __init__(self, PLATFORM, ERD_ID, cookies = None, ERD_model = Erds, FW_VERSION = "unused", **kwargs):
        self.platform = PLATFORM
        self.ERD_ID = ERD_ID
        self.cookies = cookies
        self.ERD_model = ERD_model
        self.FW_VERSION = FW_VERSION

    def save(self):
        '''
        auto ignore the data outof 'data_category'.
        '''

        except_list = []

        if not self.cookies:
            vlog("cookies is empty, do nothing.");return

        for c in self.cookies:
            if c not in JiraDataProcesser.data_category:
                except_list.append(c)

        for e in except_list:
            self.cookies.pop(e)

        Q_filter_platform = Q(platform = self.platform)
        Q_filter_erd_id   = Q(erd_id = self.ERD_ID)

        el = Erds.objects.filter(Q_filter_platform, Q_filter_erd_id)

        e = self.get_lastest_ver(el)
        if not e :
            vlog("ERD_ID [{}] does NOT exist, maybe you should import ERD TABLE items firstly.\n\tel:{}".format(self.ERD_ID,el))
            return

        # Erds Table items save.
        for d in JiraDataProcesser.data_category:
            for c in self.cookies:
                if d in Erds.__dict__ and d == c:
                    e.__dict__[d] = self.cookies[c]
        e.save()
        time.sleep(0.1)

        # TestCases Table items save.
        if 'F_casetree' in  self.cookies and self.cookies['F_casetree']:

            casetree = self.cookies['F_casetree']
            tcl = e.testcases_set.all()

            if not tcl:
                vlog("> This Erds object [from ERD {}] NOT be related to any case. Attach it. <".format(self.ERD_ID))
                for ct in casetree:
                    e.testcases_set.create(**ct).save()
                    time.sleep(0.1)
            else:
                tcl_name_map = {tc.case_name : tc for tc in tcl}
                F_casetree_set = { c['case_name'] for c in self.cookies['F_casetree']}
                delete_items = tcl_name_map.keys() - F_casetree_set

                for di in delete_items:
                    tcl_name_map[di].delete()

                tcl = e.testcases_set.all()

                for ct in casetree:
                    if ct['case_name'] not in [tc.case_name for tc in tcl]:
                        vlog("> new case [{}] bound to Erds Table. <".format(ct['case_name']))
                        e.testcases_set.create(**ct).save()
                        time.sleep(0.1)
                    else:

                        s1 = set(ct['F_report_path'].split(','))

                        # Should only!
                        tc = e.testcases_set.get(case_name = ct['case_name'])

                        vlog("\t S1 : {},\n\t S2 : {}\n\t S1-S2 : {} ".
                                format(s1,
                                    set(tc.F_report_path.split(',')),
                                    s1 - set(tc.F_report_path.split(','))))

                        if tc and s1 - set(tc.F_report_path.split(',')):
                            for s in (s1 -set(tc.F_report_path.split(','))):
                                vlog("> report added: [{}] <".format(s))
                                tc.F_report_path += ',' + str(s)
                                tc.save()
                                time.sleep(0.1)
                        else:
                            vlog("> case name and report part already exist, do nothing <")

        else:
            vlog("F_case_tree NOT be provided, do nothing for TESTCASES Table items")

    def pick_all(self):

        Q_filter_platform = Q(platform = self.platform)
        Q_filter_erd_id   = Q(erd_id = self.ERD_ID)

        el = Erds.objects.filter(Q_filter_platform, Q_filter_erd_id)

        out = {}

        if not el:
            vlog("> ERD ID [{}] is NOT in DB.<".format(self.ERD_ID))
            return out

        for e in el:
            out[e.version] = {}

            vlog("\n\tERD_ID : {}, Version : {}".format(self.ERD_ID, e.version))
            for d in JiraDataProcesser.data_category:
                # pick Erds Table items
                if d in Erds.__dict__:
                    #vlog(">> [pick] Deal Erds Table's type [{}]".format(d))
                    out[e.version][d] = e.__dict__[d]

                # pick TestCases Table items
                if d == 'F_casetree':
                    #vlog(">> [pick] Deal TestCases Table's type [{}]".format(d))
                    tcl = e.testcases_set.all()
                    out[e.version]['F_casetree'] = {}
                    out[e.version]['IR_report']  = {}

                    for tc in tcl:
                        out[e.version]['F_casetree'].update(
                            {
                                tc.case_name : {
                                    'case_name' : tc.case_name,
                                    'case_age'  : tc.case_age,
                                    'F_report_path' :tc.F_report_path,
                                }})

                        trl = tc.testreports_set.all()
                        if trl:

                            latest_tr = max(trl, key = lambda tr: tr.fw_version)
                            same_ver_sub_trl = []

                            for tr in trl:
                                if tr.fw_version == latest_tr.fw_version:
                                    same_ver_sub_trl.append(tr)

                            if len(same_ver_sub_trl) > 1:
                                combin_tr = max(same_ver_sub_trl, key = lambda tr: tr.test_date)
                            else: # count == 1
                                combin_tr = same_ver_sub_trl[0]

                            out[e.version]['IR_report'].update(
                                {
                                    tc.case_name : {
                                        'case_name' : tc.case_name,
                                        'fw_version' : combin_tr.fw_version,
                                        'test_date' : combin_tr.test_date,
                                        'test_result' : combin_tr.test_result,
                                        'IR_report_path' : combin_tr.IR_report_path,
                                    }})

        return out

    def pick_with_filter(self):
        pass

    def doit(self,action):
        if action == 'save':
            self.save()
        elif action == 'pick_all':
            return self.pick_all()
        elif action == 'pick_with_filter':
            return self.pick_with_filter()

class JenkinsDataProcesser(CookiesProcesser):
    """
    Processer for Jenkins Data.

    Date format:
    Year, month, day, hour, minute, second.
    eg.
    "2019-12-22:14-23-59"
    """

    data_category = ('IR_casetree',)

                    # {
                    # 'casename' : {
                    #    'IR_report_path': "",
                    #    'fw_version': "",
                    #    'test_result' : "",
                    #    'test_log' : "",
                    #    'test_date' : "",
                    # },
                    # 'casename2' : {},
                    # ... }

    def __init__(self, PLATFORM, ERD_ID = "unused", cookies = None, ERD_model = Erds, FW_VERSION = "", **kwargs):
        self.platform = PLATFORM
        self.ERD_ID = ERD_ID
        self.ERD_model = ERD_model
        self.FW_VERSION = FW_VERSION
        self.description = kwargs.get("description", "UNKNOWN_DESCRIPTION")
        self.cookies = copy.deepcopy(cookies)

        # >>>     "jenkins" : {
        # >>>           'IR_casetree' : {
        # >>>                  'ACIS_A_S_Test_Temp_Volt' : {
        # >>>                      'fw_version' : "",
        # >>>                      'test_result' : "",
        # >>>                      'test_log' : "",
        # >>>                      'test_date' : "",
        # >>>                      'IR_report_path' : "",
        # >>>                      },
        # >>>                  'ACIS_A_S_Test_Temp_ssss' : {
        # >>>                      'fw_version' : "",
        # >>>                      'test_result' : "",
        # >>>                      'test_log' : "",
        # >>>                      'test_date' : "",
        # >>>                      'IR_report_path' : "",
        # >>>                  },
        # >>>                  'ACIS_A_S_Test_Temp_abcd' : {
        # >>>                      'fw_version' : "",
        # >>>                      'test_result' : "",
        # >>>                      'test_log' : "",
        # >>>                      'test_date' : "",
        # >>>                      'IR_report_path' : "",
        # >>>                  },
        # >>>                  ... ...
        # >>>            }
        # >>>     }

    def save(self):
        '''
        auto ignore the data outof 'data_category'.
        '''
        except_list = []

        if not self.cookies:
            vlog("cookies is empty, do nothing.");return

        for c in self.cookies:
            if c not in JenkinsDataProcesser.data_category:
                except_list.append(c)

        for e in except_list:
            self.cookies.pop(e)

        Q_filter_platform = Q(platform = self.platform)
        el = Erds.objects.filter(Q_filter_platform)

        same_erd_id_dict = defaultdict(list)

        for e in el:
            same_erd_id_dict[e.erd_id].append((e.version, e))

        # print("recored : same_erd_id_dict")
        # pp(same_erd_id_dict)

        lastest_version_objs = {}
        for erd, o_list in same_erd_id_dict.items():
            lastest_version_objs[erd] = max(o_list, key = lambda a : a[0])[1]

        # print("recored : lastest_version_objs")
        # pp(lastest_version_objs)

        ANY_MATCHED = False
        for obj in lastest_version_objs.values():
            tcl = obj.testcases_set.all()
            for tc in tcl:
                if tc.case_name in self.cookies['IR_casetree']:
                    self.cookies['IR_casetree'][tc.case_name].update({'description' : self.description})
                    tc.testreports_set.create(**self.cookies['IR_casetree'][tc.case_name]).save()
                    time.sleep(0.1)
                    ANY_MATCHED = True

        if ANY_MATCHED is False:
            raise Exception("TestCampaign test cases are not match to DB saved.")

    def pick_all(self):
        """
        {
            'ACIS_A_S_Test_Temp_Volt' : {
                'erd_id' : "",
                'fw_version' : "",
                'test_result' : "",
                'test_log' : "",
                'test_date' : "",
                'IR_report_path' : "",
                'note' : "",
                'description' : "",
                },
            'ACIS_A_S_Test_Temp_ssss' : {
                'erd_id' : "",
                'fw_version' : "",
                'test_result' : "",
                'test_log' : "",
                'test_date' : "",
                'IR_report_path' : "",
                'note' : "",
                'description' : "",
            },
            'ACIS_A_S_Test_Temp_abcd' : {
                'erd_id' : "",
                'fw_version' : "",
                'test_result' : "",
                'test_log' : "",
                'test_date' : "",
                'IR_report_path' : "",
                'note' : "",
                'description' : "",
            },
        ... ...
        }
        """
        out = {}
        # get all Erds-objs for platform
        Q_filter_platform = Q(platform = self.platform)
        el = Erds.objects.filter(Q_filter_platform)

        Q_filter_fw_version = Q(fw_version__icontains = self.FW_VERSION)
        for e in el:
            tcl = e.testcases_set.all()
            for tc in tcl:
                trf = tc.testreports_set.filter(Q_filter_fw_version)

                if trf:
                    latest_tr = max(trf, key = lambda tr: tr.test_date)

                    out[tc.case_name] = {
                        'erd_id' : e.erd_id,
                        'fw_version' : latest_tr.fw_version,
                        'test_result' : latest_tr.test_result,
                        'test_log' : latest_tr.test_log,
                        'test_date' : latest_tr.test_date,
                        'IR_report_path' : latest_tr.IR_report_path,
                        # 'note' : "",
                        # 'description' : "",
                    }

        return out

    def pick_with_filter(self):
        pass

    def doit(self,action):
        if action == 'save':
            self.save()
        elif action == 'pick_all':
            return self.pick_all()
        elif action == 'pick_with_filter':
            return self.pick_with_filter

class UiFormDataProcesser(CookiesProcesser):
    """
    Processer for UI-Form Data.
    """

    data_category = ('UiTest',)

    def __init__(self, PLATFORM, ERD_ID, cookies = None, ERD_model = Erds, FW_VERSION = "unused" , **kwargs):
        self.ERD_ID = ERD_ID
        self.cookies = cookies
        self.ERD_model = ERD_model
        self.platform = PLATFORM
        self.FW_VERSION = FW_VERSION

    def save(self):
        pass

    def pick(self):
        pass

    def doit(self,action):
        if action == 'save':
            self.save()
        elif action == 'pick':
            return self.pick()


class UnsupportedQuery(Exception): pass
class QueryArgsInvalid(Exception): pass
class QueryNoteMultiple(Exception): pass

class Query:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class TestReportQuery(Query):
    supported_query = (
        'test_report_query',
        'ERD_caselist_query',
        'casename_query',
        'pick_note',
    )

    def __init__(self, which_query, **kwargs):
        if which_query not in TestReportQuery.supported_query:
            raise UnsupportedQuery("Query NOT be supported.")

        if which_query == 'test_report_query':
            if {'platform', 'fw_version', 'start_test_date', 'end_test_date'} - kwargs.keys():
                raise QueryArgsInvalid("[{}] can't get valid args.[{}]".format(which_query, kwargs))
            self.valid_args = kwargs
            self.which_query = which_query

        elif which_query == 'ERD_caselist_query':
            if {'platform', 'ERD_ID'} - kwargs.keys():
                raise QueryArgsInvalid("[{}] can't get valid args.[{}]".format(which_query, kwargs))
            self.valid_args = kwargs
            self.which_query = which_query

        elif which_query == 'casename_query':
            if {'platform', 'casename'} - kwargs.keys():
                raise QueryArgsInvalid("[{}] can't get valid args.[{}]".format(which_query, kwargs))
            self.valid_args = kwargs
            self.which_query = which_query

        elif which_query == 'pick_note':
            if {'platform', 'fw_version', 'test_date', 'ERD_ID', 'case_name'} - kwargs.keys():
                raise QueryArgsInvalid("[{}] can't get valid args.[{}]".format(which_query, kwargs))
            self.valid_args = kwargs
            self.which_query = which_query

        self.test_report_objs = []


    def pick_note_obj(self):

        # filter for Erds Model.
        Q_erd_model_filter = Q(platform = self.valid_args['platform'].upper()) \
                             & Q(erd_id = self.valid_args['ERD_ID'])
        # filter for TestCases Model.
        Q_testcase_model_filter = Q(case_name = self.valid_args['case_name'])

        # fiter for TestReports Model.
        Q_testreports_model_filter = Q(fw_version = self.valid_args['fw_version']) \
                                     & Q(test_date = self.valid_args['test_date'])

        only = 0 # Only one object should be picked out.
        pick_out = []
        el = Erds.objects.filter(Q_erd_model_filter)
        for e in el:
            tcl = e.testcases_set.filter(Q_testcase_model_filter)
            if tcl:
                for tc in tcl:
                    trl = tc.testreports_set.filter(Q_testreports_model_filter)
                    if trl:
                        for tr in trl:
                            pick_out.append(tr)

        if len(pick_out) != 1:
            raise QueryNoteMultiple("Hope get only one object, but query out [{}],\n [{}]"
                                    "".format(len(pick_out), pick_out))
        return pick_out[only]


    def test_report_filter(self, query_set):
        fw_version = self.valid_args['fw_version'].strip()
        start_test_date = self.valid_args['start_test_date'].strip()
        end_test_date = self.valid_args['end_test_date'].strip()
        # Set the filter
        if start_test_date and end_test_date and fw_version:
            test_report_filter = Q(test_date__gte=start_test_date) & Q(test_date__lte=end_test_date) & Q(
                fw_version=fw_version)
        elif start_test_date and end_test_date:
            test_report_filter = Q(test_date__gte=start_test_date) & Q(test_date__lte=end_test_date)
        elif start_test_date and fw_version:
            test_report_filter = Q(test_date__lte=end_test_date) & Q(fw_version=fw_version)
        elif end_test_date and fw_version:
            test_report_filter = Q(test_date__lte=end_test_date) & Q(fw_version=fw_version)
        elif start_test_date:
            test_report_filter = Q(test_date__gte=start_test_date)
        elif end_test_date:
            test_report_filter = Q(test_date__lte=end_test_date)
        elif fw_version:
            test_report_filter = Q(fw_version=fw_version)

        if not start_test_date and not end_test_date and not fw_version:
            trl = query_set.testreports_set.all()
        else:
            trl = query_set.testreports_set.filter(test_report_filter)

        return trl

    def format_test_report(self, platform, erd_id, casename, test_report):
        out = {}
        out['erd_id'] = erd_id
        out['platform'] = platform
        out['case_name'] = casename
        out['fw_version'] = test_report.fw_version
        out['test_date'] = test_report.test_date
        out['test_result'] = test_report.test_result
        out['IR_report_path'] = test_report.IR_report_path
        out['note'] = test_report.note
        return out

    def test_report_data(self):
        ui_out = []

        platform = self.valid_args['platform'].strip().upper()
        Q_filter_platform = Q(platform=platform)
        if self.which_query == "ERD_caselist_query":
            ERD_ID = self.valid_args['ERD_ID'].strip()
            erd_table_filter = Q(erd_id=ERD_ID) & Q_filter_platform
        else:
            erd_table_filter = Q_filter_platform
        el = Erds.objects.filter(erd_table_filter)

        for e in el:
            if self.which_query == "casename_query":
                casename = self.valid_args['casename'].strip()
                q_casename_filter = Q(case_name__icontains=casename)
                tcl = e.testcases_set.all().filter(q_casename_filter)
            else:
                tcl = e.testcases_set.all()
            for tc in tcl:
                if self.which_query == 'test_report_query':
                    trl = self.test_report_filter(tc)
                else:
                    trl = tc.testreports_set.all()


                for tr in trl:

                    # Hope pick out all test report objects.
                    self.test_report_objs.append(tr)

                    ui_out.append(self.format_test_report(platform, e.erd_id, tc.case_name, tr))

        return ui_out


class QueryMixin:

    def query(self, ** query_keys):
        """
        This may not be a good implementation, but at least avoid duplicate code.
        """

        # Separate elements that are unique to each category.
        if self.__class__.__name__ == "TestCampaignDealer":
            supported_query_keys = {
                'fw_version'  : 'fw_version__icontains',
                'test_date'   : 'test_date__icontains',
                'description' : 'description__icontains',
            }
            Model = TestCampaign
            ordered_str = '-test_date'

        elif self.__class__.__name__ == "SnapshotDealer":
            supported_query_keys = {
                'platform'  : 'platform__icontains',
                'date'      : 'date__icontains',
                'tag'       : 'tag__icontains',
            }
            Model = ProjectSnapshot
            ordered_str = '-date'
        else:
            raise Exception("Query Mixin NOT support [{}] query".format(self.__class__.__name__))

        # Don't want to match the whole word.
        query_result_list = []

        # if no args, query all objs in DB.
        if not query_keys:
            query_result_list = Model.objects.all().order_by(ordered_str)
            return query_result_list

        # filter out unsupport key-words.
        match_supported_keys = {}
        for key in query_keys:
            if key in supported_query_keys:
                match_supported_keys[supported_query_keys[key]] = query_keys[key]

        # The contents of the parameters are not checked.
        # If the contents do not match, there will be no query results.
        query_result_list = Model.objects.filter(**match_supported_keys).order_by(ordered_str)

        return query_result_list


class TestCampaignDealer(QueryMixin):

    def save(self, cookie):

        if not cookie:
            raise Exception("> &_& cookie is empty dict.")

        to_save = {}
        _, any = random.choice(list(cookie['jenkins']['IR_casetree'].items()))

        to_save['fw_version'] = any['fw_version']
        to_save['test_date'] = any['test_date']
        to_save['platform'] = cookie['PLATFORM']
        to_save['description'] = cookie['description']

        TestCampaign(**to_save).save()

        tb_log('Data from [{type_of_data}] to the table ({tb}) of  DB [{db}]'.format(type_of_data='Jenkins Test',
                                                                                     tb='TestCampaign',
                                                                                     db = 'ACIS_DB'))

    def get_latest(self):

        cl = TestCampaign.objects.all()
        display_count = 5
        latest_five_list = heapq.nlargest(display_count, cl, key = lambda c : c.test_date)
        return latest_five_list

class SnapshotDealer(QueryMixin):

    def pickling(self, platform, any_obj, tag = "AutoSaveWeekly"):
        s = ProjectSnapshot()
        if not platform:
            s.platform = "UNKNOWN_PLATFORM"
            vlog("unknown platform, maybe you should make sure that [cookies] of <ERD_page.htm> NOT empty.")
        else:
            s.platform = platform
        s.tag  = tag
        s.date = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        s.snap = pickle.dumps(any_obj)
        s.save()

        tb_log('Data from [{type_of_data}] to the table ({tb}) of  DB [{db}]'.format(type_of_data='project view',
                                                                                     tb='ProjectSnapshot',
                                                                                     db = 'ACIS_DB'))

    def unpickling(self, date, tag = "AutoSaveWeekly"):
        sl = ProjectSnapshot.objects.filter(date=date, tag=tag)
        only = 0
        out = pickle.loads(sl[only].snap)
        return out

    def get_latest(self):
        sl = ProjectSnapshot.objects.all()
        display_count = 5
        latest_five_list = heapq.nlargest(display_count, sl, key = lambda s: s.date)
        return latest_five_list
