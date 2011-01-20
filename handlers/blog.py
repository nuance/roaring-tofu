from tornado import web

from model import meta, Post
from handlers.base import BaseHandler

class view_post(BaseHandler):
	"""
	Blog servlet
	"""
	_path = '/post/(.+)'

	def get(self, alias):
		post = Post.by_alias(unicode(alias))

		if not post:
			raise web.HTTPError(404)

		header = self.load_header()
		self.render('post.thtml', header=header, post=post)
