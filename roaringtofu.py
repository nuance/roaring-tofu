import web

from blog import Blog, app_blog
import uri
from util import render_mako

urls = ('/blog', app_blog,
		'/', 'index')

app = web.application(urls, globals())
application = app.wsgifunc()

class blog(object):
	def GET(self, *args):
		return "foo %s" % args

class index(object):
	def GET(self):
		posts = Blog.load_posts()

		return render_mako('index', uri=uri, posts=posts)

if __name__ == "__main__":
	app.run()
