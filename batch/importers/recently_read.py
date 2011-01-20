import datetime
import json
import socket
import urlparse
import urllib2

from batch import Batch
import config
from model import Article, meta

class ImportRecentlyRead(Batch):
	def run(self):
		current_articles = meta.session.query(Article).all()
		urls = set(a.url for a in current_articles)
		added = set()

		try:
			pinboard_data = urllib2.urlopen(config.pinboard_json_feed).read()
		except IOError:
			self.log.exception("Problem reading data from pinboard")
			return

		articles = json.loads(pinboard_data)

		# set a low timeout before we look up favicons. we assume that
		# a reasonable server will response in < 5000 ms for a 404
		socket.setdefaulttimeout(5.0)
		favico_cache = {}

		for article in articles:
			url = article['u']
			title = article['d']

			if url in urls or url in added:
				continue

			hostname = urlparse.urlparse(url).hostname

			if hostname in favico_cache:
				has_favicon = favico_cache[hostname]
			else:
				# Try fetching the favicon
				try:
					urllib2.urlopen('http://' + hostname + '/favicon.ico').read()
					has_favicon = True
				except (urllib2.HTTPError, urllib2.URLError):
					has_favicon = False
				favico_cache[hostname] = has_favicon

			# '2011-01-18T17:33:19Z'
			time_added = datetime.datetime.strptime(article['dt'], '%Y-%m-%dT%H:%M:%SZ')

			article = Article(title, url, time_added, has_favicon)
			self.log.info("added %s => %s (at time %s)" % (title, url, time_added))

			added.add(url)
			meta.session.add(article)

		meta.session.commit()
		if added:
			self.log.info("Imported %d new articles" % len(added))

if __name__ == "__main__":
	batch = ImportRecentlyRead()
	batch.start()
