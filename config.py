import private

engine_url = getattr(private, 'engine_url', 'sqlite:////srv/www/domains/roaringtofu.org/blog.sqlite')
engine_params = getattr(private, 'engine_params', {'echo': False})

twitter_user = "nuance"
github_user = "nuance"
yelp_user = '5UeW6xMmWClWcOrw6cPXXg'
recently_read_file = "/srv/www/domains/roaringtofu.org/RECENTLY-READ"

ga_key = "2393143-1"

http_params = {'static_path': 'static'}
