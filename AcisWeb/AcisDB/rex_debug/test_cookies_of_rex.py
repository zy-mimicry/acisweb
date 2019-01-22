import random

# 20 items
erd_ids = [
    # alpha-01
    "04.60.25",
    "04.60.26",
    "04.60.27",
    "04.60.28",
    "04.60.29",

    # alpha-02
    "04.60.30",
    "04.60.31",
    "04.60.32",
    "04.60.33",
    "04.60.34",

    # alpha-03
    "04.60.35",
    "04.60.36",
    "04.60.37",
    "04.60.38",
    "04.60.39",

    # beta-01
    "04.60.40",
    "04.60.41",
    "04.60.42",
    "04.60.43",
    "04.60.44",
]

without_erd_ids = [
    "04.60.141",
    "04.60.142",
    "04.60.143",
    "04.60.144",
    "04.60.145",
]

more_erd_ids = [

    # alpha-01
    "04.60.45",
    "04.60.46",
    "04.60.47",
    "04.60.48",
    "04.60.49",

    # alpha-02
    "04.60.60",
    "04.60.61",
    "04.60.62",

    # alpha-03
    "04.60.70",
    "04.60.71",
    "04.60.72",
    "04.60.73",
    "04.60.74",
]

alpha_01_new = slice(0,5)
alpha_02_new = slice(5,8)
alpha_03_new = slice(8,13)

second_erd_ids = {
    'modified':[
        # alpha-01 items
        "04.60.25",
        "04.60.26",
    ],
    'modified_testcase' : {
        "04.60.25" : ['modified_test_case_01'],
        "04.60.26" : ['modified_test_case_02'],
    },
    'new' : [
        # new
        "04.60.45",
        "04.60.46",
        "04.60.47",
        "04.60.48",
        "04.60.49",
    ],
    'new_testcase': {
        "04.60.45" : ['new_test_case_01'],
        "04.60.46" : ['new_test_case_02'],
        "04.60.47" : ['new_test_case_03'],
        "04.60.48" : ['new_test_case_04'],
        "04.60.49" : ['new_test_case_05'],
    }
}

third_erd_ids = {
    'new' : [
        # new
        "04.60.60",
        "04.60.61",
        "04.60.62",
    ],
    'new_testcase':{
        "04.60.60" : ['new_test_case_06'],
        "04.60.61" : ['new_test_case_07'],
        "04.60.62" : ['new_test_case_08'],
    },
    'deactived' : [
        # alpha-02 items
        "04.60.30",
        "04.60.31",
    ],
    'deactived_testcase' : {
        "04.60.30" : ['maybe_no_testcase'],
        "04.60.31" : ['maybe_no_testcae_yet'],
    }

}

fourth_erd_ids = {
    'active' : [
        # alpha-02 items
        "04.60.30",
    ],
    'new' : [
        # new
        "04.60.70",
        "04.60.71",
        "04.60.72",
        "04.60.73",
        "04.60.74",
    ],
    'new_testcase' : {
        "04.60.70" : ['new_test_case_09'],
        "04.60.71" : ['new_test_case_10'],
        "04.60.72" : ['new_test_case_11'],
        "04.60.73" : ['new_test_case_12'],
        "04.60.74" : ['new_test_case_13'],
    },
    'active_testcase' : {
        "04.60.30" : ['active_test_case_01'],
    }
}


category = [
    "07 - Cloud Platform",
    "09 - Performances",
    "10 - Regulatory App. & Env. Compliance ",
]

title = [
    "eUICC support ",
    "Startup Time " ,
    "Spy mode ",
    "WiFi Hotspot ",
]

description = [
    'The module shall support an AT command to configure modem to bootup to SPY mode. ',
    'The module shall support a Legato API to enter spy mode when modem registers on UMTS network, the Legato API will not take effect when modem registers on LTE network. ',
    "The module shall automatically detect the 'FILE' type CWE images, decode and copy to a specific path of EFS. ",
    "The module should automatically detect the NV update file from a specific path in EFS, then parse each NV/EFS item from the file and write it to appropriate NV/EFS location, the parsed file should be deleted automatically after NV update is completed. ",
    "The module firmware design shall not change the NV item structure for a given NV item during the course of development and product maintenance. ",

    "The module shall support eUICC device requirement per GSMA specification Annex G for DEV1, DEV2, DEV3, DEV4, DEV5, DEV6, DEV8 and DEV9. See Document \"Remote Provisioning Architecture for Embedded UICC Technical Specification v1.0 17 December 2013\"",
    ' The module should support eUICC device requirement per GSMA specification Annex G for DEV7. See Document "Remote Provisioning Architecture for Embedded UICC Technical Specification v1.0 17 December 2013"',
    "The module shall support local SIM profile switch for following SIM manufacturer, including VALID, Gemalto, G&D, Oberthur and Morpho. ",

    "The module's Legato framework and service shall be ready to use in 20s from power on or reset. ",
    "blank ",
    "The module shall complete loading kernel image (i.e. to start launching \"init\" process) within 4.5s after power-on or reset, even with security signed images. ",
    "blank ",
    "The module shall support USB ready (i.e. USB enumeration complete on device side) within 10s after power-on/reset, even with security signed images. ",
    "The module shall support full emergency call functionality within 20s from module power-on or reset, even with security signed images. ",
    "Legato start-up time itself shall not be greater than 4s (i.e. from rootfs starts loading Legato to all Legato services are functional). ",
    "The module shall support an AT command to exit spy mode. ",
    "The module shall support an AT command to configure if module can exit spy mode by AT command. ",
    "The module shall support an AT command to enter spy mode when modem registers on UMTS network, and the AT command will not take effect when modem registers on LTE network. ",
]

