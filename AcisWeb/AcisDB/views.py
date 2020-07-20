#! /usr/bin/env python3
# coding=utf-8

"""
"""

from django.shortcuts import render,render_to_response
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import json,time,threading,copy,os,re,pickle
from pprint import pprint as pp, pformat
from operator import itemgetter
from itertools import groupby
from pyecharts import Bar
from collections import defaultdict,OrderedDict
import math,random
from AcisDB.models import SubordinateStaticInfo,DutStaticInfo
import jenkins
from . import log
from . import vcore

from .vcore_interface import (IntegrationExtractor,
                              DefaultExtractor,
                              ExcelProvider,
                              JiraProvider,
                              AutoJenkinsProvider)

import logging
mlogger = logging.getLogger(__name__).info


def index(request):
    return render(request, 'LigerUI/main.htm', {})


def ERD_9X28_index(request):

    de = DefaultExtractor(['9X28'])
    vcore.splitter('pick_all', extractor = de )
    out = de.ext_snapshot('9X28')
    return render(request, 'LigerUI/ACIS/ERD_page.htm', {'cookies' : json.dumps(out)})


def ERD_9X40_index(request):

    de = DefaultExtractor(['9X40'])
    vcore.splitter('pick_all', extractor = de )
    out = de.ext_snapshot('9X40')
    return render(request, 'LigerUI/ACIS/ERD_page.htm', {'cookies' : json.dumps(out)})


def ERD_SDX55_index(request):

    de = DefaultExtractor(['SD55'])
    vcore.splitter('pick_all', extractor = de )
    out = de.ext_snapshot('SD55')
    return render(request, 'LigerUI/ACIS/ERD_page.htm', {'cookies' : json.dumps(out)})


def columns_data_select(request):
    return render(request, 'LigerUI/ACIS/columns_data_select.htm')


def query(request):
    return render(request, 'LigerUI/ACIS/query.htm', {})


def query_switch(request):
    if request.method == "GET":
        # if platform not pass, throw exception.
        if 'hostname' in request.GET:
            hostname = request.GET['hostname']
            mac_addr = request.GET['mac_addr']
            dut_fsn = request.GET['FSN']

            thl = vcore.TestHistoryDealer().query(hostname=hostname, subordinate_mac_addr=mac_addr, FSN=dut_fsn)
            return render(request, 'LigerUI/ACIS/test_history.htm', {'test_history_list' : thl})

        platform = request.GET.get('platform').upper()

        if not ({'platform', 'FirmwareVersion','start_test_date', 'end_test_date'} - set(request.GET.keys())):
            fw_version = request.GET.get('FirmwareVersion')
            start_test_date = request.GET.get('start_test_date')
            end_test_date = request.GET.get('end_test_date')
            UI_data = vcore.TestReportQuery('test_report_query', platform=platform,
                                      fw_version=fw_version,
                                      start_test_date=start_test_date,
                                      end_test_date=end_test_date).test_report_data()
            return render(request, 'LigerUI/ACIS/integration_page.htm', {'cookies': json.dumps(UI_data)})

        elif not ({'ErdTableVersion'} - set(request.GET.keys())):
            erd_table_version = request.GET.get('ErdTableVersion')
            de = DefaultExtractor([platform])
            vcore.splitter('pick_all', extractor = de )
            out = de.ext_snapshot(platform = platform.upper(), spec_ver = erd_table_version)
            return render(request, 'LigerUI/ACIS/ERD_page.htm', {'cookies' : json.dumps(out)})

        elif not ({'ERD_ID'} - set(request.GET.keys())):
            ERD_ID = request.GET.get('ERD_ID')
            UI_data = vcore.TestReportQuery("ERD_caselist_query",
                                            platform=platform,
                                            ERD_ID=ERD_ID).test_report_data()
            return render(request, 'LigerUI/ACIS/integration_page.htm', {'cookies': json.dumps(UI_data)})

        elif not ({'case_name'} - set(request.GET.keys())):
            casename = request.GET.get('case_name')
            UI_data = vcore.TestReportQuery("casename_query",
                                            platform=platform,
                                            casename=casename).test_report_data()
            return render(request, 'LigerUI/ACIS/integration_page.htm', {'cookies': json.dumps(UI_data)})

        else:
            return HttpResponseNotFound("<h2> Please input valid information in form.</h2>")

    elif request.method == "POST":
        print("POST request, but do nothing.")


