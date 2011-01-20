import tornado.web

class Feeds(tornado.web.UIModule):
	def render(self):
		return ''

	def html_head(self):
		return """<link rel="alternate" type="application/rss+xml" title="The Book of Jones &raquo; Feed" href="http://mhjones.org/rss" />"""