product_priority = ['MUST', 'SHOULD']

status = ['DONE', "UNDO"]

author = ["Cassie Sheng", "Victor He", "Joe Liu",]

version = ["01.00", "01.01", "01.02", "01.03", "01.04",]

HLD = ['https://link_to_HLD_01', "https://link_to_HLD_02"]

l1_jira = ['QTI9X28-4000']
l2_jira = ['QTI9X28-3077']

bug_jiras = ['QTI9X28-4072',
             'QTI9X28-4077',
             'QTI9X28-4007',]

platform = ['SD55']

workload = ['1d', '2d', '1w', '4h']

case_name = ["ACIS_A_S_Test_Temp_Volt","ACIS_A_S_PowerOff_Linux","ACIS_A_S_Reset_Linux_HW"]

case_age = ['2018-11-25', '2017-11-24', '2011-1-1']

test_result = ['PASS', "FAIL"]

test_log = ['ftp://acis_testcase_log_path01', "ftp://acis_testcase_log_path03","ftp://acis_testcase_log_path02"]

report_path = ['QTI9X28-5555','QTI9X28-0000','QTI9X28-7777' ]

fw_version = ['SWI9X28A_00.19.02.13','SWI9X28A_00.19.01.13','SWI9X28A_00.19.02.12']

test_date = ['2011-2-22', '2015-12-1', '2014-11-9']

def test_get_excel_data_first(platform):

    ret = []
    for e in erd_ids:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['excel'] = {
            'erd_id' : e,
            'category' : random.choice(category),
            'title' : random.choice(title),
            'description' : 'This is a [ first ] version.',
            'product_priority' : random.choice(product_priority),
            'author' : random.choice(author),
            'version' : '01.00',
            'platform' : platform,
        }
        ret.append(out)
    return ret

def test_get_excel_data_second(platform):
    "Added 5, Modified 2"
    ret = []

    for s in second_erd_ids:
        if s == "modified":
            for m in second_erd_ids[s]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'This is a [ modified first ] version.',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    #'version' : '02.00',
                    'version' : '01.01',
                    'platform' : platform,
                }
                ret.append(out)

        elif s == "new":
            for m in second_erd_ids[s]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'This is a [ second new ] version.',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    #'version' : '02.00',
                    'version' : '01.01',
                    'platform' : platform,
                }
                ret.append(out)

    return ret

def test_get_excel_data_third(platform):
    "Added 3, Deactived 2"
    ret = []

    for t in third_erd_ids:
        if t == "new":
            for m in third_erd_ids[t]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'This is a [ third new ] version.',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    # 'version' : '03.00',
                    'version' : '01.02',
                    'platform' : platform,
                }
                ret.append(out)

        elif t == "deactived":
            for m in third_erd_ids[t]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'blank',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    #'version' : '03.00',
                    'version' : '01.02',
                    'platform' : platform,
                }
                ret.append(out)

    return ret


def test_get_excel_data_fourth(platform):
    "Active 1 of deactived erd, and new add 5 erds"
    ret = []

    for f in fourth_erd_ids:
        if f == "active":
            for m in fourth_erd_ids[f]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'This is a [ re-active ] version.',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    #'version' : '04.00',
                    'version' : '01.03',
                    'platform' : platform,
                }
                ret.append(out)
        elif f == 'new':
            for m in fourth_erd_ids[f]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'This is a [ fourth new ] version.',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    #'version' : '04.00',
                    'version' : '01.03',
                    'platform' : platform,
                }
                ret.append(out)
    return ret


