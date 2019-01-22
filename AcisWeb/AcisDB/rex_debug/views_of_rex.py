#! /usr/bin/env python3
# coding=utf-8

"""
< For Rex Debug >
"""

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import json,time,threading,copy,os,re
from pprint import pprint as pp, pformat

from AcisDB import log
from AcisDB import vcore

import logging
mlogger = logging.getLogger(__name__).info

class RexExcelProvider(vcore.Provider):

    from .test_cookies_of_rex import (show_time_first_from_excel,
                                      show_time_second_from_excel,
                                      show_time_third_from_excel,
                                      show_time_fourth_from_excel)

    self_test = {
        "first" : show_time_first_from_excel,
        "second" : show_time_second_from_excel,
        "third" : show_time_third_from_excel,
        "fourth" : show_time_fourth_from_excel,
    }

    def __init__(self,platform = "SD55", test_version = "first"):

        self.platform = platform
        self.test_version = test_version

    def get_data(self):
        t = RexExcelProvider.self_test[self.test_version](self.platform)

        logger_to_excel = logging.getLogger(__name__ + '.from_excel')
        logger_to_excel.info(pformat(t))

        return t

    @property
    def formatted_rawdata(self):
        return self.get_data()

class RexJiraProvider(vcore.Provider):

    from .test_cookies_of_rex import (show_time_first_from_jira,
                                      show_time_second_from_jira,
                                      show_time_third_from_jira,
                                      show_time_fourth_from_jira,

                                      follow_second_excel_update_jira,
                                      follow_third_excel_update_jira ,
                                      follow_fourth_excel_update_jira,
    )

    self_test = {
        "first" : show_time_first_from_jira,
        "second" : show_time_second_from_jira,
        "third" : show_time_third_from_jira,
        "fourth" : show_time_fourth_from_jira,

        "follow01" : follow_second_excel_update_jira,
        "follow02" : follow_third_excel_update_jira ,
        "follow03" : follow_fourth_excel_update_jira,
    }

    def __init__(self, platform, test_version):
        self.platform = platform
        self.test_version = test_version

    def get_data(self):
        t = RexJiraProvider.self_test[self.test_version](self.platform)

        logger_to_jira = logging.getLogger(__name__ + '.from_jira')
        logger_to_jira.info(pformat(t))

        return t

    @property
    def formatted_rawdata(self):
        return self.get_data()

class ExcelProvider(vcore.Provider):

    from .test_cookies_of_rex import (
        test_get_excel_data_first,
        test_get_excel_data_second,
        test_get_excel_data_third,
        test_get_excel_data_fourth,
    )

    self_test = {
            "first" : test_get_excel_data_first,
            "second" : test_get_excel_data_second,
            "third" : test_get_excel_data_third,
            "fourth" : test_get_excel_data_fourth,
    }

    def __init__(self,platform = "SD55", test_version = "first"):

        self.platform = platform
        self.test_version = test_version

    def get_data(self):
        t = ExcelProvider.self_test[self.test_version](self.platform)

        logger_to_excel = logging.getLogger(__name__ + '.from_excel')
        logger_to_excel.info(pformat(t))

        return t

    @property
    def formatted_rawdata(self):
        """
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
        >>> }
        >>> ...
        >>> ]
        """
        return self.get_data()

class JiraProvider(vcore.Provider):

    from .test_cookies_of_rex import (
        test_get_jira_data_first,
        test_get_jira_data_second,
        test_get_jira_data_third,
    )

    self_test = {
        "first" : test_get_jira_data_first,
        "second" : test_get_jira_data_second,
        "third" : test_get_jira_data_third,
    }

    def __init__(self, platform, test_version):
        self.platform = platform
        self.test_version = test_version

    def get_data(self):
        t = JiraProvider.self_test[self.test_version](self.platform)

        logger_to_jira = logging.getLogger(__name__ + '.from_jira')
        logger_to_jira.info(pformat(t))

        return t

    @property
    def formatted_rawdata(self):
        """
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
        """
        return self.get_data()

