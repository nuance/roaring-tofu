import datetime
import os, os.path
import stat

import json
import markdown
import util.rst
from sqlalchemy import Table, Column, func, types
from sqlalchemy import orm

import config
import meta
from util import to_base37

t_old_post = Table("post", meta.metadata,
                   Column("id", types.Integer, primary_key=True),
                   Column("title", types.Unicode, nullable=False),
                   Column("name", types.Unicode, nullable=False),
                   Column("content", types.Unicode, nullable=False),
                   Column("file_name", types.Unicode, nullable=False),
                   Column('time_created', types.DateTime, default=func.current_timestamp(), nullable=False),
                   Column('time_modified', types.DateTime, default=None, nullable=True))

t_post = Table("md_post", meta.metadata,
			   Column("id", types.Integer, primary_key=True),
			   Column("title", types.Unicode, nullable=False),
			   Column("alias", types.Unicode, nullable=False),
			   Column("file_name", types.Unicode, nullable=False),
			   Column('time_created', types.DateTime, default=func.current_timestamp(), nullable=False),
			   Column('time_modified', types.DateTime, default=None, nullable=True))

class Post(object):
	def __init__(self, file_name):
		md = markdown.Markdown(extensions=['meta', 'codehilite'])
		md.convert(open(file_name).read())

		self.file_name = os.path.join(config.posts_path, file_name)
		self.title = md.Meta['title'][0]
		self.alias = to_base37(self.title)

		st = os.stat(self.file_name)
		self.time_created = datetime.datetime.fromtimestamp(st[stat.ST_MTIME])
		self.time_modified = datetime.datetime.fromtimestamp(st[stat.ST_MTIME])

	def __repr__(self):
		return "<Post(id=%d, title='%s', file_name='%s', updated=%r)>" % (self.id, self.title, self.file_name, self.updated)

	@property
	def updated(self):
		return self.time_modified != self.time_created

	@property
	def date_created(self):
		return self.time_created.date().strftime("%D")

	@property
	def date_modified(self):
		return self.time_modified.date().strftime("%D")

	@property
	def content(self):
		with open(self.file_name) as f:
			raw_content = f.read()

		return markdown.markdown(raw_content, extensions=['meta', 'codehilite'])

	@classmethod
	def by_alias(cls, alias):
		return meta.session.query(Post).filter(Post.alias == alias).all()

	@classmethod
	def list_posts(cls, limit=5, offset=0):
		return meta.session.query(Post).order_by(Post.time_created.desc()).limit(limit).offset(offset).all()


class OldPost(object):
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
		return self.time_modified != self.time_created

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
			return util.rst.html_body(unicode(content))
		except IOError:
			return ''

	@classmethod
	def list_posts(self, limit=5, offset=0):
		return meta.session.query(Post).order_by(Post.time_created.desc()).limit(limit).offset(offset).all()

orm.mapper(Post, t_post)
