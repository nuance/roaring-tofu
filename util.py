from web.contrib.template import render_mako

render = render_mako(directories=['templates'], input_encoding='utf-8', output_encoding='utf-8', default_filters=['unicode', 'h'])

def render_mako(tmpl, *args, **kwargs):
	template = render._lookup.get_template(tmpl + ".mako")
	return template.render(*args, **kwargs)

def batch(fun):
	"""
	no-op for now, but this should signify functions that can only be ran in batch mode (eg from the command line)
	"""
	return fun

