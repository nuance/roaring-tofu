import twitter

from batch import Batch
from model import Tweet, meta

class ImportTweets(Batch):
	def arguments(self):
		self.opt_parser.add_option("-u", "--user", dest="user", default=None)
		self.opt_parser.add_option("-c", "--count", dest="count", default=100)

	def run(self):
		if not self.options.user:
			raise Exception("Need a user to load from!")

		api = twitter.Api()
		tweets = api.GetUserTimeline(self.options.user, count=self.options.count)

		for raw_tweet in tweets:
			tweet = Tweet(raw_tweet.id, raw_tweet.user, raw_tweet.text, raw_tweet.created_at)
			meta.session.add(tweet)

		meta.session.commit()

if __name__ == "__main__":
	batch = ImportTweets()
	batch.start()
