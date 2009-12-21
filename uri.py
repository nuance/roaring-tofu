
class URIBase(object):
	@classmethod
	def tag(cls, name, contents=None, **kwargs):
		"""
		Converts into <name **kwargs>contents</name>.
		"""
		start = "<%s %s" % (name, " ".join("%s=\"%s\"" % i for i in kwargs.iteritems()))

		if contents is None:
			return start + "/>"
		else:
			return "%s>%s</%s>" % (start, contents, name)

	@classmethod
	def link(cls, **kwargs):
		return cls.tag("link", **kwargs)

	@classmethod
	def a(cls, url, text, nofollow=True, **kwargs):
		if nofollow:
			kwargs['rel'] = 'nofollow'
		#FIXME: this needs to do escaping
		return cls.tag("a", href=uri, contents=text, **kwargs)

	@classmethod
	def script(cls, url, type="text/javascript", **kwargs):
		return cls.tag("script", src=url, type=type,
					   contents="", **kwargs)

class Static(URIBase):
	@classmethod
	def css_link(cls, stylesheet, **kwargs):
		return cls.link(rel="stylesheet", type="text/css",
						href="/static/css/%s" % stylesheet,
						**kwargs)

	@classmethod
	def js_link(cls, script, **kwargs):
		src = "/static/js/%s" % script
		return cls.script(src)

class Blog(URIBase):
	@classmethod
	def view_post(cls, post_id):
		return "/blog/view/%s" % post_id

class Twitter(URIBase):
	@classmethod
	def tweet_url(cls, user, tweet_id):
		return "http://twitter.com/%(user)s/status/%(tweet_id)d" % locals()
