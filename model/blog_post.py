import datetime

from sqlalchemy import Table, Column, func, types
from sqlalchemy import orm

from roaringtofu.model import meta

t_blog_post = Table("blog_post", meta.metadata,
					Column("id", types.Integer, primary_key=True),
					Column("title", types.String, nullable=False),
					Column("content", types.String, nullable=False),
					Column('time_created', types.DateTime, default=func.current_timestamp(), nullable=False),
					Column('time_modified', types.DateTime, default=None, nullable=True))

class BlogPost(object):
	def __init__(self, title, content):
		self.title = title
		self.content = content

	def __repr__(self):
		return "<BlogPost(title='%s', |content|=%d, updated=%r)" % (self.title, len(self.content), self.updated)

	@property
	def updated(self):
		return bool(self.time_modified)

	@property
	def date_created(self):
		return self.time_created.date().strftime("%D")

	@property
	def date_modified(self):
		return self.time_modified.date().strftime("%D")

orm.mapper(BlogPost, t_blog_post)
