from EventStudyToolsApi import ApiWrapper, ArcApplicationInput

api = ApiWrapper('http://api.dev.eventstudytools.com', '83c450c8a82cd2597b33d3486cdcb9d4')

print('Api ver:', api.get_api_version())
print('Auth: ', api.authentication())

api = ArcApplicationInput()
api.set_email('koocherov@ya.ru')
api.set_locale('en')
api.init_data_source('csv', 'e82b691e212d7d55425ab318b25ce11b')
api.init_firm_data_source('csv', '29ec0695c3fa929921f69e0cf05aedfb')
api.init_market_data_source('csv', '29ec0695c3fa929921f69e0cf05a2323')
print(api.get_dict())