class JenkinsProvider(vcore.Provider):

    from .test_cookies_of_rex import (
        show_time_jenkins_test_01,
        show_time_jenkins_test_02,
        show_time_jenkins_test_03,
        show_time_jenkins_test_04,
        show_time_jenkins_test_05,
        show_time_jenkins_test_06,
        show_time_jenkins_test_07,
    )

    self_test = {
        "test01" : show_time_jenkins_test_01,
        "test02" : show_time_jenkins_test_02,
        "test03" : show_time_jenkins_test_03,
        "test04" : show_time_jenkins_test_04,
        "test05" : show_time_jenkins_test_05,
        "test06" : show_time_jenkins_test_06,
        "test07" : show_time_jenkins_test_07,
    }

    def __init__(self, platform, test_version):
        self.platform = platform
        self.test_version = test_version

    def get_data(self):
        t = JenkinsProvider.self_test[self.test_version](self.platform)

        logger_to_jenkins = logging.getLogger(__name__ + '.from_jenkins')
        logger_to_jenkins.info(pformat(t))
        # pp(t)
        # assert False,'hope'

        return t

    @property
    def formatted_rawdata(self):
        """
        For Jenkins Test Data:
        NOTE: For jenkins data, ONLY one element for list.

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
        """
        return self.get_data()

class SubProvider(vcore.Provider):

    @property
    def formatted_rawdata(self):
        from .test_cookies_of_rex import random_gen_cookies
        return random_gen_cookies()


class IntegrationExtractor(vcore.Extractor):

    @property
    def UI_data(self):
        UI_out = []

        data = self._get_data()

        out = {}
        for case_name, vs in data['IR_casetree'].items():
            out['platform']  = data['platform']
            out['fw_version'] = data['fw_version']

            out['case_name'] = case_name
            out['erd_id']    = vs['erd_id']
            out['test_log']  = vs['test_log']
            out['test_date'] = vs['test_date']
            out['test_result'] = vs['test_result']
            out['IR_report_path'] = vs['IR_report_path']
            UI_out.append(out)
            out = {}

        return UI_out


class DefaultExtractor(vcore.Extractor):

    def is_vaild_ver(self, spec_ver):
        return True if type(spec_ver) == str and re.match('\d{2}.\d{2}', spec_ver) else False

    def ext_snapshot(self, platform , spec_ver = "max"):

        out = []
        data = self._get_data().pop(platform)

        for d in data:
            tmp_out = {}

            ERD_ID = d
            others = data[d]

            if not others['excel']: continue

            versions = sorted(list(others['excel'].keys()))
            sub_versions = []

            if spec_ver == "max":
                lastest_ver = max(versions)
                sub_versions = versions
            else:
                if not self.is_vaild_ver(spec_ver):
                    sub_versions = versions
                    lastest_ver = max(versions)
                else:
                    if spec_ver in versions:
                        sub_versions = versions[:versions.index(spec_ver) + 1]
                        lastest_ver = spec_ver
                    else:
                        if spec_ver > max(versions):
                            sub_versions = versions
                            lastest_ver = max(versions)
                        elif spec_ver < min(versions):
                            sub_versions = []
                            lastest_ver = ""
                        else:
                            for v in versions:
                                if spec_ver < v:
                                    sub_versions = versions[:versions.index(v)]
                                    lastest_ver = versions[versions.index(v)-1]
                                    break

            # print("UI lastest version : <{}> for ERD : [{}]".format(lastest_ver, ERD_ID))

            if lastest_ver == "":
                continue

            print("versions : {}".format(versions))
            print("sub_versions : {}".format(sub_versions))

            tmp_out['version'] = {}

            for sv in sub_versions:
                if others['excel'][sv]['description'] == 'blank':
                    tmp_out['version'][sv] = 'deactive'
                else:
                    tmp_out['version'][sv] = 'active'

            print("output version dict: {}".format(tmp_out['version']))

            deep_excel = others['excel'][lastest_ver]
            deep_jira  = others['jira'][lastest_ver]

            # excel part : ERD table partition
            tmp_out['erd_id'] = deep_excel['erd_id']
            tmp_out['platform'] = deep_excel['platform']
            tmp_out['author'] = deep_excel['author']
            tmp_out['category'] = deep_excel['category']
            tmp_out['product_priority'] = deep_excel['product_priority']
            tmp_out['title'] = deep_excel['title']
            tmp_out['description'] = deep_excel['description']

            # jira part : ERD table partition
            tmp_out['HLD'] = deep_jira['HLD']
            tmp_out['l1_jira'] = deep_jira['l1_jira']
            tmp_out['l2_jira'] = deep_jira['l2_jira']
            tmp_out['status'] = deep_jira['status']
            tmp_out['workload'] = deep_jira['workload']
            if deep_jira['bug_jiras']:
                tmp_out['bug_jiras'] = deep_jira['bug_jiras'].split(',')
            else:
                tmp_out['bug_jiras'] = []

            # jira part : TestCases table partition
            # Now Maybe 'case_age' NOT display
            tmp_out['case_name'] = list(deep_jira['F_casetree'].keys())
            tmp_out['F_report_path'] = []
            for dj in deep_jira['F_casetree']:
                tmp_out['F_report_path'].append(deep_jira['F_casetree'][dj]['F_report_path'])

            out.append(tmp_out)

        return out


