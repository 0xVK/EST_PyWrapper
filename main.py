import json

from EventStudyToolsApi import ApiWrapper
from EventStudyToolsApi.ApplicationInput.ArcApplicationInput import ArcApplicationInput
from EventStudyToolsApi.TestStatistics import ArcTestStatistics

api = ApiWrapper('http://api.dev.eventstudytools.com', '83c450c8a82cd2597b33d3486cdcb9d4')

print('Api ver:', api.get_api_version())
print('Auth: ', api.authentication())

arcAppInput = ArcApplicationInput()

arcAppInput.set_email('koocherov@ya.ru')
arcAppInput.set_locale(ArcApplicationInput.LOCALE_EN)
arcAppInput.init_request_data_source(ArcApplicationInput.DATA_SOURCE_TYPE_CSV)
arcAppInput.init_firm_data_source(ArcApplicationInput.DATA_SOURCE_TYPE_CSV)
arcAppInput.init_market_data_source(ArcApplicationInput.DATA_SOURCE_TYPE_CSV)

t = [
    ArcTestStatistics.AAR_ABMPZ,
    ArcTestStatistics.AAR_PTLZ,
    ArcTestStatistics.AAR_T,
]
arcAppInput.set_test_statistics(t)

api.configure_task(arcAppInput)

# print(json.dumps(arcAppInput.get_dict()))