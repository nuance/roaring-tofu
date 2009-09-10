from urllib import quote, unquote
import web

class yelp_redir(object):
	def GET(self, query):
		decoded_query = unquote(query)
		search, location = decoded_query.split('@', 1)

		raise web.seeother('yelp.com/search?find_desc=%s&find_loc=%s' % (quote(search), quote(location)))