def query_switch(request):

    if request.method == "GET":
        platform = request.GET.get('platform')
        action = request.GET.get('action')

        if action == 'ERD_table_version':
            print("recored query:\n{}\n{}\n{}".format(platform,action,request.GET.get('ErdTableVersion')))
            erd_table_version = request.GET.get('ErdTableVersion')

            de = DefaultExtractor([platform.upper()])
            vcore.splitter('pick_all', extractor = de )

            out = de.ext_snapshot(platform = platform.upper(), spec_ver = erd_table_version)

            return render(request, 'LigerUI/ACIS/rex_debug/rex_test_page.htm', {'cookies' : json.dumps(out)})

        elif action == 'integration_version':
            fw_version = request.GET.get('FirmwareVersion')
            ie = IntegrationExtractor([platform],fw_version = fw_version)
            vcore.splitter('pick_all', extractor = ie )

            return render(request, 'LigerUI/ACIS/integration_page.htm', {'cookies' : json.dumps(ie.UI_data)})

        else:
            return HttpResponseNotFound("<h2> Please input 'platform' and 'action' togather.</h2>")

    elif request.method == "POST":
        print("POST request, but do nothing.")

def rex_home(request):

    de = DefaultExtractor(['SD55'])
    vcore.splitter('pick_all', extractor = de )
    out = de.ext_snapshot('SD55')
    mlogger(pformat(out))
    return render(request, 'LigerUI/ACIS/rex_debug/rex_test_page.htm', {'cookies' : json.dumps(out)})

def ERD_9X28_index(request):

    de = DefaultExtractor(['9X28'])
    vcore.splitter('pick_all', extractor = de )
    out = de.ext_snapshot('9X28')
    pp(type(out))
    return render(request, 'LigerUI/ACIS/rex_debug/rex_test_page.htm', {'cookies' : json.dumps(out)})

def ERD_9X40_index(request):

    de = DefaultExtractor(['9X40'])
    vcore.splitter('pick_all', extractor = de )
    out = de.ext_snapshot('9X40')
    return render(request, 'LigerUI/ACIS/rex_debug/rex_test_page.htm', {'cookies' : json.dumps(out)})

def ERD_SD55_index(request):

    de = DefaultExtractor(['SD55'])
    vcore.splitter('pick_all', extractor = de )
    out = de.ext_snapshot('SD55')
    return render(request, 'LigerUI/ACIS/rex_debug/rex_test_page.htm', {'cookies' : json.dumps(out)})

def columns_data_select(request):
    return render(request, 'LigerUI/ACIS/columns_data_select.htm')

def help(request):
    return render(request, 'LigerUI/ACIS/help.htm', {})

def about(request):
    return render(request, 'LigerUI/ACIS/about.htm', {})

def query(request):
    return render(request, 'LigerUI/ACIS/query.htm', {})


def do_save_excel():
    vcore.splitter('save', provider = ExcelProvider())

def do_save_jira():
    vcore.splitter('save', provider = JiraProvider())

def do_save_jenkins():
    vcore.splitter('save', provider = JenkinsProvider())

def do_save_UI():
    pass


def do_save_excel_test1():
    vcore.splitter('save', provider = ExcelProvider(test_version = 'first'))
def do_save_excel_test2():
    vcore.splitter('save', provider = ExcelProvider(test_version = 'second'))
def do_save_excel_test3():
    vcore.splitter('save', provider = ExcelProvider(test_version = 'third'))
def do_save_excel_test4():
    vcore.splitter('save', provider = ExcelProvider(test_version = 'fourth'))

def do_save_excel_test1_o():
    vcore.splitter('save', provider = ExcelProvider(platform = '9X28', test_version = 'first'))
def do_save_excel_test2_o():
    vcore.splitter('save', provider = ExcelProvider(platform = '9X28', test_version = 'second'))
