import tornado.web

import config

class Mixpanel(tornado.web.UIModule):
	def render(self):
		return ''

	def javascript_files(self):
		if self.request.protocol == 'https':
			return ["https://api.mixpanel.com/site_media/js/api/mixpanel.js"]
		else:
			return ["http://api.mixpanel.com/site_media/js/api/mixpanel.js"]

	def embedded_javascript(self):
		return """try {
          var mpmetrics = new MixpanelLib('""" + config.mixpanel_key + """');
        } catch(err) {
		  null_fn = function () {};
          var mpmetrics = {
            track: null_fn,
		    track_funnel: null_fn,
            register: null_fn,
            register_once: null_fn,
            register_funnel: null_fn };
        }"""
