import os

from private import *
import ui

twitter_user = "nuance"
github_user = "nuance"
yelp_user = '5UeW6xMmWClWcOrw6cPXXg'
pinboard_json_feed = 'http://feeds.pinboard.in/json/v1/u:nuance/'

ga_key = "2393143-1"

http_params = {'static_path': 'static', 'debug': True, 'ui_modules': ui, 'template_path': os.path.join(base_path, 'templates')}