def do_save_excel(platform, version, erd_excel_file):
    vcore.splitter('save', provider=ExcelProvider(platform, version, erd_excel_file))


def do_save_jira(platform, jira_server_addr, jira_user, jira_passwd):
    vcore.splitter('save', provider=JiraProvider(platform, jira_server_addr, jira_user, jira_passwd))


def commands(request):
    return render(request, 'LigerUI/ACIS/commands.htm')


def actions_dispatcher(request):
    if request.method == 'GET':
        parameters = request.GET
    elif request.method == 'POST':
        parameters = request.POST

    if parameters:
        if 'erd_excel_file' in parameters:
            do_save_excel(parameters['platform'], parameters['ErdVersion'], parameters['erd_excel_file'])
        elif 'jira_address' in parameters:
            do_save_jira(parameters['platform'],
                         parameters['jira_address'],
                         parameters['jira_user'],
                         parameters['jira_passwd'])
    return HttpResponseRedirect("/commands/")


def jenkins_handler(request):

    # curl --get -d "result_path=/home/rex/nfs_acis/Integration_Test/log_and_report/platform/diff/" http://127.0.0.1:8000/jenkins_handler/
    if request.method == "GET":
        pp(AutoJenkinsProvider(request.GET['result_path']).get_data())
        vcore.splitter('save',  provider = AutoJenkinsProvider(request.GET['result_path']))
        return HttpResponse("[JENKINS DATA] Merge Done ({})\n".format(request.GET['result_path']))

    return HttpResponseNotFound("[JENKINS DATA] Merge ERROR, NOT GET request or other error.")

def campaign(request):
    latest_list = vcore.TestCampaignDealer().get_latest()
    return render(request, 'LigerUI/ACIS/latest_campaign.htm', {'latest_list' : latest_list})


def campaign_index(request):

    platform    = request.GET['platform']
    fw_version  = request.GET['fw_version']
    test_date   = request.GET['test_date']
    description = request.GET['description']

    q = vcore.TestReportQuery('test_report_query', platform=platform, fw_version=fw_version,
                              start_test_date=test_date, end_test_date=test_date)
    UI_date = q.test_report_data()

    return render(request, 'LigerUI/ACIS/integration_page.htm', {'cookies' : json.dumps(UI_date)})


def campaign_query(request):

    # filter out emtpy args.
    not_empty_args = { arg: value for arg, value in request.GET.items() if value.strip()}

    if 'id' in not_empty_args:
        query_result_list = [vcore.TestCampaignDealer().query_by_id(**not_empty_args)]
    else:
        query_result_list = vcore.TestCampaignDealer().query(**not_empty_args)

    return render(request, 'LigerUI/ACIS/latest_campaign.htm', {'latest_list' : query_result_list})


def snapshot(request):
    latest_list = vcore.SnapshotDealer().get_latest()
    return render(request, 'LigerUI/ACIS/latest_snapshot.htm', {'latest_list' : latest_list})


def snapshot_index(request):
    date = request.GET['date']
    tag  = request.GET['tag']

    out = vcore.SnapshotDealer().unpickling(date)

    return render(request, 'LigerUI/ACIS/ERD_page.htm', {'cookies' : json.dumps(out)})


def snapshot_query(request):
    not_empty_args = {}

    for arg, value in request.GET.items():
        if value.strip():
            not_empty_args[arg] = value

    query_result_list = vcore.SnapshotDealer().query(**not_empty_args)

    return render(request, 'LigerUI/ACIS/latest_snapshot.htm', {'latest_list' : query_result_list})


def snapshot_store(request):
    """
    curl --get -d "platform_list=SD55,9x28,9x40" 127.0.0.1:8000/snapshot_store/
    """
    platform_list = request.GET['platform_list'].split(',')

    for platform in platform_list:
        platform = platform.upper()

        de = DefaultExtractor([platform])
        vcore.splitter('pick_all', extractor = de )
        out = de.ext_snapshot(platform)

        vcore.SnapshotDealer().pickling(platform, out)

    return HttpResponse("Picking <{}> view Done".format(platform_list))


def special_note(request):

    note = request.GET['note']
    q = vcore.TestReportQuery('pick_note',
                              platform = request.GET['platform'],
                              ERD_ID = request.GET['ERD_ID'],
                              case_name = request.GET['case_name'],
                              fw_version = request.GET['fw_version'],
                              test_date = request.GET['test_date'])
    note_obj = q.pick_note_obj()
    note_obj.note = note
    note_obj.save()
    return HttpResponse('#')


