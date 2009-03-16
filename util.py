from web.contrib.template import render_mako

render = render_mako(directories=['templates'],
	input_encoding='utf-8', output_encoding='utf-8')

def render_mako(tmpl, *args, **kwargs):
	template = render._lookup.get_template(tmpl + ".mako")
	return template.render(*args, **kwargs)
