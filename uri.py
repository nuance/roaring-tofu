
class URIBase(object):
	@classmethod
	def link(cls, **kwargs):
		return "<link %s/>" % " ".join("%s=\"%s\"" % i for i in kwargs.iteritems())

class Static(URIBase):
	@classmethod
	def css_link(cls, stylesheet):
		return cls.link(rel="stylesheet", type="text/css", href="/static/%s" % stylesheet)

class Blog(URIBase):
	@classmethod
	def view_post(cls, post_id):
		return "/blog/view/%s" % post_id
