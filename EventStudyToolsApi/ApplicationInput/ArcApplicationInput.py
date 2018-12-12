from .AxcApplicationInput import AxcApplicationInput


class ArcApplicationInput(AxcApplicationInput):

    def __init__(self):

        self.set_application_key('arc')

        self.set_return_type(self.RETURN_TYPE_LOG)
        self.set_result_file_type('ods')
        self.set_non_trading_days('later')
        self.set_benchmark_model('mm')
        self.set_regression_method('ols')
