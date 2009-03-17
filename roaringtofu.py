import web

from blog import app_blog, render_blog
from objects.post import Post
import uri
from util import read_conn, render_mako

urls = ('/blog', app_blog,
		'/', 'index')

app = web.application(urls, globals())
application = app.wsgifunc()

class index(object):
	def GET(self):
		posts = Post.select_by_range(read_conn, 0, 5)

		return render_blog(posts=posts)

if __name__ == "__main__":
	app.run()
