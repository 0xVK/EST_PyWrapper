import json


class BaseApplicationInput:

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

        self.set('application', 'application', [])

        self.request_data['application']['application'].append(data_source)
