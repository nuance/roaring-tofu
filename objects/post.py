import rst
from sqlalchemy import Table, Column, DateTime, Integer, String
from sqlalchemy.sql import func, and_

from util import batch, meta

posts = Table("post", meta,
			Column("id", Integer, primary_key=True),
			Column("title", String, nullable=False),
			Column("file_name", String, nullable=False),
			Column('time_created', DateTime, default=func.current_timestamp(), nullable=False),
			Column('time_modified', DateTime, default=None, nullable=True))

class Post(object):
	c = posts.c

	def __init__(self, id, title, file_name, date_created, date_modified):
		self.id = id
		self.title = title
		self.file_name = file_name
		self.date_created = date_created
		self.date_modified = date_modified

	@batch
	def commit(self):
		posts.insert().execute(id=self.id, title=self.title,
							   file_name=self.file_name,
							   date_created=self.date_created,
							   date_modified=self.date_modified)

	@classmethod
	def _select(cls, expr):
		result = posts.select(and_(*expr)).execute()
		row = result.fetchone()
		return [Post(row[posts.c.id], row[posts.c.title],
					 row[posts.c.file_name], row[posts.c.time_created],
					 row[posts.c.time_modified])]

	@classmethod
	def select_by_id(cls, id):
		expr = [cls.c.id == id]
		return cls._select(expr)

	@classmethod
	def select_by_range(cls, min_id, max_id):
		expr = [cls.c.id >= min_id, cls.c.id <= max_id]
		return cls._select(expr)

	@property
	def updated(self):
		return self.date_created != self.date_modified

	@property
	def body_html(self):
		try:
			content = open("blog-posts/%s" % self.file_name).readlines()
			return rst.html_body(unicode(self.content))
		except IOError:
			return ''