def test_get_jira_data_first(platform):

    ret = []
    for e in erd_ids:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : "https://link_to_HLD_01",
            'status' : "UNDO",
            'l1_jira' : "QTI9X28-4000",
            'l2_jira' : "QTI9X28-3077",
            'bug_jiras' : ','.join(['QTI9X28-4072', 'QTI9X28-4077']),
            'platform' : platform,
            'workload' : '2d',
            'milestone' : 'alpha-01',

            'F_casetree' : [
                {
                    'case_name' : "ACIS_A_S_Test_Temp_Volt",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "ACIS_A_S_Test_Temp_ssss",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "ACIS_A_S_Test_Temp_abcd",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)
    return ret

def test_get_jira_data_second(platform):

    ret = []
    for e in erd_ids:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : "https://link_to_HLD_02",
            'status' : "DONE",
            'l1_jira' : "QTI9X28-1111",
            'l2_jira' : "QTI9X28-2222",
            'bug_jiras' : ','.join(['QTI9X28-3333', 'QTI9X28-7777']),
            'platform' : platform,
            'workload' : '3d',
            'milestone' : 'alpha-02',

            'F_casetree' : [
                {
                    'case_name' : "ACIS_A_S_Test_Temp_Volt_11111",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "ACIS_A_S_Test_Temp_ssss_2222",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "ACIS_A_S_Test_Temp_abcd_sdfk",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)
    return ret

def test_get_jira_data_third(platform):

    ret = []

    for e in without_erd_ids:

        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : "https://link_to_HLD_01",
            'status' : "UNDO",
            'l1_jira' : "QTI9X28-4000",
            'l2_jira' : "QTI9X28-3077",
            'bug_jiras' : ','.join(['QTI9X28-4072', 'QTI9X28-4077']),
            'platform' : platform,
            'workload' : '2d',
            'milestone' : 'alpha-03',

            'F_casetree' : [
                {
                    'case_name' : "ACIS_A_S_Test_Temp_Volt",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "ACIS_A_S_Test_Temp_ssss",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "ACIS_A_S_Test_Temp_abcd",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    return ret

def test_get_jira_data():

    ret = []
    for e in erd_ids:
        out = {}
        out['PLATFORM'] = random.choice(platform)
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : random.choice(status),
            'l1_jira' : random.choice(l1_jira),
            'l2_jira' : random.choice(l2_jira),
            'bug_jiras' : random.choice(bug_jiras),
            'platform' : random.choice(platform),
            'workload' : random.choice(workload),

            'F_casetree' : [
                {
                    'case_name' : "ACIS_A_S_Test_Temp_Volt",
                    'case_age' : random.choice(case_age),
                    'F_report_path' : ','.join(report_path),
                },
                {
                    'case_name' : "ACIS_A_S_Test_Temp_ssss",
                    'case_age' : random.choice(case_age),
                    'F_report_path' : ','.join(report_path),
                },
                {
                    'case_name' : "ACIS_A_S_Test_Temp_abcd",
                    'case_age' : random.choice(case_age),
                    'F_report_path' : ','.join(report_path),
                },
            ],
        }
        ret.append(out)
    return ret


##
# jenkins Simulation data
# 1. simulate 2 times upload the integration test list, different fw_version.
# 2. simulate the same fw_version of integration test and upload 2 times, chech combin function
# 3. supply the query function for integration test by FW_Version
##

# TODO 04
def show_time_jenkins_test_01(platform):
    ret = []
    out = {}
    out['PLATFORM'] = platform
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            "test_case_01_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.01",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org",
                'test_date' : "2019-01-01",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_02_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.01",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.2",
                'test_date' : "2019-01-01",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_03_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.01",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-01",
                'IR_report_path' : "ftp://report_location.org",
            },
        }
    }
    ret.append(out)
    return ret

# TODO 7
def show_time_jenkins_test_02(platform):
    ret = []
    out = {}
    out['PLATFORM'] = platform
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            "test_case_01_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.02",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org",
                'test_date' : "2019-01-02",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_02_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.02",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.2",
                'test_date' : "2019-01-02",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_03_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.02",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-02",
                'IR_report_path' : "ftp://report_location.org",
            },


            "modified_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.02",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-02",
                'IR_report_path' : "ftp://report_location.org",
            },
            "modified_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.02",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-02",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.02",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-02",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.02",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-02",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_03" : {
                'fw_version' : "SWI9X28A_00.11.01.02",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-02",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_04" : {
                'fw_version' : "SWI9X28A_00.11.01.02",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-02",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_05" : {
                'fw_version' : "SWI9X28A_00.11.01.02",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-02",
                'IR_report_path' : "ftp://report_location.org",
            },
        }
    }
    ret.append(out)
    return ret

# TODO 9
def show_time_jenkins_test_03(platform):
    ret = []
    out = {}
    out['PLATFORM'] = platform
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            "test_case_01_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_02_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.2",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            # "test_case_03_alpha_01" : {
            #     'fw_version' : "SWI9X28A_00.11.01.03",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },


            "modified_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "modified_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_03" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            # "new_test_case_04" : {
            #     'fw_version' : "SWI9X28A_00.11.01.03",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            "new_test_case_05" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },


            "test_case_01_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },

            "test_case_02_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },

            "test_case_03_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.03",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
        }
    }
    ret.append(out)
    return ret


