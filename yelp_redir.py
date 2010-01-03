from urllib import quote, unquote
from tornado import web
import app_urls

class yelp_redir(web.RequestHandler):
	def get(self, query):
		decoded_query = unquote(query)
		if '@' in decoded_query:
			desc, loc = decoded_query.split('@', 1)
			search = 'find_desc=%s&find_loc=%s' % (quote(desc.strip()), quote(loc.strip()))
		else:
			search = 'find_desc=%s' % quote(decoded_query.strip())

		self.redirect('http://www.yelp.com/search?%s' % search)


urls = [('/yelp/(.*)', yelp_redir)]
app_urls.urls.extend(urls)
