from sqlalchemy import Table, Column, func, types
from sqlalchemy import orm

import meta

t_post = Table("post", meta.metadata,
			   Column("id", types.Integer, primary_key=True),
			   Column("title", types.String, nullable=False),
			   Column("file_name", types.String, nullable=False),
			   Column('time_created', types.DateTime, default=func.current_timestamp(), nullable=False),
			   Column('time_modified', types.DateTime, default=None, nullable=True))

class Post(object):
	def __init__(self, title, content):
		self.title = title
		self.content = content

	def __repr__(self):
		return "<Post(title='%s', |content|=%d, updated=%r)>" % (self.title, len(self.content), self.updated)

	@property
	def updated(self):
		return bool(self.time_modified)

	@property
	def date_created(self):
		return self.time_created.date().strftime("%D")

	@property
	def date_modified(self):
		return self.time_modified.date().strftime("%D")

orm.mapper(Post, t_post)
