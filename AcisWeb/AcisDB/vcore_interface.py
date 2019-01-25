#! /usr/bin/env python3
# coding = utf-8

"""
"""

from pprint import pprint as pp, pformat
import logging,re,os

from . import vcore
from AcisDB import erd_excel_retrieve, jira_scan

class ExcelProvider(vcore.Provider):

    def __init__(self, platform, version, erd_excel_file):
        self.platform = platform
        self.test_version = version
        self.erd_file = erd_excel_file

    def get_data(self):
        t = erd_excel_retrieve.read_excel(self.erd_file, self.platform, self.test_version)

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

    def __init__(self, platform, jira_server_addr, jira_user, jira_passwd):
        self.platform = platform
        self.jira_server_addr = jira_server_addr
        self.jira_user = jira_user
        self.jira_pwd = jira_passwd

    def get_data(self):
        t = jira_scan.retrieve_new_feature_jiras(self.jira_server_addr, self.jira_user, self.jira_user, self.platform)

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


class AutoJenkinsProvider(vcore.Provider):

    def __init__(self, result_path):
        self.result_path = result_path

    def get_log_files(self, path):
        if not os.path.isdir(path):
            raise TypeError

        log_files = []
        for root, dirs, files in os.walk(path):
            for f in files:
                if f.startswith('ACIS') and f.endswith('.log'):
                    log_files.append(os.path.join(root, f))

        return log_files

    def get_element(self, files):
        """
        Element:
        - TESTCASE - Result - Test_Date - Test_Times - Test_Log - Test_IR_Report
        - Platform - FW_version - PASS_TIMES - FAIL_TIMES
        """
        record = {}

        re_g = {
            'testcase'       : 1,
            'result'         : 2,
            'test_date'      : 3,
            'test_times'     : 4,
            'test_log'       : 5,
            'test_ir_report' : 6,

            'product'        : 1,
            'fw_version'     : 2,
        }

        platform_maps = {
            '9X28' : ('AR7588',),
            '9X40' : ('AR7598',),
        }

        re_SWI_ACIS = re.compile(r'TESTCASE:\[(.*?)\]\s*Result:\[(.*?)\]\s*Test_Date:\[(.*?)\]\s*Test_Times:\[(.*?)\]\s*Test_Log:\[(.*?)\]\s*Test_IR_Report:\[(.*?)\]\s*')
        re_AT_ATI   = re.compile(r'\[Model: (.*)<CR><LF>Revision: (.*?)\s')

        for f in files:
            record[f] = {}
            last_one_touch = False
            once_flag      = False

            pass_times = 0
            fail_times = 0

            for line in reversed(list(open(f))):
                if line.startswith('<SWI:ACIS>'):

                    gs = re_SWI_ACIS.search(line)

                    if gs and gs.group(re_g['result']) == 'PASS':
                        pass_times += 1
                    elif gs and gs.group(re_g['result']) == 'FAIL':
                        fail_times += 1

                    if gs and not last_one_touch:
                        record[f]['TESTCASE'] = gs.group(re_g['testcase'])
                        record[f]['Result']   = gs.group(re_g['result'])
                        record[f]['Test_Date']  = gs.group(re_g['test_date'])
                        record[f]['Test_Times'] = gs.group(re_g['test_times'])
                        record[f]['Test_Log']   = gs.group(re_g['test_log'])
                        record[f]['IR_Report_Path'] = gs.group(re_g['test_ir_report'])
                        last_one_touch = True

                rs = re_AT_ATI.search(line)

                if rs and not once_flag:
                    for platform, products in platform_maps.items():
                        if rs.group(re_g['product']) in products:
                            record[f]['Platform'] = platform

                    record[f]['FW_version'] = rs.group(re_g['fw_version'])

                    once_flag = True

            record[f]['PASS_TIMES'] = pass_times
            record[f]['FAIL_TIMES'] = fail_times

        return record

    def translate_element(self, files, record):
        out = []
        once_dict ={'jenkins'  : {'IR_casetree' : {}}}

        any=0
        once_dict['PLATFORM'] = record[files[any]]['Platform']

        ref = once_dict['jenkins']['IR_casetree']
        for f in files:
            ref[record[f]['TESTCASE']] = {
                'fw_version'   : record[f]['FW_version'],
                'test_result'  : record[f]['Result'],
                'test_log'     : record[f]['Test_Log'],
                'test_date'    : record[f]['Test_Date'],
                'IR_report_path' : record[f]['IR_Report_Path'],
            }

        out.append(once_dict)
        return out

    def get_data(self):
        files = self.get_log_files(self.result_path)
        record = self.get_element(files)
        return self.translate_element(files, record)

    @property
    def formatted_rawdata(self):
        return self.get_data()

