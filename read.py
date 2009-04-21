import web

from model import Article, meta
from private import post_key
from util import render_mako

urls = ('/save', 'save_post',
		'/add/(.+)', 'add_post',
		'/bookmarklet/(.+)', 'bookmarklet')
app_read = web.application(urls, globals())

class save_post(object):
	"""
	Blog servlet
	"""
	def POST(self):
		input = web.input()

		if input.key != post_key:
			return app_read.notfound()

		title = input.title
		url = input.url

		article = Article(title, url)
		meta.session.add(article)
		meta.session.commit()

		web.redirect(url)


class add_post(object):
	"""
	Blog servlet
	"""
	def GET(self, key):
		if key != post_key:
			return app_read.notfound()

		return render_mako('article_submission', key=key)

class bookmarklet(object):
	"""
	Blog servlet
	"""
	def GET(self, key):
		if key == 'css':
			web.header("Content-Type","text/css; charset=utf-8")
			return render_mako('bookmarklet_css')
		if key != post_key:
			return app_read.notfound()

		web.header("Content-Type","application/javascript; charset=utf-8")
		return render_mako('bookmarklet', key=key)
