import tornado.web

class BootstrapCSS(tornado.web.UIModule):
	def render(self):
		return ''

	def css_files(self):
		return ["css/bootstrap/bootstrap.css", "css/bootstrap/bootstrap.responsive.css"]