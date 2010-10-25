from tornado import web

from base import BaseHandler
from model import Article, meta
from private import post_key
from util import render_mako

class save_post(BaseHandler):
	"""
	Blog servlet
	"""
	_path = '/read/save'

	def post(self):
		key = self.get_argument('key')

		if key != post_key:
			raise web.HTTPError(404)

		title = input.title
		url = input.url

		article = Article(title, url)
		meta.session.add(article)
		meta.session.commit()

		self.redirect(url)


class add_post(BaseHandler):
	"""
	Blog servlet
	"""
	_path = '/read/add/(.+)'

	def get(self, key):
		if key != post_key:
			raise web.HTTPError(404)

		return render_mako('article_submission', key=key)


class bookmarklet(BaseHandler):
	"""
	Blog servlet
	"""
	_path = '/read/bookmarklet/(.+)'

	def get(self, key):
		if key == 'css':
			self.set_header("Content-Type","text/css; charset=utf-8")
			return render_mako('bookmarklet_css')
		if key != post_key:
			raise web.HTTPError(404)

		self.set_header("Content-Type","application/javascript; charset=utf-8")
		return render_mako('bookmarklet', key=key)

