import requests
from .exceptions import ApiException


class ApiWrapper:

    def __init__(self, api_server_url, api_key, max_chunk_size=41943040, connect_timeout=10):

        self.api_server_url = api_server_url
        self.api_key = api_key
        self.max_chunk_size = max_chunk_size
        self.connect_timeout = connect_timeout

    def get_api_version(self):

        response = self._request('/version', 'GET')

        return response.json().get('version') or ''

    def _request(self, api_method, http_method, headers={}, params={}):

        request_url = self.api_server_url + api_method

        if http_method == 'GET':

            return requests.get(request_url, params=params, headers=headers)

    def _check_result(self, api_method, result):

        if result.status_code != 200:
            msg = 'The server returned HTTP {0} {1}. Response body:\n[{2}]' \
                .format(result.status_code, result.reason, result.text.encode('utf8'))
            raise ApiException(msg, api_method, result)

        try:
            result_json = result.json()
        except:
            msg = 'The server returned an invalid JSON response. Response body:\n[{0}]' \
                .format(result.text.encode('utf8'))
            raise ApiException(msg, api_method, result)

        if not result_json['ok']:
            msg = 'Error code: {0} Description: {1}' \
                .format(result_json['error_code'], result_json['description'])
            raise ApiException(msg, api_method, result)
        return result_json


"""
    public function getApiVersion()
    {
        $version = '';
        $response = $this->_request('/version', 'GET');

        if ($response['code'] == 200) {
            $result = json_decode($response['result']);
            if (isset($result->version)) {
                $version = $result->version;
            }
        }

        return $version;
    }
    """

"""
private function _request($apiMethodName, $httpMethod, $httpHeaders = [], $params = '')
    {

        $response = [];

        $ch = curl_init($this->apiServerUrl . $apiMethodName);

        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, $httpMethod);
        if ($httpMethod == 'POST') {
            curl_setopt($ch, CURLOPT_POST, true);
            curl_setopt($ch, CURLOPT_POSTFIELDS, $params);
        }
        curl_setopt($ch, CURLOPT_HTTPHEADER, $httpHeaders);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        $response['result'] = curl_exec($ch);
        $response['code'] = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $response['error'] = curl_error($ch);
        curl_close($ch);

        if (!empty($response['error'])) {
            throw new \Exception($response['error']);
        }

        return $response;
    }
"""