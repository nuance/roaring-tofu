import tornado.web

class BaseCSS(tornado.web.UIModule):
	def render(self):
		return ''

	def css_files(self):
		return ["css/base.css"]
