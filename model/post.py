import rst
from sqlalchemy import Table, Column, func, types
from sqlalchemy import orm

import meta

t_post = Table("post", meta.metadata,
			   Column("id", types.Integer, primary_key=True),
			   Column("title", types.String, nullable=False),
			   Column("name", types.String, nullable=False),
			   Column("content", types.String, nullable=False),
			   Column("file_name", types.String, nullable=False),
			   Column('time_created', types.DateTime, default=func.current_timestamp(), nullable=False),
			   Column('time_modified', types.DateTime, default=None, nullable=True))

class Post(object):
	def __init__(self, title, file_name, name=None, time_created=None, time_modified=None):
		self.title = title
		self.file_name = file_name

		self.name = name
		self.time_created = time_created
		self.time_modified = time_modified
		self.id = None

		try:
			open("blog-posts/%s" % self.file_name)
		except IOError:
			raise Exception("No blog post file found for file name %s, cancelling add" % self.file_name)

		self.content = self.body_html

	def __repr__(self):
		return "<Post(id=%d, title='%s', |file_name|=%d, updated=%r)>" % (self.id, self.title, len(self.file_name), self.updated)

	@property
	def updated(self):
		return bool(self.time_modified)

	@property
	def date_created(self):
		return self.time_created.date().strftime("%D")

	@property
	def date_modified(self):
		return self.time_modified.date().strftime("%D")

	@property
	def body_html(self):
		try:
			content = open("blog-posts/%s" % self.file_name).read()
			return rst.html_body(unicode(content))
		except IOError:
			return ''

orm.mapper(Post, t_post)
