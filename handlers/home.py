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
			self.redirect('/')

		rpp = 5

		posts = meta.session.query(Post).order_by(Post.time_created.desc()).limit(rpp).offset(offset).all()
		header = self.load_header()

		prev = None
		if offset:
			prev = max(offset - rpp, 0)
		next = None
		if offset + rpp < count:
			next = min(count - 1, offset + rpp)

		newer_url = None
		if prev:
			newer_url = '/%d' % (prev,)

		older_url = None
		if next:
			older_url = '/%d' % (next,)

		self.render('blog.thtml', header=header, posts=posts, newer_url=None, older_url=None)
