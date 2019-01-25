from jira import JIRA
from configparser import ConfigParser


test_evidence_field_name = "Environment"


platform_to_jira_project_maps = {
    "AR759X": "FW 9x40",
    "AR758X": "FW 9x28"
}


def get_jira_field_name_map(jira_object):
    # Fetch all fields
    all_fields = jira_object.fields()

    # make a map from field name -> field id
    name_map = {field['name']: field['id'] for field in all_fields}
    return name_map


def get_all_new_feature_jiras(jira_object, project, max_result_buf=2000):
    '''
    >>>[
    >>>jira_ticket1, jira_tcket2 ...
    >>>]
    '''
    new_feature_jiras = []
    new_features = jira_object.search_issues("project='" + project + "' and type='New Feature'", maxResults=max_result_buf)
    for new_feature in new_features:
        new_feature_jiras.append(new_feature.key)
    return new_feature_jiras


def retrieve_jira_erd_id(jira_issue_object, name_map):
    return getattr(jira_issue_object.fields, name_map['Requirement ID'])


def retrieve_jira_status(jira_issue_object, name_map):
    status = getattr(jira_issue_object.fields, name_map['Status'])
    return status.name


def retrieve_linked_issues(jira_issue_object, name_map):
    linked_jira_tickets = []
    for linked_issue in getattr(jira_issue_object.fields, name_map['Linked Issues']):
        if "outwardIssue" in dir(linked_issue):
            linked_jira_tickets.append(linked_issue.outwardIssue.key)
        elif "inwardIssue" in dir(linked_issue):
            linked_jira_tickets.append(linked_issue.inwardIssue.key)
        else:
            raise Exception("Linked issue can't processed")
    return linked_jira_tickets


def retrieve_jira_workload(jira_issue_object, name_map):
    seconds = getattr(jira_issue_object.fields, name_map['Original Estimate'])
    if not seconds:
        hours = 0
    else:
        minutes = seconds/60
        if minutes >= 60:
            return str(minutes/60) + "hours"
        else:
            return str(minutes) + "minutes"


def retrieve_jira_milestone(jira_issue_object, name_map):
    fix_version = getattr(jira_issue_object.fields, name_map['Fix Version/s'])
    if not fix_version:
        return ''
    else:
        return fix_version[0].name


def retrive_jira_test_evidence(jira_issue_object, name_map):
    return getattr(jira_issue_object.fields, name_map["Test Evidence/s"])


def retrieve_jira_test_case_info(test_evidence):
    F_case_tree = []
    parser = ConfigParser(allow_no_value=True)
    parser.read_string(test_evidence)
    test_cases_string = parser.get("ACIS RETRIEVE", "TestCases")
    test_cases = test_cases_string.split(",")
    for test_case in test_cases:
        test_case_info = {}
        test_case_info["case_name"] = test_case.strip()
        test_case_info["F_report_path"] = parser.get("ACIS RETRIEVE", test_case.strip())
        test_case_info["case_age"] = "" # still don't know how to use it.
        F_case_tree.append(test_case_info)
    return F_case_tree


def retrieve_hld(test_evidence):
    parser = ConfigParser(allow_no_value=True)
    parser.read_string(test_evidence)
    return parser.get("ACIS RETRIEVE", "HLD")


jira_field_retrieve_func_map ={
    "status": retrieve_jira_status,
    "workload": retrieve_jira_workload,
    "milestone": retrieve_jira_milestone,
    "bug_jiras": retrieve_linked_issues,
}

def jira_ticket_data(platform, jira_object, jiras):
    '''
    >>> [
       >>> ...
       >>> {
       >>>   "PLATFORM" : "",
       >>>   "ERD_ID" : "",
       >>>   "jira" : {
       >>>     'HLD' : "",
       >>>     'status' : "",
       >>>     'l1_jira' : "", # seems no use, all are ""
       >>>     'l2_jira' : "",
       >>>     'bug_jiras' : "",
       >>>     'platform' : "",
       >>>     'workload' : "",
       >>>     'milestone' : "",
       >>>     'F_casetree' : [
       >>>                 ...
       >>>                 {
       >>>                     'case_name' : "",
       >>>                     'case_age' : "", # don't know how to define it, all are ""
       >>>                     'F_report_path': "",
       >>>                 },
       >>>                 ... ]
       >>>     }
       >>> ...
       >>> ]
    '''
    all_jira_tickets = []
    jira_field_name_map = get_jira_field_name_map(jira_object)

    for jira in jiras:
        print(jira)
        jira_ticket_full_info = {}
        jira_ticket_info = {}
        jira_ticket_object = jira_object.issue(jira)

        for key, value in jira_field_retrieve_func_map.items():
            jira_ticket_info[key] = value(jira_ticket_object, jira_field_name_map)

        jira_ticket_full_info["PLATFORM"] = platform
        jira_ticket_full_info["ERD_ID"] = retrieve_jira_erd_id(jira_ticket_object, jira_field_name_map)
        jira_ticket_info["l1_jira"] = "" # seems useless
        jira_ticket_info["l2_jira"] = jira
        jira_ticket_info["platform"] = platform

        # This part is get from "Test Evidence/s" field
        test_evidence = retrive_jira_test_evidence(jira_ticket_object, jira_field_name_map)
        if not test_evidence:
            jira_ticket_info["HLD"] = ""
            jira_ticket_info["F_casetree"] = []
        else:
            jira_ticket_info["HLD"] = retrieve_hld(test_evidence)
            jira_ticket_info["F_casetree"] = retrieve_jira_test_case_info(test_evidence)

        jira_ticket_full_info["jira"] = jira_ticket_info
        all_jira_tickets.append(jira_ticket_full_info)

    return all_jira_tickets


def retrieve_new_feature_jiras(jira_addr, user, passwd, platform):
    jira_login = JIRA(jira_addr, basic_auth=(user, passwd))
    all_new_feature_jiras = get_all_new_feature_jiras(jira_login, platform_to_jira_project_maps[platform])
    return jira_ticket_data(platform, jira_login, all_new_feature_jiras)
