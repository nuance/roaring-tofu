import tornado.web

class Sidebar(tornado.web.UIModule):
	def css_files(self):
		return ["css/header.css"]

	def render(self, info):
		return self.render_string('sidebar.thtml', info=info)

