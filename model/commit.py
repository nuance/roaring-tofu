from sqlalchemy import Table, Column, types
from sqlalchemy import orm

from sqlalchemy import func, sql

import meta

t_commit = Table("github_commit", meta.metadata,
				 Column("id", types.Integer, primary_key=True),
				 Column("cksum", types.Unicode, nullable=False),
				 Column("project", types.Unicode, nullable=False),
				 Column("message", types.Unicode, nullable=False),
				 Column("url", types.Unicode, nullable=False),
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

	icon = 'C'

	@property
	def title(self):
		return self.project

	@property
	def content(self):
		return self.message

	@property
	def time_created(self):
		return self.time_authored

	@classmethod
	def recent(cls, number=3):
		last_commits = meta.session.query(cls.project, func.max(cls.time_authored)).group_by(cls.project).order_by(func.max(cls.time_authored).desc()).limit(number).all()

		commits = []
		for project, time_authored in last_commits:
			commits.extend(meta.session.query(cls).filter(sql.and_(cls.time_authored == time_authored, cls.project == project)).limit(1).all())

		return commits

	def __repr__(self):
		return "Commit(%r, %r, %r, %r, %r)" % (self.cksum, self.project, self.message, self.url, self.time_authored)

orm.mapper(Commit, t_commit)
