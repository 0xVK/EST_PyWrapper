from .BaseApplicationInput import BaseApplicationInput


class AxcApplicationInput(BaseApplicationInput):

    FIRM_DATA_FILE = 'firm_data'

    MARKET_DATA_FILE = 'market_data'

    REQUEST_DATA_FILE = 'request_file'

    def set_return_type(self, return_type):
        self.set('parameters', 'return_type', return_type)

    def set_result_file_type(self, result_file_type):
        self.set('parameters', 'result_file_type', result_file_type)

    def set_non_trading_days(self, non_trading_days):
        self.set('parameters', 'non_trading_days', non_trading_days)

    def set_benchmark_model(self, benchmark_model):
        self.set('parameters', 'benchmark_model', benchmark_model)

    def set_regression_method(self, regression_method):
        self.set('parameters', 'regression_method', regression_method)

    def init_request_data_source(self, source_type, source_hash=''):
        self.init_data_source(self.REQUEST_DATA_FILE, source_type, source_hash)

    def init_market_data_source(self, source_type, source_hash=''):
        self.init_data_source(self.MARKET_DATA_FILE, source_type, source_hash)

    def init_firm_data_source(self, source_type, source_hash=''):
        self.init_data_source(self.FIRM_DATA_FILE, source_type, source_hash)

    def set_test_statistics(self, test_statistics=[]):

        if test_statistics:

            self.set('parameters', 'test_statistics', [])

            for item in test_statistics:
                self.request_data['parameters']['test_statistics'].append(item)