# TODO 12
def show_time_jenkins_test_04(platform):

    ret = []
    out = {}
    out['PLATFORM'] = platform
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            "test_case_01_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_02_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.2",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_03_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },


            "modified_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "modified_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_03" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_04" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_05" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },


            "test_case_01_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },

            "test_case_02_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },

            "test_case_03_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },


            "new_test_case_06" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_07" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_08" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },


            "maybe_no_testcase" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "maybe_no_testcae_yet" : {
                'fw_version' : "SWI9X28A_00.11.01.04",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
        }
    }
    ret.append(out)
    return ret

# TODO 14
def show_time_jenkins_test_05(platform):
    ret = []
    out = {}
    out['PLATFORM'] = platform
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            # "test_case_01_alpha_01" : {
            #     'fw_version' : "SWI9X28A_00.11.01.05",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org",
            #     'test_date' : "2019-01-05",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "test_case_02_alpha_01" : {
            #     'fw_version' : "SWI9X28A_00.11.01.05",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.2",
            #     'test_date' : "2019-01-05",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "test_case_03_alpha_01" : {
            #     'fw_version' : "SWI9X28A_00.11.01.05",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-05",
            #     'IR_report_path' : "ftp://report_location.org",
            # },


            "modified_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "modified_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_03" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_04" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_05" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },


            "test_case_01_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },

            "test_case_02_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },

            "test_case_03_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },


            "new_test_case_06" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_07" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_08" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },


            "maybe_no_testcase" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "maybe_no_testcae_yet" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },


            "test_case_01_alpha_03" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_02_alpha_03" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_03_alpha_03" : {
                'fw_version' : "SWI9X28A_00.11.01.05",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-05",
                'IR_report_path' : "ftp://report_location.org",
            },
        }
    }
    ret.append(out)
    return ret


# TODO 17
def show_time_jenkins_test_06(platform):

    ret = []
    out = {}
    out['PLATFORM'] = platform
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            "test_case_01_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_02_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.2",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_03_alpha_01" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },


            "modified_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "modified_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_03" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_04" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_05" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },


            "test_case_01_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },

            "test_case_02_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },

            "test_case_03_alpha_02" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },


            "new_test_case_06" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_07" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_08" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },


            "maybe_no_testcase" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "maybe_no_testcae_yet" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },


            "test_case_01_alpha_03" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_02_alpha_03" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_03_alpha_03" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },

            "active_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_09" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_10" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_11" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_12" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
            "new_test_case_13" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-06",
                'IR_report_path' : "ftp://report_location.org",
            },
        }
    }
    ret.append(out)
    return ret

# TODO 18
def show_time_jenkins_test_07(platform):

    ret = []
    out = {}
    out['PLATFORM'] = platform
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            # "test_case_01_alpha_01" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "test_case_02_alpha_01" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.2",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "test_case_03_alpha_01" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },


            "modified_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-02-03",
                'IR_report_path' : "xxxftp://report_location.org",
            },
            "modified_test_case_02" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-02-03",
                'IR_report_path' : "xxxftp://report_location.org",
            },
            "new_test_case_01" : {
                'fw_version' : "SWI9X28A_00.11.01.06",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-02-03",
                'IR_report_path' : "xxxftp://report_location.org",
            },
            # "new_test_case_02" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "new_test_case_03" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "new_test_case_04" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "new_test_case_05" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },


            # "test_case_01_alpha_02" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },

            # "test_case_02_alpha_02" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },

            # "test_case_03_alpha_02" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },


            # "new_test_case_06" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "new_test_case_07" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "new_test_case_08" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },


            # "maybe_no_testcase" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "maybe_no_testcae_yet" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },


            # "test_case_01_alpha_03" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "test_case_02_alpha_03" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "test_case_03_alpha_03" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },

            # "active_test_case_01" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "new_test_case_09" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "new_test_case_10" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "new_test_case_11" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "new_test_case_12" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
            # "new_test_case_13" : {
            #     'fw_version' : "SWI9X28A_00.11.01.06",
            #     'test_result' : "PASS",
            #     'test_log' : "ftp://log_location.org.3",
            #     'test_date' : "2019-01-03",
            #     'IR_report_path' : "ftp://report_location.org",
            # },
        }
    }
    ret.append(out)
    return ret

def test_get_jenkins_data_first(platform):

    ret = []
    out = {}
    out['PLATFORM'] = platform
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            #'ACIS_A_S_Test_Temp_Volt' : {
            "test_case_01_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            #'ACIS_A_S_Test_Temp_ssss' : {
            "test_case_02_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.2",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            #'ACIS_A_S_Test_Temp_abcd' : {
            "test_case_03_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_04_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_05_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_06_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
        }
    }
    ret.append(out)
    return ret

