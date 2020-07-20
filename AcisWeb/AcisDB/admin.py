from django.contrib import admin
from .models import (Erds,TestCases,TestReports,
                     TestCampaign,ProjectSnapshot,
                     SubordinateStaticInfo,DutStaticInfo,
                     TestHistory)

from reversion.admin import VersionAdmin

@admin.register(Erds)
class ErdsModelAdmin(VersionAdmin):
    list_display = ('platform','erd_id','version','l2_jira','bug_jiras')
    list_filter = ('platform','milestone','component','project')
    search_fields = ('erd_id','title','HLD','description','version',
                     'category','product_priority', 'author','l1_jira',
                     'l2_jira','bug_jiras','status', 'workload')
    ordering = ['platform', 'erd_id']


@admin.register(TestCases)
class TestCasesModelAdmin(VersionAdmin):
    list_display = ('case_name',)
    autocomplete_fields = ('erd',)
    search_fields = ['case_name']


@admin.register(TestReports)
class TestReportsModelAdmin(VersionAdmin):
    list_display = ('test_date', 'description', 'test_result', 'fw_version')
    list_filter = ('description','fw_version')
    search_fields = ['note','test_log','IR_report_path','test_date']
    autocomplete_fields = ('test_case',)


@admin.register(TestCampaign)
class TestCampaignModelAdmin(VersionAdmin):
    list_display = ('platform', 'test_date', 'description', 'fw_version')
    list_filter = ('platform',)
    search_fields = ['test_date', 'description', 'fw_version']
    ordering = ['test_date']


@admin.register(ProjectSnapshot)
class ProjectSnapshotModelAdmin(VersionAdmin):
    list_display = ('platform', 'date', 'tag')
    list_filter = ('platform',)
    search_fields = ['date', 'tag',]
    ordering = ['date']


@admin.register(SubordinateStaticInfo)
class SubordinateStaticInfoModelAdmin(VersionAdmin):
    list_display = ('hostname', 'birthday','img_version','mac_addr','owner','dead_date')
    list_filter = ('remove_status','owner')
    search_fields = ['hostname', 'birthday','img_version','mac_addr','dead_date']
    ordering = ['birthday']


@admin.register(DutStaticInfo)
class DutStaticInfoModelAdmin(VersionAdmin):
    list_display = ('FSN', 'usb_ser', 'birthday', 'owner', 'dead_date','subordinate_mac_addr')
    list_filter = ('remove_status', 'owner')
    search_fields = ['FSN', 'usb_ser', 'birthday', 'dead_date','subordinate_mac_addr']
    ordering = ['birthday']

@admin.register(TestHistory)
class TestHistoryModelAdmin(VersionAdmin):
    list_display = ('test_date_on_pi', 'hostname', 'FSN', 'case_name', 'test_result','subordinate_mac_addr')
    list_filter = ('hostname', 'FSN', 'case_name')
    search_fields = ['FSN', 'test_date_on_pi', 'test_result', 'subordinate_mac_addr']
    ordering = ['-test_date_on_pi']

