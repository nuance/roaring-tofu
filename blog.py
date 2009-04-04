import web

from model import Article, Post, Tweet, meta
from util import render_mako

urls = ('/view/(\d+)', 'view_post')
app_blog = web.application(urls, globals())

def render_blog(posts=[], commits=[], reviews=[]):
	articles = Article.recent_articles()
	tweet = Tweet.recent_tweet()

	return render_mako('index', posts=posts,
					   recent_tweet=tweet,
					   commits=commits,
					   reviews=reviews,
					   articles=articles)

class view_post(object):
	"""
	Blog servlet
	"""
	def GET(self, id):
		post = meta.session.query(Post).filter(Post.id == id).all()

		if not post:
			# 404
			return app_blog.notfound()

		return render_blog(posts=post)
