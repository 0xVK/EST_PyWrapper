import json


class BaseApplicationInput:

    LOCALE_EN = 'en'

    DATA_SOURCE_TYPE_CSV = 'csv'

    DATA_SOURCE_TYPE_CSV_ZIP = 'csv_zip'
    
    DATA_SOURCE_TYPE_XLS = 'xls'

    DATA_SOURCE_TYPE_XLS_ZIP = 'xls_zip'

    DATA_SOURCE_TYPE_XLSX = 'xlsx'

    DATA_SOURCE_TYPE_XLSX_ZIP = 'xlsx_zip'

    RESULT_FILE_TYPE_XLS = 'xls'

    RESULT_FILE_TYPE_ODS = 'ods'

    RESULT_FILE_TYPE_CSV = 'csv'

    RESULT_FILE_TYPE_XLSX = 'xlsx'
    
    request_data = {}

    def set(self, section, key, value):

        if section not in self.request_data.keys():
            self.request_data[section] = {}

        self.request_data[section][key] = value

    def get_dict(self):
        return self.request_data

    def to_json(self):
        return json.dumps(self.request_data)

    def set_email(self, email):
        self.set('task', 'email', email)

    def set_locale(self, locale):
        self.set('task', 'locale', locale)

    def set_application_key(self, app_key):
        self.set('application', 'key', app_key)

    def init_data_source(self, source_key, source_type, source_hash=''):

        data_source = {
            'key': source_key,
            'type': source_type,
            'hash': source_hash
        }

        if 'data_sources' not in self.request_data['application'].keys():
            self.set('application', 'data_sources', [])

        self.request_data['application']['data_sources'].append(data_source)
