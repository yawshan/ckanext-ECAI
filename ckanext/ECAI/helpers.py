from pylons import config

import ckan.model as model # get_licenses should be in core

import ckan.plugins as p
import ckan.lib.helpers as helpers
import ckan.lib.formatters as formatters

import ckanext.ECAI.lists as lists


def get_DC_LANGUAGE():
   return lists.DC_LANGUAGE

def get_DC_TYPE():
   return lists.DC_TYPE

def get_DC_FORMAT():
   return lists.DC_FORMAT

def get_ECAI_TEAM():
   return lists.ECAI_TEAM

def get_DC_SUBJECT_DOMAIN():
   return lists.DC_SUBJECT_DOMAIN

def extras_to_dict(pkg):
   extras_dict = {}
   if pkg and 'extras' in pkg:
       for extra in pkg['extras']:
            extras_dict[extra['key']] = extra['value']
   return extras_dict

