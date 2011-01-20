import tornado.web

class DisqusComments(tornado.web.UIModule):
	def render(self, post):
		return """<div id="disqus_thread">
	  </div>
	  <noscript>
		<a href="http://thebookofjones.disqus.com/?url=ref">
		  View the discussion thread.
		</a>
	  </noscript>
	  <a href="http://disqus.com" class="dsq-brlink">
		blog comments powered by <span class="logo-disqus">Disqus</span>
	  </a>"""	

	def embedded_javascript(self):
		return """(function() {
				var links = document.getElementsByTagName('a');
				var query = '?';
				for(var i = 0; i < links.length; i++) {
					if(links[i].href.indexOf('#disqus_thread') >= 0) {
						query += 'url' + i + '=' + encodeURIComponent(links[i].href) + '&';
					}
				}
				document.write('<script charset="utf-8" type="text/javascript" src="http://disqus.com/forums/thebookofjones/get_num_replies.js' + query + '"></' + 'script>');
			})();"""

	def javascript_files(self):
		return ["http://disqus.com/forums/thebookofjones/embed.js"]


class DisqusSlug(tornado.web.UIModule):
	def render(self, post):
		return """<a href=\"""" + post.url + """#disqus_thread">View Comments</a>"""

	def embedded_javascript(self):
		return """(function() {
				var links = document.getElementsByTagName('a');
				var query = '?';
				for(var i = 0; i < links.length; i++) {
					if(links[i].href.indexOf('#disqus_thread') >= 0) {
						query += 'url' + i + '=' + encodeURIComponent(links[i].href) + '&';
					}
				}
				document.write('<script charset="utf-8" type="text/javascript" src="http://disqus.com/forums/thebookofjones/get_num_replies.js' + query + '"></' + 'script>');
			})();"""

