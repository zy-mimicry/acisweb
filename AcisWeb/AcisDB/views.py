#! /usr/bin/env python3
# coding=utf-8

"""
"""

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound
import json,time,threading,copy,os,re
from pprint import pprint as pp, pformat

from . import log
from . import vcore

from .vcore_interface import (IntegrationExtractor,
                              DefaultExtractor,
                              ExcelProvider,
                              JiraProvider,
                              JenkinsProvider,
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

def query_new(request):
    return render(request, 'LigerUI/ACIS/query_new.htm', {})

def query_new_switch(request):
    if request.method == "GET":
        platform = request.GET.get('platform')
        action = request.GET.get('action')

        def integration_test_get_cookies(query_cookies):
            UIout = []
            out = {}

            ERDs = query_cookies['Erds']
            for erd_id in ERDs:
                for casename in ERDs[erd_id]:
                    out['erd_id'] = erd_id
                    out['platform']  = query_cookies['platform']
                    out['case_name'] = casename
                    out['fw_version'] = ERDs[erd_id][casename]['fw_version']
                    out['test_date']  = ERDs[erd_id][casename]['test_date']
                    out['test_result']= ERDs[erd_id][casename]['test_result']
                    out['IR_report_path'] = ERDs[erd_id][casename]['IR_report_path']
                    UIout.append(out)
                    out = {}

            return UIout

        if action == 'integration_version':
            fw_version = request.GET.get('FirmwareVersion')
            test_date = request.GET.get('test_date')
            q = vcore.Query('integration_query_exactly', platform=platform, fw_version=fw_version, test_date=test_date)
            UI_date = integration_test_get_cookies(q.do_query())
            return render(request, 'LigerUI/ACIS/integration_page.htm', {'cookies' : json.dumps(UI_date)})

        if action == 'date_of_night':
            date_of_night = request.GET.get('date_of_night')
            q = vcore.Query('night_regression_query', platform=platform, test_date=date_of_night)
            UI_date =  integration_test_get_cookies(q.do_query())
            return render(request, 'LigerUI/ACIS/integration_page.htm', {'cookies' : json.dumps(UI_date)})

        if action == 'ERD':
            ERD_ID = request.GET.get('ERD_ID')
            return render(request, 'LigerUI/ACIS/special_query_page.htm', {})

        if action == 'case_name':
            casename = request.GET.get('case_name')
            return render(request, 'LigerUI/ACIS/special_query_page.htm', {})

        else:
            return HttpResponseNotFound("<h2> Please input 'platform' and 'action' togather.</h2>")


def do_save_excel(platform, version, erd_excel_file):
    vcore.splitter('save', provider=ExcelProvider(platform, version, erd_excel_file))


def do_save_jira(platform, jira_server_addr, jira_user, jira_passwd):
    vcore.splitter('save', provider=JiraProvider(platform, jira_server_addr, jira_user, jira_passwd))


def do_save_jenkins(platform, test_report_file):
    vcore.splitter('save', provider=JenkinsProvider(platform, test_report_file))

supported_cmds = {
    'save_excel_data'  : do_save_excel,
    'save_jira_data'   : do_save_jira,
    'save_jenkins_data': do_save_jenkins,
}

def commands(request):
    return render(request, 'LigerUI/ACIS/commands.htm', {'cmds' : list(supported_cmds.keys())})

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
