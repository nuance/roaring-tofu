import web

from objects.post import Post
from util import render_mako

urls = ('/view/(\d+)', 'view_post')
app_blog = web.application(urls, globals())

def render_blog(posts=[], recent_tweet="foo", commits=[], reviews=[], articles=[]):
	return render_mako('index', posts=posts, recent_tweet=recent_tweet, commits=commits, reviews=reviews, articles=articles)

class view_post(object):
	"""
	Blog servlet
	"""
	def GET(self, id):
		post = Post.select_by_id(int(id))

		return render_blog(posts=post)