# We will download the pyecharts static library to the local,
# if you need to update, please go to the official website to view.
# ref: "https://pyecharts.github.io/assets/js".

# REMOTE_HOST = "https://pyecharts.github.io/assets/js" << Online temporary usage.
REMOTE_HOST = "../../LigerUI/ACIS/static/pyecharts-js"


def bug_effectiveness_chart(request):
    template = loader.get_template('LigerUI/ACIS/bug_effectiveness_chart.htm')

    platform_list = ['9X40'] # here should be modified later.
    cursor_list, trs_of_platform = pick_all_test_campaign(platform_list)
    bar_dict = {}

    for platform in platform_list:
        bar_c = BSC_generator_baseon_campaign(platform, trs_of_platform, cursor_list)
        bar_d = BSC_generator_baseon_day(platform, trs_of_platform, cursor_list)
        bar_dict[platform] = [bar_c, bar_d]

    bar_dict_rendered = {}
    for p, bar_obj_list in bar_dict.items():
        _l = []
        for bar_obj in bar_obj_list:
            _l.append(bar_obj.render_embed())
        bar_dict_rendered[p] = _l

    context = dict(
        bar_dict_rendered = bar_dict_rendered,
        host = REMOTE_HOST,
        script_list = bar_dict[random.choice(platform_list)][0].get_js_dependencies()
    )

    return HttpResponse(template.render(context, request))


def pick_all_test_campaign(platform_list):

    trs_of_platform = {}
    test_campaign_array = {}

    # 'test_campaign_name' used by sort of test campaign, so don't modify the format.
    # <ref: [TAG: t-camp]>
    test_campaign_name = "<{platform} {fw_version} {description} {test_date}>"

    # Standard dictionaries are unordered, and cursor can be indexed sequentially.
    from collections import defaultdict
    cursor_list = defaultdict(list)

    for platform in platform_list:
        q = vcore.TestReportQuery('test_report_query',
                                  platform=platform,
                                  fw_version="",
                                  start_test_date="",
                                  end_test_date="")

        unused = q.test_report_data() # improvement here.
        trs_of_platform[platform] = {}

        # Each TestCampaign's test_date should be unique. So we groupby it.
        q.test_report_objs.sort(key = lambda tr : tr.test_date)
        for test_date, grp in groupby(q.test_report_objs, key=lambda tr : tr.test_date):

            #'itertools._grouper' object is not subscriptable, so convert to 'list'.
            list_out = list_grp = list(grp)

            # When different TestCampaigns's test_date are the same.(Probability is almost non-existent.)
            # Each 'description' should be used.
            if not all_same_desc(list_grp):
                list_grp.sort(key = lambda tr: tr.description)
                for desc, grp_d in groupby(list_grp, key=lambda tr: tr.description):
                    list_out = list(grp_d)

                    combin_str = test_campaign_name.format(
                        platform = platform,
                        fw_version = list_out[0].fw_version,
                        description = desc,
                        test_date = test_date,)
                    cursor_list[platform].append(combin_str)
                    trs_of_platform[platform][combin_str] = list_out
            else:
                combin_str = test_campaign_name.format(
                    platform = platform,
                    fw_version = list_out[0].fw_version,
                    description = list_out[0].description,
                    test_date = test_date,)

                cursor_list[platform].append(combin_str)
                trs_of_platform[platform][combin_str] = list_out

    return (cursor_list, trs_of_platform)

def all_same_desc(list_grp):
    desc = list_grp[0].description
    for g in list_grp:
        if g.description != desc:
            return False
    return True


# 'Bar Stacked Chart' is abbreviated as BSC
def BSC_generator_baseon_day(platform, trs, cursor):
    # The raw materials needed to generate the form.
    attr = list(); v1 = list(); v2 = list()
    bar = None

    # [TAG: t-camp] sort of test_date of test campaign.
    # test_date format : yyyy_mm_dd_HH_MM_SS
    cursor[platform].sort(key=lambda campaign: campaign[(campaign.rfind(' ') + 1) : -1])

    daily_test_campaign_dict = defaultdict(list)
    for campaign in cursor[platform]:
        test_date = campaign[(campaign.rfind(' ') + 1) : -1]
        daily_test_campaign_dict[test_date].append(campaign)

    for day, daily_test_list in daily_test_campaign_dict.items():
        attr.append(day)
        valid_counter   = 0
        invalid_counter = 0

        for campaign in daily_test_list:
            reports = trs[platform][campaign]

            for r in reports:
                if not r.note:
                    continue # ignore the null item.
                else:
                    if is_valid(r.note):
                        valid_counter += 1
                    else:
                        invalid_counter += 1

        v1.append(valid_counter)
        v2.append(invalid_counter)

    bar = BSC_format("Stack Chart base on each Day"
                     "<{}>".format(platform), attr, v1, v2)
    return bar


