from sqlalchemy import create_engine
import web

from blog import app_blog, render_blog
from model import Post, init_model, meta

urls = ('/blog', app_blog,
		'/', 'index')

app = web.application(urls, globals())
application = app.wsgifunc()
read_conn = create_engine('sqlite:///blog.sqlite', echo=True)
init_model(read_conn)

class index(object):
	def GET(self):
		posts = meta.session.query(Post).order_by(Post.id).limit(5).all()

		return render_blog(posts=posts)

if __name__ == "__main__":
	app.run()
