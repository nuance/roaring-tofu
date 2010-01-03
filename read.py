from tornado import web

from model import Article, meta
from private import post_key
from util import render_mako
import app_urls

class save_post(web.RequestHandler):
	"""
	Blog servlet
	"""
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


class add_post(web.RequestHandler):
	"""
	Blog servlet
	"""
	def get(self, key):
		if key != post_key:
			raise web.HTTPError(404)

		return render_mako('article_submission', key=key)


class bookmarklet(web.RequestHandler):
	"""
	Blog servlet
	"""
	def get(self, key):
		if key == 'css':
			self.set_header("Content-Type","text/css; charset=utf-8")
			return render_mako('bookmarklet_css')
		if key != post_key:
			raise web.HTTPError(404)

		self.set_header("Content-Type","application/javascript; charset=utf-8")
		return render_mako('bookmarklet', key=key)

urls = [('/read/save', save_post),
		('/read/add/(.+)', add_post),
		('/read/bookmarklet/(.+)', bookmarklet)]
app_urls.urls.extend(urls)
