from batch.importers import ImportReviews, ImportRecentlyRead, ImportCommits, ImportTweets

if __name__ == "__main__":
	for batch in (ImportReviews, ImportRecentlyRead, ImportCommits, ImportTweets):
		self.log.info("Running import for %s" % batch.__name__)
		try:
			b = batch()
			b.start()
		except Exception, e:
			self.log.exception('Batch %s failed' % batch.__name__)
