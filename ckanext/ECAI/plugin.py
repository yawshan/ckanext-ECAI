import logging

import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
import ckanext.ECAI.helpers as ECAI_helpers
from ckanext.ECAI import validators

log = logging.getLogger(__name__)

def _get_module_functions(module, function_names):
    functions = {}
    for f in function_names:
        functions[f] = module.__dict__[f]

    return functions

class ECAIPlugin(plugins.SingletonPlugin,
        tk.DefaultDatasetForm):
    '''An example IDatasetForm CKAN plugin.

    Uses a tag vocabulary to add a custom metadata field to datasets.

    '''
    plugins.implements(plugins.IConfigurer, inherit=False)
    plugins.implements(plugins.IDatasetForm, inherit=False)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IValidators)
    plugins.implements(plugins.IPackageController, inherit=True)

    # These record how many times methods that this plugin's methods are
    # called, for testing purposes.
    num_times_new_template_called = 0
    num_times_read_template_called = 0
    num_times_edit_template_called = 0
    num_times_search_template_called = 0
    num_times_history_template_called = 0
    num_times_package_form_called = 0
    num_times_check_data_dict_called = 0
    num_times_setup_template_variables_called = 0

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
        tk.add_public_directory(config, 'public')
	tk.add_resource('fanstatic', 'ecai')

    def get_helpers(self):

        function_names = (
        'get_DC_LANGUAGE',
	    'get_DC_TYPE',
	    'get_DC_FORMAT',
	    'get_ECAI_TEAM',
	    'get_DC_SUBJECT_DOMAIN',
	    'extras_to_dict',
        )
        return _get_module_functions(ECAI_helpers, function_names)


    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []

    def _modify_package_schema(self, schema):
        _convert_to_extras = plugins.toolkit.get_converter('convert_to_extras')
        _ignore_missing = plugins.toolkit.get_validator('ignore_missing')
        _ignore_empty = plugins.toolkit.get_validator('ignore_empty')
        _int_validator = plugins.toolkit.get_validator('int_validator')
	_solrdate = plugins.toolkit.get_validator('solrdate')

        schema.update({
            		'spatial': [_ignore_missing, _convert_to_extras],
            		'DC_Title': [_ignore_missing, _convert_to_extras],
			'DC_Title_Alternative': [_ignore_missing, _convert_to_extras],
			'DC_Creator_PersonalName': [_ignore_missing, _convert_to_extras],
			'DC_Creator_PersonalName_Address': [_ignore_missing, _convert_to_extras],
			'DC_Creator_CorporateName': [_ignore_missing, _convert_to_extras],
			'DC_Creator_CorporateName_Address': [_ignore_missing, _convert_to_extras],
			'DC_Subject_Specific': [_ignore_missing, _convert_to_extras],
			'DC_Description': [_ignore_missing, _convert_to_extras],
			'DC_Description_History': [_ignore_missing, _convert_to_extras],
			'DC_Publisher': [_ignore_missing, _convert_to_extras],
			'DC_Publisher_Address': [_ignore_missing, _convert_to_extras],
			'DC_Contributor_CorporateName': [_ignore_missing, _convert_to_extras],
			'DC_Contributor_CorporateName_Address': [_ignore_missing, _convert_to_extras],
			'DC_Contributor_PersonalName': [_ignore_missing, _convert_to_extras],
			'DC_Contributor_PersonalName_Address': [_ignore_missing, _convert_to_extras],
			'DC_Identifier': [_ignore_missing, _convert_to_extras],
			'DC_Source': [_ignore_missing, _convert_to_extras],
			'DC_Language': [_ignore_missing, _convert_to_extras],
			'DC_Rights': [_ignore_missing, _convert_to_extras],
			'DC_Date_Created': [_ignore_missing, _solrdate,  _convert_to_extras],
			'DC_Date_DataGathered': [_ignore_missing, _solrdate,  _convert_to_extras],
			'DC_Date_Valid': [_ignore_missing, _solrdate, _convert_to_extras],
			'DC_Date_LastModified': [_ignore_missing, _solrdate, _convert_to_extras],
			'DC_Date_Issued': [_ignore_missing, _solrdate, _convert_to_extras],
			'DC_Date_Available': [_ignore_missing, _solrdate, _convert_to_extras],
			'DC_Date_Accepted': [_ignore_missing, _solrdate, _convert_to_extras],
			'DC_Date_Acquired': [_ignore_missing, _solrdate, _convert_to_extras],
			'DC_Type': [_ignore_missing, _convert_to_extras],
			'DC_Type_Specific': [_ignore_missing, _convert_to_extras],
			'DC_Format': [_ignore_missing, _convert_to_extras],
			'DC_Format_Specific': [_ignore_missing, _convert_to_extras],
			'DC_Format_Size': [_ignore_missing, _convert_to_extras],
			'DC_Relation': [_ignore_missing, _convert_to_extras],
			'DC_Relation_Type': [_ignore_missing, _convert_to_extras],
			'DC_Relation_Identifier': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_X_min': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_X_max': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_Y_min': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_Y_max': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_T_Early': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_T_Late': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_PeriodName': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_PlaceName': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_Spatial_Resolution': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_Spatial_Aggregation': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_Spatial_Georeference': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_Temporal_Precision': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_Temporal_Interval': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_Temporal_Aggregation': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_AlternativeMetadata': [_ignore_missing, _convert_to_extras],
			'DC_Coverage_Notes': [_ignore_missing, _convert_to_extras],
			'ECAI_Team': [_ignore_missing, _convert_to_extras],
			'ECAI_Theme': [_ignore_missing, _convert_to_extras],
			'ECAI_Notes': [_ignore_missing, _convert_to_extras],
			'ECAI_UseRestrictions': [_ignore_missing, _convert_to_extras],
			'ECAI_Content': [_ignore_missing, _convert_to_extras],
			'ECAI_Expert': [_ignore_missing, _convert_to_extras],
			'ECAI_Expert_Commentary': [_ignore_missing, _convert_to_extras],
			'ECAI_Expert_InternalNotes': [_ignore_missing, _convert_to_extras],
        })

        return schema

    def create_package_schema(self):
        schema = super(ECAIPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(ECAIPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(ECAIPlugin, self).show_package_schema()

        # Import core converters and validators
        _convert_from_extras = plugins.toolkit.get_converter('convert_from_extras')
        _ignore_missing = plugins.toolkit.get_validator('ignore_missing')
        _ignore_empty = plugins.toolkit.get_validator('ignore_empty')
        _int_validator = plugins.toolkit.get_validator('int_validator')

        schema.update({
			'spatial': [_convert_from_extras,_ignore_missing],
       			'DC_Title': [_convert_from_extras,_ignore_missing],
			'DC_Title_Alternative': [_convert_from_extras,_ignore_missing],
			'DC_Creator_CorporateName': [_convert_from_extras,_ignore_missing],
			'DC_Creator_CorporateName_Address': [_convert_from_extras,_ignore_missing],
			'DC_Creator_PersonalName': [_convert_from_extras,_ignore_missing],
			'DC_Creator_PersonalName_Address': [_convert_from_extras,_ignore_missing],
			'DC_Subject_Specific': [_convert_from_extras,_ignore_missing],
			'DC_Description': [_convert_from_extras,_ignore_missing],
			'DC_Description_History': [_convert_from_extras,_ignore_missing],
			'DC_Publisher': [_convert_from_extras,_ignore_missing],
			'DC_Publisher_Address': [_convert_from_extras,_ignore_missing],
			'DC_Contributor_CorporateName': [_convert_from_extras,_ignore_missing],
			'DC_Contributor_CorporateName_Address': [_convert_from_extras,_ignore_missing],
			'DC_Contributor_PersonalName': [_convert_from_extras,_ignore_missing],
			'DC_Contributor_PersonalName_Address': [_convert_from_extras,_ignore_missing],
			'DC_Identifier': [_convert_from_extras,_ignore_missing],
			'DC_Source': [_convert_from_extras,_ignore_missing],
			'DC_Language': [_convert_from_extras,_ignore_missing],
			'DC_Rights': [_convert_from_extras,_ignore_missing],
			'DC_Date_Created': [_convert_from_extras,_ignore_missing],
			'DC_Date_DataGathered': [_convert_from_extras,_ignore_missing],
			'DC_Date_Valid': [_convert_from_extras,_ignore_missing],
			'DC_Date_LastModified': [_convert_from_extras,_ignore_missing],
			'DC_Date_Issued': [_convert_from_extras,_ignore_missing],
			'DC_Date_Available': [_convert_from_extras,_ignore_missing],
			'DC_Date_Accepted': [_convert_from_extras,_ignore_missing],
			'DC_Date_Acquired': [_convert_from_extras,_ignore_missing],
			'DC_Type': [_convert_from_extras,_ignore_missing],
			'DC_Type_Specific': [_convert_from_extras,_ignore_missing],
			'DC_Format': [_convert_from_extras,_ignore_missing],
			'DC_Format_Specific': [_convert_from_extras,_ignore_missing],
			'DC_Format_Size': [_convert_from_extras,_ignore_missing],
			'DC_Relation': [_convert_from_extras,_ignore_missing],
			'DC_Relation_Type': [_convert_from_extras,_ignore_missing],
			'DC_Relation_Identifier': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_X_min': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_X_max': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_Y_min': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_Y_max': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_T_Early': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_T_Late': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_PeriodName': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_PlaceName': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_Spatial_Resolution': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_Spatial_Aggregation': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_Spatial_Georeference': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_Temporal_Precision': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_Temporal_Interval': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_Temporal_Aggregation': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_AlternativeMetadata': [_convert_from_extras,_ignore_missing],
			'DC_Coverage_Notes': [_convert_from_extras,_ignore_missing],
			'ECAI_Team': [_convert_from_extras,_ignore_missing],
			'ECAI_Theme': [_convert_from_extras,_ignore_missing],
			'ECAI_Notes': [_convert_from_extras,_ignore_missing],
			'ECAI_UseRestrictions': [_convert_from_extras,_ignore_missing],
			'ECAI_Content': [_convert_from_extras,_ignore_missing],
			'ECAI_Expert': [_convert_from_extras,_ignore_missing],
			'ECAI_Expert_Commentary': [_convert_from_extras,_ignore_missing],
			'ECAI_Expert_InternalNotes': [_convert_from_extras,_ignore_missing],
        })

        return schema


    def get_validators(self):
	function_names = (
            'solrdate',
        )
        return _get_module_functions(validators, function_names)


    # These methods just record how many times they're called, for testing
    # purposes.
    # TODO: It might be better to test that custom templates returned by
    # these methods are actually used, not just that the methods get
    # called.

    def setup_template_variables(self, context, data_dict):
        ECAIPlugin.num_times_setup_template_variables_called += 1
        return super(ECAIPlugin, self).setup_template_variables(
                context, data_dict)

    def before_index(self, data_dict):
        # log.debug(data_dict.get("DC_Coverage_T_Early"))
        DC_Coverage_T_Early = data_dict.get("DC_Coverage_T_Early")
        DC_Coverage_T_End = data_dict.get("DC_Coverage_T_Late")

        if  DC_Coverage_T_Early:
            if DC_Coverage_T_Early.count(";") < 1:
                if DC_Coverage_T_Early.count("-") < 2:
                    data_dict['Start_Date'] = int(DC_Coverage_T_Early)
                else :
                    if DC_Coverage_T_Early.find('-') ==0:
                        data_dict['Start_Date'] = int('-' + DC_Coverage_T_Early.split('-')[1])
                    else:
                        data_dict['Start_Date'] = int(DC_Coverage_T_Early.split('-')[0])
            else:
                log.debug(DC_Coverage_T_Early)

        if  DC_Coverage_T_End:
            log.debug(DC_Coverage_T_End)
            if DC_Coverage_T_End.count(";") < 1:
                if DC_Coverage_T_End.count("-") < 2:
                    data_dict['End_Date'] = int(DC_Coverage_T_End)
                else :
                    if DC_Coverage_T_End.find('-') ==0:
                        data_dict['End_Date'] = int('-' + DC_Coverage_T_End.split('-')[1])
                    else:
                        data_dict['End_Date'] = int(DC_Coverage_T_End.split('-')[0])
            else:
                log.debug(DC_Coverage_T_End)


        # data_dict.update({'data_type_facet': '', 'proj_facet': '', 'language_facet': '',
        #         'encoding_facet': '', 'theme_keyword_facets': [], 'loc_keyword_facet': []})
        # fields = helpers.get_field_choices('dataset')
        # for field_name in ['data_type', 'proj', 'language', 'encoding']:
        #     value = data_dict.get(field_name)
        #     if value:
        #         data_dict[field_name+'_facet'] = fields[field_name][value]
        # if data_dict.get('theme_keyword'):
        #     data_dict['theme_keyword_facets'] = json.loads(data_dict.get('theme_keyword'))
        # #For old schema definition
        # for i in range(5):
        #     field_name = 'theme_keyword_' + str(i+1)
        #     if isinstance(data_dict.get(field_name), unicode):
        #     data_dict['theme_keyword_facets'].append(fields['theme_keyword'].get(data_dict[field_name]))
        # if data_dict.get('loc_keyword'):
        #     data_dict['loc_keyword_facet'] = json.loads(data_dict.get('loc_keyword'))
        #     if isinstance(data_dict['loc_keyword_facet'], list):
        #         data_dict['loc_keyword_facet'] = [fields['loc_keyword'][loc_keyword] for loc_keyword in filter(None, data_dict['loc_keyword_facet'])]
        #     #For old schema definition
        # elif isinstance(data_dict['loc_keyword_facet'], int):
        #         data_dict['loc_keyword_facet'] = fields['loc_keyword'][str(data_dict['loc_keyword'])]
        return data_dict

    def new_template(self):
        ECAIPlugin.num_times_new_template_called += 1
        return super(ECAIPlugin, self).new_template()

    def read_template(self):
        ECAIPlugin.num_times_read_template_called += 1
        return super(ECAIPlugin, self).read_template()

    def edit_template(self):
        ECAIPlugin.num_times_edit_template_called += 1
        return super(ECAIPlugin, self).edit_template()

    def search_template(self):
        ECAIPlugin.num_times_search_template_called += 1
        return super(ECAIPlugin, self).search_template()

    def history_template(self):
        ECAIPlugin.num_times_history_template_called += 1
        return super(ECAIPlugin, self).history_template()

    def package_form(self):
        ECAIPlugin.num_times_package_form_called += 1
        return super(ECAIPlugin, self).package_form()

    # check_data_dict() is deprecated, this method is only here to test that
    # legacy support for the deprecated method works.
    def check_data_dict(self, data_dict, schema=None):
        ECAIPlugin.num_times_check_data_dict_called += 1

class TimeSearchPlugin(plugins.SingletonPlugin):

    plugins.implements(plugins.IPackageController, inherit=True)


    def before_search(self, search_params):
        extras = search_params.get('extras')
        log.debug("extras: {0}".format(extras))
        if not extras:
            # There are no extras in the search params, so do nothing.
            return search_params

        start_date = extras.get('ext_startdate')
        log.debug("start_date: {0}".format(start_date))

        end_date = extras.get('ext_enddate')
        log.debug("end_date: {0}".format(end_date))

        if not start_date and not end_date:
            # The user didn't select either a start and/or end date, so do nothing.
            return search_params
        if not start_date:
            start_date = '*'
        if not end_date:
            end_date = '*'
        # Add a date-range query with the selected start and/or end dates into the Solr facet queries.
        fq = search_params['fq']
	log.debug("search_params: {0}".format(search_params))
        log.debug("fq: {0}".format(fq))
        fq = '{fq} +Start_Date:[{sd} TO *],End_Date:[* TO {ed}]'.format(fq=fq, sd=start_date,ed=end_date)
        # fq = '{fq} +End_Date:[* TO {ed}]'.format(fq=fq, ed=end_date)

        log.debug("fq: {0}".format(fq))
        search_params['fq'] = fq
        log.debug("search_params: {0}".format(search_params))

        return search_params
 