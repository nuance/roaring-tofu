import web

from model import Post, meta
from util import render_mako

urls = ('/view/(\d+)', 'view_post')
app_blog = web.application(urls, globals())

def render_blog(posts=[], recent_tweet="foo", commits=[], reviews=[], articles=[]):
	return render_mako('index', posts=posts,
					   recent_tweet=recent_tweet,
					   commits=commits,
					   reviews=reviews,
					   articles=articles)

class view_post(object):
	"""
	Blog servlet
	"""
	def GET(self, id):
		post = meta.session.query(Post, Post.id == id).all()

		if not post:
			# 404
			return app_blog.notfound()

		return render_blog(posts=post)
