import datetime
from ckan.lib.navl.dictization_functions import Invalid
from ckan.logic.validators import int_validator
import ckan.lib.helpers as h
from ckan.common import _



def solrdate(value, context):
    if isinstance(value, datetime.datetime):
        return value + 'Z'
    if value == '' or value==None:
        return None
    if value[-1] =='Z':
	return value
    try:
        date = h.date_str_to_datetime(value)
    except (TypeError, ValueError), e:
        raise Invalid(_('Date format incorrect'))
    return date.isoformat()+  'Z'
