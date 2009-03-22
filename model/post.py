import rst
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
	def __init__(self, title, file_name):
		self.title = title
		self.file_name = file_name

		try:
			open("blog-posts/%s" % self.file_name)
		except IOError:
			raise Exception("No blog post file found for file name %s, cancelling add" % self.file_name)

	def __repr__(self):
		return "<Post(title='%s', |file_name|=%d, updated=%r)>" % (self.title, len(self.file_name), self.updated)

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
			content = open("blog-posts/%s" % self.file_name).readlines()
			return rst.html_body(unicode(self.content))
		except IOError:
			return ''

orm.mapper(Post, t_post)
