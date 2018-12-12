from .AxcApplicationInput import AxcApplicationInput


class ArcApplicationInput(AxcApplicationInput):

    RETURN_TYPE_LOG = 'log'

    RETURN_TYPE_SIMPLE = 'simple'

    BENCHMARK_MODEL_MM = 'mm'

    BENCHMARK_MODEL_MM_SW = 'mm-sw'

    BENCHMARK_MODEL_CPMAM = 'cpmam'
    
    BENCHMARK_MODEL_MAM = 'mam'
    
    BENCHMARK_MODEL_FF3FM = 'ff3fm'

    BENCHMARK_MODEL_FFM4FM = 'ffm4fm'
    
    BENCHMARK_MODEL_GARCH = 'garch'

    BENCHMARK_MODEL_EGARCH = 'egarch'

    NON_TRADING_DAYS_LATER = 'later'

    NON_TRADING_DAYS_EARLIER = 'earlier'

    NON_TRADING_DAYS_KEEP = 'keep'

    NON_TRADING_DAYS_SKIP = 'skip'

    REGRESSION_METHOD_OLS = 'ols'

    def __init__(self):

        self.set_application_key('arc')

        self.set_return_type(self.RETURN_TYPE_LOG)
        self.set_result_file_type(self.RETURN_TYPE_LOG)
        self.set_non_trading_days(self.NON_TRADING_DAYS_KEEP)
        self.set_benchmark_model(self.BENCHMARK_MODEL_MM)
        self.set_regression_method(self.REGRESSION_METHOD_OLS)

        super().__init__()
