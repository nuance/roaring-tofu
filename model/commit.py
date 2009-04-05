import datetime
import urllib2, urlparse

from sqlalchemy import Table, Column, func, types
from sqlalchemy import orm
from sqlalchemy.sql import not_, select

import meta
import uri

t_commit = Table("github_commit", meta.metadata,
				 Column("id", types.Integer, primary_key=True),
				 Column("cksum", types.String, nullable=False),
				 Column("project", types.String, nullable=False),
				 Column("message", types.String, nullable=False),
				 Column("url", types.String, nullable=False),
				 Column('time_authored', types.DateTime, nullable=False))

class Commit(object):
	def __init__(self, cksum, project, message, url, time_authored):
		self.cksum = cksum
		self.project = project
		self.message = message
		self.url = url
		self.time_authored = time_authored

	@classmethod
	def all_hashes(cls):
		return set(commit.cksum for commit in meta.session.query(cls).all())

	@classmethod
	def recent_commits(cls, number=3):
		query = meta.session.query(cls).group_by(cls.project).order_by(cls.time_authored.desc())
		return query.limit(number).all()

orm.mapper(Commit, t_commit)