def test_get_jenkins_data_second(platform):

    ret = []
    out = {}
    out['PLATFORM'] = platform
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            #'ACIS_A_S_Test_Temp_Volt' : {
            "test_case_01_alpha_01" : {
                'fw_version' : "SWI9X28A_00.29.02.13",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            #'ACIS_A_S_Test_Temp_ssss' : {
            "test_case_02_alpha_01" : {
                'fw_version' : "SWI9X28A_00.29.02.13",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.2",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            #'ACIS_A_S_Test_Temp_abcd' : {
            "test_case_03_alpha_01" : {
                'fw_version' : "SWI9X28A_00.29.02.13",
                'test_result' : "FAIL",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_04_alpha_01" : {
                'fw_version' : "SWI9X28A_00.29.02.13",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_05_alpha_01" : {
                'fw_version' : "SWI9X28A_00.29.02.13",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_06_alpha_01" : {
                'fw_version' : "SWI9X28A_00.29.02.13",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-01-03",
                'IR_report_path' : "ftp://report_location.org",
            },
        }
    }
    ret.append(out)
    return ret

def test_get_jenkins_data_third(platform):

    # fw_version = ['SWI9X28A_00.19.02.13','SWI9X28A_00.19.01.13','SWI9X28A_00.19.02.12']

    ret = []
    out = {}
    out['PLATFORM'] = platform
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            #'ACIS_A_S_Test_Temp_Volt' : {
            "test_case_01_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org",
                'test_date' : "2019-11-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            #'ACIS_A_S_Test_Temp_ssss' : {
            "test_case_02_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.2",
                'test_date' : "2019-11-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            #'ACIS_A_S_Test_Temp_abcd' : {
            "test_case_03_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-11-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_04_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-11-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_05_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-11-03",
                'IR_report_path' : "ftp://report_location.org",
            },
            "test_case_06_alpha_01" : {
                'fw_version' : "SWI9X28A_00.19.02.13",
                'test_result' : "PASS",
                'test_log' : "ftp://log_location.org.3",
                'test_date' : "2019-11-03",
                'IR_report_path' : "ftp://report_location.org",
            },
        }
    }
    ret.append(out)
    return ret

def test_get_jenkins_data():

    ret = []
    out = {}
    out['PLATFORM'] = random.choice(platform)
    out['ERD_ID'] = ""
    out['jenkins'] = {
        'IR_casetree' : {
            'ACIS_A_S_Test_Temp_Volt' : {
                'fw_version' : random.choice(fw_version),
                'test_result' : random.choice(test_result),
                'test_log' : random.choice(test_log),
                'test_date' : random.choice(test_date),
                'IR_report_path' : random.choice(report_path)
            },
            'ACIS_A_S_Test_Temp_ssss' : {
                'fw_version' : random.choice(fw_version),
                'test_result' : random.choice(test_result),
                'test_log' : random.choice(test_log),
                'test_date' : random.choice(test_date),
                'IR_report_path' : random.choice(report_path)
            },
            'ACIS_A_S_Test_Temp_abcd' : {
                'fw_version' : random.choice(fw_version),
                'test_result' : random.choice(test_result),
                'test_log' : random.choice(test_log),
                'test_date' : random.choice(test_date),
                'IR_report_path' : random.choice(report_path)
            }
        }
    }
    ret.append(out)
    return ret

#TODO 01
def show_time_first_from_excel(platform):

    ret = []
    for e in erd_ids:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['excel'] = {
            'erd_id' : e,
            'category' : random.choice(category),
            'title' : random.choice(title),
            'description' : 'This is a [ first import ] version (01.00).',
            'product_priority' : random.choice(product_priority),
            'author' : random.choice(author),
            'version' : '01.00',
            'platform' : platform,
        }
        ret.append(out)
    return ret


# TODO 5
def show_time_second_from_excel(platform):
    "Added 5, Modified 2"
    ret = []

    for s in second_erd_ids:
        if s == "modified":
            for m in second_erd_ids[s]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'This is a [ modified from first ] version (02.00).',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    'version' : '02.00',
                    'platform' : platform,
                }
                ret.append(out)

        elif s == "new":
            for m in second_erd_ids[s]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'This is [ new ] version (02.00).',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    'version' : '02.00',
                    'platform' : platform,
                }
                ret.append(out)

    return ret

# TODO 10
def show_time_third_from_excel(platform):
    "Added 3, Deactived 2"
    ret = []

    for t in third_erd_ids:
        if t == "new":
            for m in third_erd_ids[t]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'This is a [ new ] version (03.00).',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    'version' : '03.00',
                    'platform' : platform,
                }
                ret.append(out)

        elif t == "deactived":
            for m in third_erd_ids[t]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'blank',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    'version' : '03.00',
                    'platform' : platform,
                }
                ret.append(out)

    return ret