class JenkinsProvider(vcore.Provider):

    from .rex_debug.test_cookies_of_rex import (
        test_get_jenkins_data_first,
        test_get_jenkins_data_second,
        test_get_jenkins_data_third,
    )

    self_test = {
        "first" : test_get_jenkins_data_first,
        "second" : test_get_jenkins_data_second,
        "third" : test_get_jenkins_data_third,
    }

    def __init__(self, platform, test_version):
        self.platform = platform
        self.test_version = test_version

    def get_data(self):
        t = JenkinsProvider.self_test[self.test_version](self.platform)

        logger_to_jenkins = logging.getLogger(__name__ + '.from_jenkins')
        logger_to_jenkins.info(pformat(t))

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

            # 'minor_ver' is useful when Erds Table update, but no Jenkins Test-Report upload.
            from heapq import nlargest
            top_two = nlargest(2, sub_versions)
            if top_two and len(top_two) == 2:
                minor_ver = top_two[1]
            elif top_two and len(top_two) == 1:
                minor_ver = top_two[0] # == latest_Ver

            if lastest_ver == "":
                continue

            # print("versions : {}".format(versions))
            # print("sub_versions : {}".format(sub_versions))
            # print("minor version : {}".format(minor_ver))
            # print("latest version : {}".format(lastest_ver))

            tmp_out['version'] = {}

            #for sv in sub_versions:
            #    if others['excel'][sv]['description'] == 'blank':
            #        tmp_out['version'][sv] = 'deactive'
            #    else:
            #        tmp_out['version'][sv] = 'active'

            versions_list_string = ''
            for sv in sub_versions:
                if others['excel'][sv]['description'] == 'blank':
                    versions_list_string = versions_list_string + sv + '-deactive,'
                else:
                    versions_list_string = versions_list_string + sv + '-active,'
            tmp_out['version'] = versions_list_string
            # print("output version dict: {}".format(tmp_out['version']))

            deep_excel = others['excel'][lastest_ver]

            deep_jira  = others['jira'][lastest_ver]
            minor_deep_jira = others['jira'][minor_ver]

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
            tmp_out['milestone'] = deep_jira['milestone']
            if deep_jira['bug_jiras']:
                tmp_out['bug_jiras'] = deep_jira['bug_jiras'].split(',')
            else:
                tmp_out['bug_jiras'] = []

            # jira part : TestCases table partition
            # Hope NOT display 'test_case' and 'F_report_path' on UI for the item that description is 'blank'.
            if deep_excel['description'] != 'blank':
                tmp_out['case_name'] = list(deep_jira['F_casetree'].keys())
                tmp_out['F_report_path'] = []
                for dj in deep_jira['F_casetree']:
                    tmp_out['F_report_path'].append(deep_jira['F_casetree'][dj]['F_report_path'])

                tmp_out['test_result'] = []
                tmp_out['test_report'] = []

                for casename in tmp_out['case_name']:
                    if deep_jira['IR_report']:
                        tmp_out['test_result'].append((casename, deep_jira['IR_report'][casename]['test_result']))
                        tmp_out['test_report'].append((casename,
                                                       deep_jira['IR_report'][casename]['fw_version'],
                                                       deep_jira['IR_report'][casename]['IR_report_path']))
                    elif casename in minor_deep_jira['IR_report'].keys():
                        # minor_deep_jira = others['jira'][minor_ver]
                        if minor_deep_jira['IR_report']:
                            tmp_out['test_result'].append((casename, minor_deep_jira['IR_report'][casename]['test_result']))
                            tmp_out['test_report'].append((casename,
                                                           minor_deep_jira['IR_report'][casename]['fw_version'],
                                                           minor_deep_jira['IR_report'][casename]['IR_report_path']))
            else:
                tmp_out['case_name'] = ""
                tmp_out['F_report_path'] = []
                tmp_out['test_result'] = []
                tmp_out['test_report'] = []

            out.append(tmp_out)
        return out
