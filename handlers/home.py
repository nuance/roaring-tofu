from handlers.base import BaseHandler
from model import Post, meta

class index(BaseHandler):
	_path = '/(\d*)'

	def get(self, offset):
		count = meta.session.query(Post).count()

		if offset:
			offset = int(offset)
		else:
			offset = 0

		if offset > count:
			# temp redirect to home
			pass

		self.render_blog(post_count=count, offset=offset, rpp=5)