def do_save_excel_test3_o():
    vcore.splitter('save', provider = ExcelProvider(platform = '9X28', test_version = 'third'))
def do_save_excel_test4_o():
    vcore.splitter('save', provider = ExcelProvider(platform = '9X28', test_version = 'fourth'))


def do_save_jira_test1():
    vcore.splitter('save', provider = JiraProvider(platform = 'SD55', test_version = 'first'))

def do_save_jira_test2():
    vcore.splitter('save', provider = JiraProvider(platform = 'SD55', test_version = 'second'))

def do_save_jira_test3():
    vcore.splitter('save', provider = JiraProvider(platform = 'SD55', test_version = 'third'))

def do_save_jira_test1_o():
    vcore.splitter('save', provider = JiraProvider(platform = '9X28', test_version = 'first'))
def do_save_jira_test2_o():
    vcore.splitter('save', provider = JiraProvider(platform = '9X28', test_version = 'second'))
def do_save_jira_test3_o():
    vcore.splitter('save', provider = JiraProvider(platform = '9X28', test_version = 'third'))



def do_save_jenkins_test1():
    vcore.splitter('save', provider = JenkinsProvider(platform = 'SD55', test_version = 'first'))
def do_save_jenkins_test2():
    vcore.splitter('save', provider = JenkinsProvider(platform = 'SD55', test_version = 'second'))
def do_save_jenkins_test3():
    vcore.splitter('save', provider = JenkinsProvider(platform = 'SD55', test_version = 'third'))

def do_save_jenkins_test1_o():
    vcore.splitter('save', provider = JenkinsProvider(platform = '9X28', test_version = 'first'))
def do_save_jenkins_test2_o():
    vcore.splitter('save', provider = JenkinsProvider(platform = '9X28', test_version = 'second'))
def do_save_jenkins_test3_o():
    vcore.splitter('save', provider = JenkinsProvider(platform = '9X28', test_version = 'third'))

supported_cmds = {
    'save_excel_data'  : do_save_excel,
    'save_jira_data'   : do_save_jira,
    'save_jenkins_data': do_save_jenkins,
    'save_UI_data'     : do_save_UI,

    'save_excel_data_test1_SD55'  : do_save_excel_test1,
    'save_excel_data_test2_SD55'  : do_save_excel_test2,
    'save_excel_data_test3_SD55'  : do_save_excel_test3,
    'save_excel_data_test4_SD55'  : do_save_excel_test4,

    'save_excel_data_test1_9X28'  : do_save_excel_test1_o,
    'save_excel_data_test2_9X28'  : do_save_excel_test2_o,
    'save_excel_data_test3_9X28'  : do_save_excel_test3_o,
    'save_excel_data_test4_9X28'  : do_save_excel_test4_o,

    'save_jira_data_test1_SD55'  : do_save_jira_test1,
    'save_jira_data_test2_SD55'  : do_save_jira_test2,
    'save_jira_data_test3_SD55'  : do_save_jira_test3,

    'save_jira_data_test1_9X28'  : do_save_jira_test1_o,
    'save_jira_data_test2_9X28'  : do_save_jira_test2_o,
    'save_jira_data_test3_9X28'  : do_save_jira_test3_o,

    'save_jenkins_data_test1_SD55'  : do_save_jenkins_test1,
    'save_jenkins_data_test2_SD55'  : do_save_jenkins_test2,
    'save_jenkins_data_test3_SD55'  : do_save_jenkins_test3,

    'save_jenkins_data_test1_9X28'  : do_save_jenkins_test1_o,
    'save_jenkins_data_test2_9X28'  : do_save_jenkins_test2_o,
    'save_jenkins_data_test3_9X28'  : do_save_jenkins_test3_o,
}

def rex_commands(request):
    return render(request, 'LigerUI/ACIS/rex_debug/rex_debug_commands.htm', {'cmds' : list(supported_cmds.keys())})

def rex_actions_dispatcher(request):
    # Maybe only one.
    for name, cmd in request.GET.items():
        if name == "command":
            if cmd and cmd in supported_cmds:
                supported_cmds[cmd]()
    return HttpResponseRedirect("/rex_commands/")


def show_time_do_excel_save():
    vcore.splitter('save', provider = RexExcelProvider(platform = 'SD55', test_version = 'first'))

def show_time_do_jira_save_first():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'first'))

def show_time_do_jira_save_second():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'second'))

def show_time_do_jira_save_third():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'third'))


