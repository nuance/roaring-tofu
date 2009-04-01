import datetime

import twitter

from batch import Batch
from model import Article, meta

class ImportRecentlyRead(Batch):
	def run(self):
		current_articles = meta.session.query(Article).all()
		urls = set(a.url for a in current_articles)
		added = set()

		articles = open("RECENTLY-READ")
		for article_line in articles:
			if "][" not in article_line: continue
			url, title = article_line.rstrip()[2:-2].split("][", 1)
			if url in urls or url in added:
				continue

			article = Article(title, url)

			added.add(url)
			meta.session.add(article)

		meta.session.commit()
		print "Imported %d new articles" % len(added)

if __name__ == "__main__":
	batch = ImportRecentlyRead()
	batch.start()
