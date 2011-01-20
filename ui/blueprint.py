import tornado.web

class BlueprintCSS(tornado.web.UIModule):
	def render(self):
		return ''

	def html_head(self):
		return """<!--[if IE] <link href=\"""" + self.handler.static_url("css/blueprint/ie.css") + """\"<![endif]-->"""

	def css_files(self):
		return ["css/blueprint/screen.css", "css/blueprint/fancy-type.css"]
