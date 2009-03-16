from collections import defaultdict

import web
from web.contrib.template import render_mako

import uri

urls = ('/', 'index')
app = web.application(urls, globals())
application = app.wsgifunc()

render = render_mako(directories=['templates'],
	input_encoding='utf-8', output_encoding='utf-8')

def render_mako(tmpl, *args, **kwargs):
	template = render._lookup.get_template(tmpl + ".mako")
	return template.render(*args, **kwargs)

class index(object):
	def GET(self):
		return render_mako('index', uri=uri, posts=[])

if __name__ == "__main__":
	app.run()
