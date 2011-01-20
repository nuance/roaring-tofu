import datetime
import urlparse

from sqlalchemy import Table, Column, types
from sqlalchemy import orm

import meta
import util.uri

t_article = Table("article", meta.metadata,
				  Column("id", types.Integer, primary_key=True),
				  Column("title", types.Unicode, nullable=False),
				  Column("url", types.Unicode, nullable=False),
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
		return util.uri.a(self.url, self.title)

	@property
	def domain(self):
		hostname = urlparse.urlparse(self.url).hostname

		if hostname.startswith('www.'):
			return hostname[4:]
		return hostname		

	@property
	def favicon(self):
		return "http://" + urlparse.urlparse(self.url).hostname + "/favicon.ico"

	@classmethod
	def recent_articles(cls, number=5):
		query = meta.session.query(cls).order_by(cls.time_added.desc())
		return query.limit(number).all()


orm.mapper(Article, t_article)
