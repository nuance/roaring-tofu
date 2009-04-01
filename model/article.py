import datetime

from sqlalchemy import Table, Column, func, types
from sqlalchemy import orm
from sqlalchemy.sql import not_, select

import meta
import uri

t_article = Table("article", meta.metadata,
				  Column("id", types.Integer, primary_key=True),
				  Column("title", types.String, nullable=False),
				  Column("url", types.String, nullable=False),
				  Column('time_added', types.DateTime, nullable=False))

class Article(object):
	def __init__(self, title, url, time_added=None):
		self.title = title
		self.url = url
		if time_added:
			self.time_added = time_added
		else:
			self.time_added = datetime.datetime.now()

		self.id = None

	@property
	def link(self):
		return uri.a(self.url, self.title)

	@classmethod
	def recent_articles(cls, number=5):
		query = meta.session.query(cls).order_by(cls.time_added.desc())
		return query.limit(number).all()

orm.mapper(Article, t_article)
