class ApiException(Exception):

    def __init__(self, msg, function_name, result):
        super(ApiException, self).__init__("A request to the EventStudyTools API was unsuccessful. {0}".format(msg))
        self.function_name = function_name
        self.result = result
