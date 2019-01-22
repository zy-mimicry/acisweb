#! /usr/bin/env python3
# coding=utf-8

import logging
import logging.config
import os

# Maybe you want to create a logger dynamically, fill it here please ^_^.

DEBUG_LOG_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/DebugLogs/'
if not os.path.exists(DEBUG_LOG_ROOT):
    os.makedirs(DEBUG_LOG_ROOT)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'pure': {
            'format': '%(name)s %(message)s'
        },
    },

    'handlers': {

        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'pure',
        },

        'vcore_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': DEBUG_LOG_ROOT + 'vcore.log',
            'mode' : 'a',
            'formatter': 'pure',
        },
        'views_rex_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': DEBUG_LOG_ROOT + 'views.rex.log',
            'formatter': 'pure',
        },

        'from_excel': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': DEBUG_LOG_ROOT + 'data_from_excel.log',
            'mode' : 'w',
            'formatter': 'pure',
        },
        'from_jira': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': DEBUG_LOG_ROOT + 'data_from_jira.log',
            'mode' : 'w',
            'formatter': 'pure',
        },
        'from_jenkins': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': DEBUG_LOG_ROOT + 'data_from_jenkins.log',
            'mode' : 'w',
            'formatter': 'pure',
        },
        'pick_all': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': DEBUG_LOG_ROOT + 'pick_all.log',
            'mode' : 'w',
            'formatter': 'pure',
        },
    },

    'loggers': {
        'AcisDB': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'AcisDB.vcore': {
            'handlers': ['vcore_file'],
            'level': 'DEBUG',
            'propagate': True,
        },

        'AcisDB.views_of_rex': {
            'handlers': ['views_rex_file', 'console'],
            #'handlers': ['views_rex_file'],
            'level': 'DEBUG',
            'propagate': True,
        },

        ## For Web Server Data Debug.
        'AcisDB.views_of_rex.from_excel': {
            'handlers': ['from_excel'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'AcisDB.views_of_rex.from_jira': {
            'handlers': ['from_jira'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'AcisDB.views_of_rex.from_jenkins': {
            'handlers': ['from_jenkins'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'AcisDB.vcore.pick_all': {
            'handlers': ['pick_all'],
            'level': 'DEBUG',
            'propagate': False,
        },

    },
}

logging.config.dictConfig(LOGGING)