# TODO 15
def show_time_fourth_from_excel(platform):
    "Active 1 of deactived erd, and new add 5 erds"
    ret = []

    for f in fourth_erd_ids:
        if f == "active":
            for m in fourth_erd_ids[f]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'This is a [ re-active ] version (04.00).',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    'version' : '04.00',
                    'platform' : platform,
                }
                ret.append(out)
        elif f == 'new':
            for m in fourth_erd_ids[f]:
                out = {}
                out['PLATFORM'] = platform
                out['ERD_ID'] = m
                out['excel'] = {
                    'erd_id' : m,
                    'category' : random.choice(category),
                    'title' : random.choice(title),
                    'description' : 'This is a [ new ] version (04.00).',
                    'product_priority' : random.choice(product_priority),
                    'author' : random.choice(author),
                    'version' : '04.00',
                    'platform' : platform,
                }
                ret.append(out)
    return ret

# TODO 6
def follow_second_excel_update_jira(platform):
    ret = []

    for e in second_erd_ids['new']:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4001",
            'l2_jira' : "QTI9X28-3001",
            'bug_jiras' : "QTI9X28-1000",
            'platform' : platform,
            'workload' : "4d",
            'milestone' :"alpha-01",
            'F_casetree' : [
                {
                    'case_name' : second_erd_ids['new_testcase'][e][0],
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    for e in second_erd_ids['modified']:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4001",
            'l2_jira' : "QTI9X28-3001",
            'bug_jiras' : "QTI9X28-1000",
            'platform' : platform,
            'workload' : "4d",
            'milestone' :"alpha-01",
            'F_casetree' : [
                {
                    'case_name' : second_erd_ids['modified_testcase'][e][0],
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    return ret

# TODO 11
def follow_third_excel_update_jira(platform):
    ret = []

    for e in third_erd_ids['new']:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4001",
            'l2_jira' : "QTI9X28-3001",
            'bug_jiras' : "QTI9X28-1000",
            'platform' : platform,
            'workload' : "4d",
            'milestone' :"alpha-02",
            'F_casetree' : [
                {
                    'case_name' : third_erd_ids['new_testcase'][e][0],
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    for e in third_erd_ids['deactived']:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4001",
            'l2_jira' : "QTI9X28-3001",
            'bug_jiras' : "QTI9X28-1000",
            'platform' : platform,
            'workload' : "4d",
            'milestone' :"alpha-02",
            'F_casetree' : [
                {
                    'case_name' : third_erd_ids['deactived_testcase'][e][0],
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    return ret


# TODO 16
def follow_fourth_excel_update_jira(platform):
    ret = []

    for e in fourth_erd_ids['new']:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4001",
            'l2_jira' : "QTI9X28-3001",
            'bug_jiras' : "QTI9X28-1000",
            'platform' : platform,
            'workload' : "4d",
            'milestone' :"alpha-03",
            'F_casetree' : [
                {
                    'case_name' : fourth_erd_ids['new_testcase'][e][0],
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    for e in fourth_erd_ids['active']:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4001",
            'l2_jira' : "QTI9X28-3001",
            'bug_jiras' : "QTI9X28-1000",
            'platform' : platform,
            'workload' : "4d",
            'milestone' :"alpha-02",
            'F_casetree' : [
                {
                    'case_name' : fourth_erd_ids['active_testcase'][e][0],
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)
    return ret

def show_time_follow_excel_update_jira(platform):

    ret = []

    for e in more_erd_ids[alpha_01_new]:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4001",
            'l2_jira' : "QTI9X28-3001",
            'bug_jiras' : "QTI9X28-1000",
            'platform' : platform,
            'workload' : "4d",
            'milestone' :"alpha-01",
            'F_casetree' : [
                {
                    'case_name' : "test_case_04_alpha_01",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_05_alpha_01",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_06_alpha_01",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    for e in more_erd_ids[alpha_02_new]:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4002",
            'l2_jira' : "QTI9X28-3002",
            'bug_jiras' : "QTI9X28-1002",
            'platform' : platform,
            'workload' : "4d",
            'milestone' :"alpha-02",
            'F_casetree' : [
                {
                    'case_name' : "test_case_04_alpha_02",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_05_alpha_02",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_06_alpha_02",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    for e in more_erd_ids[alpha_03_new]:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4003",
            'l2_jira' : "QTI9X28-3003",
            'bug_jiras' : "QTI9X28-1003",
            'platform' : platform,
            'workload' : "2d",
            'milestone' :"alpha-03",
            'F_casetree' : [
                {
                    'case_name' : "test_case_04_alpha_03",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_05_alpha_03",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_06_alpha_03",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    #ret += show_time_third_from_jira(platform)

    return ret


# TODO 02
def show_time_first_from_jira(platform):

    ret = []

    alpha_01 = slice(0,5)
    alpha_02 = slice(5,10)
    alpha_03 = slice(10,15)
    beta_01  = slice(15,20)

    for e in erd_ids[alpha_01]:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : "",
            'status' : "",
            'l1_jira' : "QTI9X28-4001",
            'l2_jira' : "QTI9X28-3001",
            'bug_jiras' :"",
            'platform' : platform,
            'workload' : "",
            'milestone' :"alpha-01",
            'F_casetree' : [],
        }
        ret.append(out)

    for e in erd_ids[alpha_02]:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : "",
            'status' : "",
            'l1_jira' : "QTI9X28-4002",
            'l2_jira' : "QTI9X28-3002",
            'bug_jiras' :"",
            'platform' : platform,
            'workload' : "",
            'milestone' :"alpha-02",
            'F_casetree' : [],
        }
        ret.append(out)


    for e in erd_ids[alpha_03]:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : "",
            'status' : "",
            'l1_jira' : "QTI9X28-4003",
            'l2_jira' : "QTI9X28-3003",
            'bug_jiras' :"",
            'platform' : platform,
            'workload' : "",
            'milestone' :"alpha-03",
            'F_casetree' : [],
        }
        ret.append(out)

    for e in erd_ids[beta_01]:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : "",
            'status' : "",
            'l1_jira' : "QTI9X28-4004",
            'l2_jira' : "QTI9X28-3004",
            'bug_jiras' :"",
            'platform' : platform,
            'workload' : "",
            'milestone' :"beta-01",
            'F_casetree' : [],
        }
        ret.append(out)

    return ret

# TODO 03
def show_time_second_from_jira(platform):

    ret = []

    alpha_01 = slice(0,5)
    alpha_02 = slice(5,10)
    alpha_03 = slice(10,15)
    beta_01  = slice(15,20)

    for e in erd_ids[alpha_01]:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "UNDO",
            'l1_jira' : "QTI9X28-4001",
            'l2_jira' : "QTI9X28-3001",
            'bug_jiras' : "QTI9X28-1000",
            'platform' : platform,
            'workload' : "2d",
            'milestone' :"alpha-01",
            'F_casetree' : [
                {
                    'case_name' : "test_case_01_alpha_01",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_02_alpha_01",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_03_alpha_01",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    return ret

# TODO 08
def show_time_third_from_jira(platform):

    ret = []

    alpha_01 = slice(0,5)
    alpha_02 = slice(5,10)
    alpha_03 = slice(10,15)
    beta_01  = slice(15,20)

    for e in erd_ids[alpha_02]:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4002",
            'l2_jira' : "QTI9X28-3002",
            'bug_jiras' : "QTI9X28-1002",
            'platform' : platform,
            'workload' : "4d",
            'milestone' :"alpha-02",
            'F_casetree' : [
                {
                    'case_name' : "test_case_01_alpha_02",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_02_alpha_02",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_03_alpha_02",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    return ret

# TODO 13
def show_time_fourth_from_jira(platform):

    ret = []

    alpha_01 = slice(0,5)
    alpha_02 = slice(5,10)
    alpha_03 = slice(10,15)
    beta_01  = slice(15,20)

    for e in erd_ids[alpha_03]:
        out = {}
        out['PLATFORM'] = platform
        out['ERD_ID'] = e
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : "DONE",
            'l1_jira' : "QTI9X28-4003",
            'l2_jira' : "QTI9X28-3003",
            'bug_jiras' : "QTI9X28-1003",
            'platform' : platform,
            'workload' : "2d",
            'milestone' :"alpha-03",
            'F_casetree' : [
                {
                    'case_name' : "test_case_01_alpha_03",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_02_alpha_03",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
                {
                    'case_name' : "test_case_03_alpha_03",
                    'case_age' : "2018-11-25",
                    'F_report_path' : random.choice(report_path),
                },
            ],
        }
        ret.append(out)

    return ret
# def show_time_third_from_jira(platform):

#     ret = []

#     alpha_01 = slice(0,5)
#     alpha_02 = slice(5,10)
#     alpha_03 = slice(10,15)
#     beta_01  = slice(15,20)

#     for e in erd_ids[alpha_01]:
#         out = {}
#         out['PLATFORM'] = platform
#         out['ERD_ID'] = e
#         out['jira'] = {
#             'HLD' : random.choice(HLD),
#             'status' : "UNDO",
#             'l1_jira' : "QTI9X28-4001",
#             'l2_jira' : "QTI9X28-3001",
#             'bug_jiras' : "QTI9X28-1000",
#             'platform' : platform,
#             'workload' : "2d",
#             'milestone' :"alpha-01",
#             'F_casetree' : [
#                 {
#                     'case_name' : "test_case_01_alpha_01",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#                 {
#                     'case_name' : "test_case_02_alpha_01",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#                 {
#                     'case_name' : "test_case_03_alpha_01",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#             ],
#         }
#         ret.append(out)

#     for e in erd_ids[alpha_02]:
#         out = {}
#         out['PLATFORM'] = platform
#         out['ERD_ID'] = e
#         out['jira'] = {
#             'HLD' : random.choice(HLD),
#             'status' : "DONE",
#             'l1_jira' : "QTI9X28-4002",
#             'l2_jira' : "QTI9X28-3002",
#             'bug_jiras' : "QTI9X28-1002",
#             'platform' : platform,
#             'workload' : "4d",
#             'milestone' :"alpha-02",
#             'F_casetree' : [
#                 {
#                     'case_name' : "test_case_01_alpha_02",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#                 {
#                     'case_name' : "test_case_02_alpha_02",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#                 {
#                     'case_name' : "test_case_03_alpha_02",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#             ],
#         }
#         ret.append(out)


#     for e in erd_ids[alpha_03]:
#         out = {}
#         out['PLATFORM'] = platform
#         out['ERD_ID'] = e
#         out['jira'] = {
#             'HLD' : random.choice(HLD),
#             'status' : "DONE",
#             'l1_jira' : "QTI9X28-4003",
#             'l2_jira' : "QTI9X28-3003",
#             'bug_jiras' : "QTI9X28-1003",
#             'platform' : platform,
#             'workload' : "2d",
#             'milestone' :"alpha-03",
#             'F_casetree' : [
#                 {
#                     'case_name' : "test_case_01_alpha_03",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#                 {
#                     'case_name' : "test_case_02_alpha_03",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#                 {
#                     'case_name' : "test_case_03_alpha_03",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#             ],
#         }
#         ret.append(out)

#     for e in erd_ids[beta_01]:
#         out = {}
#         out['PLATFORM'] = platform
#         out['ERD_ID'] = e
#         out['jira'] = {
#             'HLD' : random.choice(HLD),
#             'status' : "DONE",
#             'l1_jira' : "QTI9X28-4004",
#             'l2_jira' : "QTI9X28-3004",
#             'bug_jiras' : "QTI9X28-1004",
#             'platform' : platform,
#             'workload' : "3w",
#             'milestone' :"beta-01",
#             'F_casetree' : [
#                 {
#                     'case_name' : "test_case_01_beta_01",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#                 {
#                     'case_name' : "test_case_02_beta_01",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#                 {
#                     'case_name' : "test_case_03_beta_01",
#                     'case_age' : "2018-11-25",
#                     'F_report_path' : random.choice(report_path),
#                 },
#             ],
#         }
#         ret.append(out)

#     return ret



def random_gen_cookies():
    """
    out_cookies = [{
                    'ERD_ID'  : "",
                    'excel'   : {},
                    'jira'    : {},
                    'jenkins' : {},
                    'UIform'  : {}},
                    ...]
    """

    out_cookies = []

    for e in erd_ids:
        out = {}
        out['ERD_ID'] = e
        out['excel'] = {
            'erd_id' : e,
            'category' : random.choice(category),
            'title' : random.choice(title),
            'description' : random.choice(description),
            'product_priority' : random.choice(product_priority),
            'author' : random.choice(author),
            'version' : random.choice(version),
            'platform' : random.choice(platform),
        }
        out['jira'] = {
            'HLD' : random.choice(HLD),
            'status' : random.choice(status),
            'l1_jira' : random.choice(l1_jira),
            'l2_jira' : random.choice(l2_jira),
            'bug_jiras' : random.choice(bug_jiras),
            'platform' : random.choice(platform),
            'workload' : random.choice(workload),

            'F_casetree' : [
                {
                    'case_name' : "ACIS_A_S_Test_Temp_Volt",
                    'case_age' : random.choice(case_age),
                    'F_report_path' : ','.join(report_path),
                },
                {
                    'case_name' : "ACIS_A_S_Test_Temp_ssss",
                    'case_age' : random.choice(case_age),
                    'F_report_path' : ','.join(report_path),
                },
                {
                    'case_name' : "ACIS_A_S_Test_Temp_abcd",
                    'case_age' : random.choice(case_age),
                    'F_report_path' : ','.join(report_path),
                },
            ],
        }
        out['jenkins'] = {
            # casename : {}
            'ACIS_A_S_Test_Temp_Volt' : {
                'fw_version' : random.choice(fw_version),
                'test_result' : random.choice(test_result),
                'test_log' : random.choice(test_log),
                'test_date' : random.choice(test_date),
                'IR_report_path' : random.choice(report_path)
                },
            'ACIS_A_S_Test_Temp_ssss' : {
                'fw_version' : random.choice(fw_version),
                'test_result' : random.choice(test_result),
                'test_log' : random.choice(test_log),
                'test_date' : random.choice(test_date),
                'IR_report_path' : random.choice(report_path)
            },
            'ACIS_A_S_Test_Temp_abcd' : {
                'fw_version' : random.choice(fw_version),
                'test_result' : random.choice(test_result),
                'test_log' : random.choice(test_log),
                'test_date' : random.choice(test_date),
                'IR_report_path' : random.choice(report_path)
            }
        }
        out['UIform'] = {
            'UItest' : "I Love This Game.",
        }
        out_cookies.append(out)

    return out_cookies

