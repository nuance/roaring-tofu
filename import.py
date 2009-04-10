from importers import ImportReviews, ImportRecentlyRead, ImportCommits, ImportTweets

if __name__ == "__main__":
	for batch in (ImportReviews, ImportRecentlyRead, ImportCommits, ImportTweets):
		b = batch()
		b.start()
