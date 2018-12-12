import requests
import telebot
from .exceptions import ApiException
from .ApplicationInput.BaseApplicationInput import BaseApplicationInput


class ApiWrapper:

    CONTENT_TYPE_HEADER = 'Content-Type'

    CONTENT_TYPE_JSON = 'application/json'

    CONTENT_TYPE_OCTET_STREAM = 'application/octet-stream'

    CUSTOMER_KEY = 'X-Customer-Key'

    TASK_KEY_HEADER = 'X-Task-Key'

    def __init__(self, api_server_url, api_key, max_chunk_size=41943040, connection_timeout=10):

        self.api_server_url = api_server_url
        self.api_key = api_key
        self.max_chunk_size = max_chunk_size
        self.connection_timeout = connection_timeout
        self.token = ''

    def get_api_version(self):

        response = self._request('/version', 'GET')

        return response.get('version') or ''

    def authentication(self):

        headers = {
            self.CONTENT_TYPE_HEADER: self.CONTENT_TYPE_JSON,
            self.CUSTOMER_KEY: self.api_key,
        }

        response = self._request('/task/create', 'POST', headers)

        self.token = response.get('token')

        return self.token

    def configure_task(self, application_input):

        json = application_input.to_json()

        headers = {
            self.CONTENT_TYPE_HEADER: self.CONTENT_TYPE_JSON,
            self.TASK_KEY_HEADER: self.token,
        }

        print(headers)

        response = self._request('/task/conf', 'POST', headers, json)

    def _request(self, api_method, http_method, headers={}, json_data=''):

        request_url = self.api_server_url + api_method

        if http_method == 'GET':
            response = requests.get(request_url, headers=headers)

        if http_method == 'POST':
            response = requests.post(request_url, json=json_data, headers=headers)

        return self._check_result(api_method, response)


    def _check_result(self, api_method, result):

        print('METHOD: ', api_method)
        print(result.request.headers)
        # print(result.status_code)

        try:
            result_json = result.json()
        except:
            msg = 'The server returned an invalid JSON response. Response body:\n[{0}]' \
                .format(result.text.encode('utf8'))
            raise ApiException(msg, api_method, result)

        if result_json.get('error'):
            msg = 'The server returned an error : {}'.format(result_json['error'])
            raise ApiException(msg, api_method, result)

        if result.status_code != 200:
            msg = 'The server returned HTTP {0} {1}. Response body:\n[{2}]' \
                .format(result.status_code, result.reason, result.text.encode('utf8'))
            raise ApiException(msg, api_method, result)

        return result_json
