from tornado import web

from model import meta, Post
from base import BaseHandler

class view_post(BaseHandler):
	"""
	Blog servlet
	"""
	_path = '/post/(.+)'

	def get(self, alias):
		post = Post.by_alias(alias)

		if not post:
			# 404
			return app_blog.notfound()

		self.render_blog(posts=post, rpp=1)

