import tornado.web

import config

class GoogleAnalytics(tornado.web.UIModule):
	def render(self):
		return ''

	def javascript_files(self):
		if self.request.protocol == 'https':
			return ["https://ssl.google-analytics.com/ga.js"]
		else:
			return ["http://www.google-analytics.com/ga.js"]

	def embedded_javascript(self):
		return """try{
	      			var pageTracker = _gat._getTracker("UA-""" + config.ga_key + """");
	        		pageTracker._trackPageview();
	    			} catch(err) {}"""

