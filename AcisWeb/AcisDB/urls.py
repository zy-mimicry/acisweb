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
from .shwu_debug import views_of_shw

app_name = 'AcisDB'

urlpatterns = [
    path('', views.index, name = 'index'),

    path('9X28_default_index/', views.ERD_9X28_index, name = "ERD_9X28_index"),
    path('9X40_default_index/', views.ERD_9X40_index, name = "ERD_9X40_index"),
    path('SD55_default_index/', views.ERD_SD55_index, name = "ERD_SD55_index"),

    path('columns_data_select/', views.columns_data_select, name = 'columns_data_select'),

    path('commands/', views.commands, name = "commands"),
    path('help/',     views.help,     name = "help"),
    path('about/',    views.about,    name = "about"),

    path('query/',    views.query,    name = "query"),
    path('query/switch/', views.query_switch,  name = "switch"),

    path('query_new/',    views.query_new,    name = "query_new"),
    path('query_new/switch/',    views.query_new_switch,    name = "query_new"),

    path('actions/', views.actions_dispatcher,   name = "actions"),

    path('jenkins_handler/', views.jenkins_handler, name = "jenkins_handler"),

    # >Debug Page of rex<
    path('rex_home/',     views_of_rex.rex_home,     name = 'rex_home'),
    path('rex_commands/', views_of_rex.rex_commands, name = 'rex_commands'),
    path('rex_prompt/', views_of_rex.rex_prompt, name = 'rex_prompt'),

    path('test_query/', views_of_rex.rex_test_query, name = 'query_test'),

    path('rex_actions/',  views_of_rex.rex_actions_dispatcher,   name = 'rex_actions'),
    path('rex_show_actions/',  views_of_rex.rex_show_actions_dispatcher,   name = 'rex_show_actions'),

    # >Debug Page of shwu<
    path('shw_home/',     views_of_shw.shw_home, name = 'shw_home'),
]
