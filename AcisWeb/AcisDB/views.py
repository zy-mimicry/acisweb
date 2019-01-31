#! /usr/bin/env python3
# coding=utf-8

"""
"""

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import json,time,threading,copy,os,re,pickle
from pprint import pprint as pp, pformat

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
    pp(type(out))
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


def help(request):
    return render(request, 'LigerUI/ACIS/help.htm', {})


def about(request):
    return render(request, 'LigerUI/ACIS/about.htm', {})


def query(request):
    return render(request, 'LigerUI/ACIS/query.htm', {})


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

            return render(request, 'LigerUI/ACIS/ERD_page.htm', {'cookies' : json.dumps(out)})

        elif action == 'integration_version':
            fw_version = request.GET.get('FirmwareVersion')
            ie = IntegrationExtractor([platform],fw_version = fw_version)
            vcore.splitter('pick_all', extractor = ie )

            return render(request, 'LigerUI/ACIS/integration_page.htm', {'cookies' : json.dumps(ie.UI_data)})

        else:
            return HttpResponseNotFound("<h2> Please input 'platform' and 'action' togather.</h2>")

    elif request.method == "POST":
        print("POST request, but do nothing.")


def test_report_query_enter(request):
    return render(request, 'LigerUI/ACIS/test_report_query.htm', {})


def test_report_query(request):
    if request.method == "GET":
        platform = request.GET.get('platform')
        action = request.GET.get('action')

        if action == 'test_report_query':
            fw_version = request.GET.get('FirmwareVersion')
            start_test_date = request.GET.get('start_test_date')
            end_test_date = request.GET.get('end_test_date')
            q = vcore.Query('test_report_query', platform=platform, fw_version=fw_version,
                            start_test_date=start_test_date, end_test_date=end_test_date)
        elif action == 'ERD':
            ERD_ID = request.GET.get('ERD_ID')
            q = vcore.Query("ERD_caselist_query",  platform=platform, ERD_ID=ERD_ID)
        elif action == 'case_name':
            casename = request.GET.get('case_name')
            q = vcore.Query("casename_query",  platform=platform, casename=casename)
        else:
            return HttpResponseNotFound("<h2> Please input 'platform' and 'action' togather.</h2>")

        UI_data = q.test_report_data()
        return render(request, 'LigerUI/ACIS/integration_page.htm', {'cookies': json.dumps(UI_data)})


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
        if parameters['command'] == 'save_erd_data':
            do_save_excel(parameters['platform'], parameters['ErdVersion'], parameters['erd_excel_file'])
        elif parameters['command'] == 'save_jira_data':
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

    q = vcore.Query('test_report_query', platform=platform, fw_version=fw_version,
                    start_test_date=test_date, end_test_date=test_date)
    UI_date = q.test_report_data()

    return render(request, 'LigerUI/ACIS/integration_page.htm', {'cookies' : json.dumps(UI_date)})


def campaign_query(request):

    not_empty_args = {}

    # filter out emtpy args.
    for arg, value in request.GET.items():
        if value.strip():
            not_empty_args[arg] = value

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
    pp(request.GET)
    platform_list = request.GET['platform_list'].split(',')

    for platform in platform_list:
        platform = platform.upper()

        de = DefaultExtractor([platform])
        vcore.splitter('pick_all', extractor = de )
        out = de.ext_snapshot(platform)

        vcore.SnapshotDealer().pickling(platform, out)

    return HttpResponse("Picking <{}> view Done".format(platform_list))
