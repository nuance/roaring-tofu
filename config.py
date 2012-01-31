import os

from private import *
import ui

twitter_user = "nuance"
github_user = "nuance"
yelp_user = '5UeW6xMmWClWcOrw6cPXXg'
pinboard_json_feed = 'http://feeds.pinboard.in/json/v1/u:nuance/'

ga_key = "2393143-1"
mixpanel_key = "57a71122b2415e43874dcf95edccd401"

http_params = locals().get('http_params', {})
http_params.update({'static_path': 'static', 'ui_modules': ui, 'template_path': os.path.join(base_path, 'templates'), 'xheaders': True})
