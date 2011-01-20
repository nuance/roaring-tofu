import datetime
import PyRSS2Gen

from handlers.base import BaseHandler
from model import Post, meta

FEED_SIZE = 20
class Rss(BaseHandler):
	_path = '/rss'

	def get(self):
		posts = meta.session.query(Post).order_by(Post.time_created.desc()).limit(FEED_SIZE).all()

		items = []
		for post in posts:
			item = PyRSS2Gen.RSSItem(title=post.title, link=post.url, description=post.content,
									 pubDate=post.date_created, guid=PyRSS2Gen.Guid(post.url))
			items.append(item)

		rss = PyRSS2Gen.RSS2(title="The Book of Jones",
							 link="http://mhjones.org",
							 description="Cooking, travel, and techno-babble",
							 lastBuildDate=datetime.datetime.utcnow(),
							 items=items)

		self.set_header("Content-Type", "text/xml")
		self.write(rss.to_xml())
