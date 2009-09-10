from urllib import quote, unquote
import web

class yelp_redir(object):
	def GET(self, query):
		decoded_query = unquote(query)
		if '@' in decoded_query:
			desc, loc = decoded_query.split('@', 1)
			search = 'find_desc=%s&find_loc=%s' % (quote(search.strip()), quote(location.strip()))
		else:
			search = 'find_desc=%s' % quote(decoded_query.strip())

		raise web.seeother('http://www.yelp.com/search?%s' % search)
