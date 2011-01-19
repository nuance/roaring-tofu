import logging

from importers import ImportReviews, ImportRecentlyRead, ImportCommits, ImportTweets

logging.basicConfig()
log = logging.getLogger('import')

if __name__ == "__main__":
	for batch in (ImportReviews, ImportRecentlyRead, ImportCommits, ImportTweets):
		log.info("Running import for %s" % batch.__name__)
		try:
			b = batch()
			b.start()
		except Exception, e:
			log.exception('Batch %s failed' % batch.__name__)
