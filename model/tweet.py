import datetime

from sqlalchemy import Table, Column, func, types
from sqlalchemy import orm
from sqlalchemy.sql import not_, select

import meta
import util
import util.uri

t_tweet = Table("tweet", meta.metadata,
				Column("id", types.Integer, primary_key=True),
				Column("status_id", types.Integer, nullable=False),
				Column("user", types.Unicode, nullable=False),
				Column("text", types.Unicode, nullable=False),
				Column('time_created', types.DateTime, nullable=False))

class Tweet(object):
	title = 'tweet'
	icon = '@'

	def __init__(self, tweet_id, user, text, http_time_created):
		self.status_id = tweet_id
		self.text = text
		self.user = user.screen_name
		year = http_time_created[-4:]
		self.time_created = datetime.datetime.strptime(http_time_created[:-11] + " " + year, "%a %b %d %H:%M:%S %Y")

		self.id = None

	@property
	def url(self):
		return util.uri.Twitter.tweet_url(self.user, self.status_id)

	@classmethod
	def recent(cls, count=1, show_replies=False):
		query = meta.session.query(cls).order_by(cls.time_created.desc())
		if not show_replies:
			query = query.filter(not_(cls.text.like("@%")))
		return query.limit(count).all()

	@property
	def content(self):
		return util.linkify_tweet(self.text)


orm.mapper(Tweet, t_tweet)