def BSC_generator_baseon_campaign(platform, trs, cursor):
    attr = list(); v1 = list(); v2 = list()
    bar = None

    for c in cursor[platform]:
        attr.append("{}".format(c))
        reports = trs[platform][c]

        valid_counter   = 0
        invalid_counter = 0

        for r in reports:
            if not r.note:
                continue # ignore the null item.
            else:
                if is_valid(r.note):
                    valid_counter += 1
                else:
                    invalid_counter += 1

        v1.append(valid_counter)
        v2.append(invalid_counter)

    bar = BSC_format("Stack Chart base on each TestCampaign"
                     "<{}>".format(platform), attr, v1, v2)
    return bar

def is_note_format(note):
    hit = re.match(r'\s*bug\s*:\s*\[(.*?)\]\s*brief\s*:\s*\[(.*?)\]\s*is_valid\s*:\s*\[(.*?)\]\s*', note, re.I)
    return True if hit else False

def is_valid(note):
    note = note.strip()
    if is_note_format(note):
        valid = re.match(r'.*is_valid\s*:\s*\[\s*(.*)\s*\]', note, re.I).group(1)
        return True if valid.lower() == 'true' else False
    else:
        # If you didn't fill in the form according to the format,
        # then can NOT say that there is a problem with the system,
        # we hope to mark it as 'valid'.
        return True

def BSC_format(title, attr, v1, v2):

    bar = Bar(title,
              width=800, height=450,
              extra_html_text_label=["<span style='font-size:12px;background-color:#D13232;'>"
                                     "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>&nbsp;[valid] <br />"
                                     "<span style='font-size:12px;background-color:#0B4C5F;'>"
                                     "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>&nbsp;[invalid]"])

    bar.add("", attr, v1,
            is_stack=True,
            is_label_show=True,
            is_datazoom_show=True,
            xaxis_interval=0,
            xaxis_rotate=15,
            yaxis_rotate=15,)

    bar.add("", attr, v2,
            is_stack=True,
            is_label_show=True,
            is_datazoom_show=True,
            xaxis_interval=0,
            xaxis_rotate=15,
            yaxis_rotate=15,)
    return bar


def subordinate_static_info_query(action):
    subordinates = vcore.DeviceStaticInfoManager("subordinate_static_info")
    if action == "all_removed_subordinates_manage":
        subordinates_info = subordinates.get_removed_subordinates()
    elif action == "all_available_subordinates_manage":
        subordinates_info = subordinates.get_available_subordinates()
    return subordinates_info


def dut_static_info_query(action):
    duts = vcore.DeviceStaticInfoManager("dut_static_info")
    if action == "all_removed_duts_manage":
        duts_info = duts.get_removed_subordinates()
    elif action == "all_available_duts_manage":
        duts_info = duts.get_available_subordinates()
    return duts_info


def device_static_info_query(request):
    action = request.GET.get("action")
    if action == "all_removed_subordinates_manage" or action == "all_available_subordinates_manage":
        subordinates_info = subordinate_static_info_query(action)
        return render(request, 'LigerUI/ACIS/subordinate_static_info.htm', {'cookies': json.dumps(subordinates_info)})
    elif action == "all_removed_duts_manage" or action == "all_available_duts_manage":
        duts_info = dut_static_info_query(action)
        return render(request, 'LigerUI/ACIS/dut_static_info.htm', {'cookies': json.dumps(duts_info)})
    else:
        raise Exception("Cannot Support This Query")


def device_static_info_update(request):
    # For subordinate, the "mac_addr" must be passed, so this field to distinguish subordinate or dut.
    if "mac_addr" in request.GET.keys():
        subordinate = vcore.DeviceStaticInfoManager("subordinate_static_info", request.GET)
        subordinate.update_info()
    else:
        subordinate = vcore.DeviceStaticInfoManager("dut_static_info", request.GET)
        subordinate.update_info()
    return HttpResponse('#')

def device_manage(request):
    return render(request, 'LigerUI/ACIS/device_manage.htm')


