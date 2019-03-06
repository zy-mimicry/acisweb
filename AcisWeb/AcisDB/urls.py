"""AcisWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

from .rex_debug import views_of_rex

app_name = 'AcisDB'

urlpatterns = [
    path('', views.index, name = 'index'),

    path('9X28_default_index/', views.ERD_9X28_index, name = "ERD_9X28_index"),
    path('9X40_default_index/', views.ERD_9X40_index, name = "ERD_9X40_index"),
    path('SDX55_default_index/', views.ERD_SDX55_index, name = "ERD_SDX55_index"),

    path('columns_data_select/', views.columns_data_select, name = 'columns_data_select'),
    path('actions/', views.actions_dispatcher, name = "actions"),

    path('commands/', views.commands, name = "commands"),
    path('help/', views.help, name = "help"),
    path('about/', views.about, name = "about"),

    path('query/', views.query, name = "query"),
    path('query/switch/', views.query_switch, name = "switch"),

    path('jenkins_handler/', views.jenkins_handler, name = "jenkins_handler"),

    path('campaign/', views.campaign, name = "latest_campaign"),
    path('campaign_index/', views.campaign_index, name = "campaign_index"),
    path('campaign_query/', views.campaign_query, name = "campaign_query"),

    path('snapshot/', views.snapshot, name = "latest_snapshot"),
    path('snapshot_index/', views.snapshot_index, name = "snapshot_index"),
    path('snapshot_query/', views.snapshot_query, name = "snapshot_query"),
    path('snapshot_store/', views.snapshot_store, name = "snapshot_store"),

    path('special_note/', views.special_note, name = "special_note"),
    path('bug_effectiveness_chart/', views.bug_effectiveness_chart, name = "bug_effectiveness_chart"),

    path('device_manage/', views.device_manage, name = "device_manage"),
    path('device_manage/device_static_info_query/', views.device_static_info_query, name = "device_static_info_query"),
    path('device_static_info_update/', views.device_static_info_update, name = "device_static_info_update"),
    path('slave_details/', views.slave_details, name = "slave_details")
    # debug
    path('rex_show_actions/', views_of_rex.rex_show_actions_dispatcher, name = "rex_debug"),
    path('rex_prompt/', views_of_rex.rex_prompt, name = "rex_prompt"),
]
