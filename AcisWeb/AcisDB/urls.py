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

app_name = 'AcisDB'

urlpatterns = [
    path('', views.index, name = 'index'),

    path('9X28_default_index/', views.ERD_9X28_index, name = "ERD_9X28_index"),
    path('9X40_default_index/', views.ERD_9X40_index, name = "ERD_9X40_index"),
    path('SDX55_default_index/', views.ERD_SDX55_index, name = "ERD_SDX55_index"),

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
]
