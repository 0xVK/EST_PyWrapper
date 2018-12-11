import EventStudyToolsApi

api = EventStudyToolsApi.ApiWrapper('http://api.eventstudytools.com', '83c450c8a82cd2597b33d3486cdcb9d4')

print(api.get_api_version())