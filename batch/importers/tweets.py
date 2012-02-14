import datetime

import twitter

from batch import Batch
import config
from model import Tweet, meta

class ImportTweets(Batch):
	def arguments(self):
		self.opt_parser.add_option("-u", "--user", dest="user", default=config.twitter_user)
		self.opt_parser.add_option("-c", "--count", dest="count", default=100)

	def run(self):
		if not self.options.user:
			raise Exception("Need a user to load from!")

		last_tweet = Tweet.recent(show_replies=True)[0]

		api = twitter.Api()
		tweets = api.GetUserTimeline(self.options.user, count=self.options.count, since_id=last_tweet.status_id)
		added = set()

		for raw_tweet in tweets:
			tweet = Tweet(raw_tweet.id, raw_tweet.user, raw_tweet.text, raw_tweet.created_at)
			if last_tweet and (tweet.time_created < last_tweet.time_created or tweet.text == last_tweet.text):
				continue

			added.add(tweet)
			meta.session.add(tweet)

		meta.session.commit()
		if added:
			self.log.info("Imported %d new statuses" % len(added))

if __name__ == "__main__":
	batch = ImportTweets()
	batch.start()