def show_time_do_excel_second_update():
    vcore.splitter('save', provider = RexExcelProvider(platform = 'SD55', test_version = 'second'))
    # vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'follow'))

def show_time_do_excel_third_update():
    vcore.splitter('save', provider = RexExcelProvider(platform = 'SD55', test_version = 'third'))
    # vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'follow'))

def show_time_do_excel_fourth_update():
    vcore.splitter('save', provider = RexExcelProvider(platform = 'SD55', test_version = 'fourth'))
    # vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'follow'))

def show_time_do_follow_excel():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'follow'))


def do_step_01():
    vcore.splitter('save', provider = RexExcelProvider(platform = 'SD55', test_version = 'first'))

def do_step_02():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'first'))

def do_step_03():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'second'))

def do_step_04():
    vcore.splitter('save', provider = JenkinsProvider(platform = 'SD55', test_version = 'test01'))

def do_step_05():
    vcore.splitter('save', provider = RexExcelProvider(platform = 'SD55', test_version = 'second'))

def do_step_06():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'follow01'))

def do_step_07():
    vcore.splitter('save', provider = JenkinsProvider(platform = 'SD55', test_version = 'test02'))

def do_step_08():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'third'))

def do_step_09():
    vcore.splitter('save', provider = JenkinsProvider(platform = 'SD55', test_version = 'test03'))

def do_step_10():
    vcore.splitter('save', provider = RexExcelProvider(platform = 'SD55', test_version = 'third'))

def do_step_11():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'follow02'))

def do_step_12():
    vcore.splitter('save', provider = JenkinsProvider(platform = 'SD55', test_version = 'test04'))

def do_step_13():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'fourth'))

def do_step_14():
    vcore.splitter('save', provider = JenkinsProvider(platform = 'SD55', test_version = 'test05'))

def do_step_15():
    vcore.splitter('save', provider = RexExcelProvider(platform = 'SD55', test_version = 'fourth'))

def do_step_16():
    vcore.splitter('save', provider = RexJiraProvider(platform = 'SD55', test_version = 'follow03'))

def do_step_17():
    vcore.splitter('save', provider = JenkinsProvider(platform = 'SD55', test_version = 'test06'))

def do_step_18():
    vcore.splitter('save', provider = JenkinsProvider(platform = 'SD55', test_version = 'test07'))

show_supported_cmds = {
    'do_step_01' : do_step_01,
    'do_step_02' : do_step_02,
    'do_step_03' : do_step_03,
    'do_step_04' : do_step_04,
    'do_step_05' : do_step_05,
    'do_step_06' : do_step_06,
    'do_step_07' : do_step_07,
    'do_step_08' : do_step_08,
    'do_step_09' : do_step_09,
    'do_step_10' : do_step_10,
    'do_step_11' : do_step_11,
    'do_step_12' : do_step_12,
    'do_step_13' : do_step_13,
    'do_step_14' : do_step_14,
    'do_step_15' : do_step_15,
    'do_step_16' : do_step_16,
    'do_step_17' : do_step_17,
    'do_step_18' : do_step_18,
}

global_cmd = ""
def rex_show_actions_dispatcher(request):
    # assert False, "Rex >> {}".format(request.path)
    print("Hook: GET->{} , POST->{}, path->{}".format(request.GET,request.POST, request.path))
    global global_cmd
    for name, cmd in request.GET.items():
        if name == "command":
            if cmd and cmd in show_supported_cmds:
                show_supported_cmds[cmd]()
                global_cmd = cmd
    #return HttpResponseRedirect("/rex_commands/")
    return HttpResponseRedirect("/rex_prompt/")

def rex_prompt(request):
    global global_cmd
    return render(request, 'LigerUI/ACIS/rex_debug/prompt.htm', {'cmd' : global_cmd})

def rex_test_query(request):
    from ..vcore import Query
    #q = Query('integration_query_exactly', platform= 'SD55', fw_version="SWI9X28A_00.11.01.06", test_date="2019-02-03")
    # q = Query('integration_query_exactly', platform= 'SD55', fw_version="SWI9X28A_00.11.01.06", test_date="2019-01-03")
    # q = Query('night_regression_query', platform= 'SD55', test_date="2019-01-03")
    # q = Query('ERD_caselist_query', platform= 'SD55', ERD_ID="04.60.26")
    q = Query('casename_query', platform= 'SD55', casename = "test_case_03_alpha_02")
    q.do_query()
    return HttpResponse("done")
