from urllib import quote, unquote
from tornado import web
from base import BaseHandler

class yelp_redir(BaseHandler):
	_path = '/yelp/(.*)'

	def get(self, query):
		decoded_query = unquote(query)
		if '@' in decoded_query:
			desc, loc = decoded_query.split('@', 1)
			search = 'find_desc=%s&find_loc=%s' % (quote(desc.strip()), quote(loc.strip()))
		else:
			search = 'find_desc=%s' % quote(decoded_query.strip())

		self.redirect('http://www.yelp.com/search?%s' % search)

