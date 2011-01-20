import os.path

import private
import ui

engine_url = getattr(private, 'engine_url', 'sqlite:////srv/www/domains/roaringtofu.org/blog.sqlite')
engine_params = getattr(private, 'engine_params', {'echo': False})

twitter_user = "nuance"
github_user = "nuance"
yelp_user = '5UeW6xMmWClWcOrw6cPXXg'
pinboard_json_feed = 'http://feeds.pinboard.in/json/v1/u:nuance/'

ga_key = "2393143-1"

http_params = {'static_path': 'static', 'debug': True, 'ui_modules': ui, 'template_path': os.path.join(private.base_path, 'templates')}

posts_path = '/Users/matt/dev/roaring-tofu'
