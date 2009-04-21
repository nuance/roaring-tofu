import web

from model import Article, meta
from private import post_key
from util import render_mako

urls = ('/save', 'save_post',
		'/add/(.+)', 'add_post')
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

		web.redirect('/add/%s' % input.key)


class add_post(object):
	"""
	Blog servlet
	"""
	def GET(self, key):
		if key != post_key:
			return app_read.notfound()

		return render_mako('article_submission', key=key)