def get_all_valid_nodes():
    """
    Description
    process steps
    1. filter out all record that remove_status == False
    2. get all nodes from Jenkins that cantains 'online' and 'offline'
    3. previous two steps result in the intersection.
      a) in model, but NOT in Jenkins (drop)
      b) NOT in model, but in Jenkins (drop)
      c) both in model and Jenkins:
         c.1) Jenkins status offline ( show offline )
         c.2) Jenkins status online  ( show dynamic info )
    """
    ssil = SubordinateStaticInfo.objects.all().filter(remove_status = False)
    nodes_from_model = [ ssi.hostname for ssi in ssil ]

    server = jenkins.Jenkins('http://cnshz-ed-svr098:8080', username='acis', password='acis')
    subordinate_pi_nodes = server.get_nodes()
    nodes_from_jenkins = [ node['name'] for node in subordinate_pi_nodes ]
    nodes_intersection = set(nodes_from_model) & set(nodes_from_jenkins)

    nodes_with_status = []
    for index,subordinate_pi in enumerate(subordinate_pi_nodes):
        if subordinate_pi['name'] in nodes_intersection:
            nodes_with_status.append(subordinate_pi)

    return nodes_with_status


def subordinate_details(request):

    nodes = get_all_valid_nodes()
    info = {}

    subordinate_info_re = re.compile(r'\s*<subordinate info>\s*\[\s*(.*?)\s*\]\s*:\s*\[\s*(.*?)\s*\]\s*\[\s*(.*?)\s*\]')
    dut_info_re = re.compile(r'\s*<dut info>\s*\[\s*(.*?)\s*:\s*(.*?)\]\s*\[\s*(.*?)\s*:\s*(.*?)\s*\]\s*\[\s*(.*?)\s*:\s*(.*?)\s*\]')
    info_dir = '/home/rex/temp/Subordinate-Info/'

    for node in nodes:
        info[node['name']] = {}
        static_info = info[node['name']]['static'] = {}

        ssi = SubordinateStaticInfo.objects.get(hostname = node['name'])
        static_info['offline'] = node['offline']
        for name,value in ssi.__dict__.items():
            # Filter out the properties that are integrated by the parent class(model.Model).
            if name not in ('id', '_state'):
                static_info[name] = value

        static_info['DUTs'] = {}
        dsil = DutStaticInfo.objects.all().\
               filter(subordinate_mac_addr = ssi.mac_addr, remove_status = False)

        for dsi in dsil:
            _si = static_info['DUTs'][dsi.FSN] = {}
            for name,value in dsi.__dict__.items():
                if name not in ('id', '_state'):
                    _si[name] = value

        dynamic_info = info[node['name']]['dynamic'] = {}
        #info_dir = '/home/rex/nfs_acis/Subordinate-Info/'
        info_dir = '/home/rex/temp/Subordinate-Info/'
        latest = max(os.listdir(info_dir))
        node_file_names = os.listdir(info_dir + latest)

        if node['name'] not in node_file_names:
            dynamic_info['UNKONWN'] = "Dut to NOT auto-generate info file yet :("
        else:
            dynamic_info['DUTs'] = {}

            info_file = info_dir + latest + '/' + node['name'] +'/subordinate_info.log'
            with open(info_file, 'r') as f:
                for line in f:
                    g_of_subordinate = subordinate_info_re.match(line)
                    if g_of_subordinate:
                        # example: <subordinate info> [subordinate_root_space_total   ]: [status:0   ] [30G]
                        dynamic_info['subordinate_info_' + g_of_subordinate.group(1)] = g_of_subordinate.group(3)

                    g_of_dut = dut_info_re.match(line)
                    if g_of_dut:
                        # example: <dut info> [path: acis/DUT2/AT] [usb_serial: fdf5a6b3] [status: READY]
                        dut_name = g_of_dut.group(2).split('/')[1]
                        dynamic_info['DUTs'][dut_name] = {}
                        dynamic_info['DUTs'][dut_name]['dut_info_' + g_of_dut.group(1)] = g_of_dut.group(2)
                        dynamic_info['DUTs'][dut_name]['dut_info_' + g_of_dut.group(3)] = g_of_dut.group(4)
                        dynamic_info['DUTs'][dut_name]['dut_info_' + g_of_dut.group(5)] = g_of_dut.group(6)

    return render(request, 'LigerUI/ACIS/subordinate_details.htm', {'info' : info})

