import datetime
import json
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

		for article in articles:
			url = article['u']
			title = article['d']
			# '2011-01-18T17:33:19Z'
			time_added = datetime.datetime.strptime(article['dt'], '%Y-%m-%dT%H:%M:%SZ')

			if url in urls or url in added:
				continue

			article = Article(title, url, time_added)
			self.log.info("added %s => %s (at time %s)" % (title, url, time_added))

			added.add(url)
			meta.session.add(article)

		meta.session.commit()
		if added:
			self.log.info("Imported %d new articles" % len(added))

if __name__ == "__main__":
	batch = ImportRecentlyRead()
	batch.start()
