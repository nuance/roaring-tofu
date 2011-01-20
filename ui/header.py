import tornado.web

class Header(tornado.web.UIModule):
	def css_files(self):
		return ["css/header.css"]

	def render(self, info):
		return self.render_string('header.thtml', info=info)

