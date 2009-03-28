import datetime

from sqlalchemy import Table, Column, func, types
from sqlalchemy import orm
from sqlalchemy.sql import not_, select

import meta
import uri

t_tweet = Table("tweet", meta.metadata,
				Column("id", types.Integer, primary_key=True),
				Column("status_id", types.Integer, nullable=False),
				Column("user", types.String, nullable=False),
				Column("text", types.String, nullable=False),
				Column('time_created', types.DateTime, nullable=False))

class Tweet(object):
	def __init__(self, tweet_id, user, text, http_time_created):
		self.status_id = tweet_id
		self.text = text
		self.user = user.screen_name
		year = http_time_created[-4:]
		self.time_created = datetime.datetime.strptime(http_time_created[:-11] + " " + year, "%a %b %d %H:%M:%S %Y")

		self.id = None

	@property
	def link(self):
		return uri.Twitter.tweet_url(self.user, self.status_id)

	@classmethod
	def tweet_for_headline(cls):
		return meta.session.query(cls).filter(not_(cls.text.like("@%"))).order_by(cls.time_created.desc()).limit(1).all()[0]

orm.mapper(Tweet, t_tweet)
