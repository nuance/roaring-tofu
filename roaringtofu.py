import web

from blog import app_blog, render_blog
from objects.post import Post

urls = ('/blog', app_blog,
		'/', 'index')

app = web.application(urls, globals())
application = app.wsgifunc()

class index(object):
	def GET(self):
		posts = Post.select_by_range(0, 5)
		raise Exception("foo")

		return render_blog(posts=posts)

if __name__ == "__main__":
	app.run()
