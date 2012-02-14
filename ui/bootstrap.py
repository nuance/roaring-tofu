import tornado.web

class BootstrapCSS(tornado.web.UIModule):
	def render(self):
		return ''

	def css_files(self):
		return ["css/bootstrap/bootstrap.min.css", "css/bootstrap/bootstrap.min.responsive.css"]
