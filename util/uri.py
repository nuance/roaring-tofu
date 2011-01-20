
class URIBase(object):
	@classmethod
	def link(cls, **kwargs):
		return "<link %s/>" % " ".join("%s=\"%s\"" % i for i in kwargs.iteritems())

	@classmethod
	def a(cls, url, text, nofollow=True, **kwargs):
		if nofollow:
			kwargs['rel'] = 'nofollow'
		#FIXME: this needs to do escaping
		return "<a href=\"%s\" %s>%s</a>" % (url, " ".join("%s=\"%s\"" % i for i in kwargs.iteritems()), text)

class Static(URIBase):
	@classmethod
	def css_link(cls, stylesheet, **kwargs):
		return cls.link(rel="stylesheet", type="text/css", href="/static/css/%s" % stylesheet, **kwargs)

class Blog(URIBase):
	@classmethod
	def view_post(cls, post_alias):
		return "/post/%s" % post_alias

	@classmethod
	def offset(cls, offset):
		return "/"

class Twitter(URIBase):
	@classmethod
	def tweet_url(cls, user, tweet_id):
		return "http://twitter.com/%(user)s/status/%(tweet_id)d" % locals()
