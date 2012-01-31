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
from util import to_base_37, uri

t_log_entry = Table("log_entry", meta.metadata,
			   Column("id", types.Integer, primary_key=True),
			   Column("text", types.Unicode, nullable=False),
			   Column('time_created', types.DateTime, default=func.current_timestamp(), nullable=False),
			   Column('time_modified', types.DateTime, default=None, nullable=True))

class LogEntry(object):
	def __init__(self, text):
		self.text = text

	def __repr__(self):
		return "<LogEntry(id=%d, text='%s', created='%s', updated=%r)>" % (self.id, self.text, self.time_created)

	@property
	def jsonable(self):
		return {'id': self.id, 'text': self.text, 'completed': self.time_created.strftime("%s")}

	@classmethod
	def get(cls, entry_id):
		return meta.session.query(LogEntry).filter(LogEntry.id == entry_id).one()

	@classmethod
	def list(cls, limit, offset, tag=None):
		query = meta.session.query(LogEntry).order_by(LogEntry.time_created.desc())

		if tag:
			query = query.filter(LogEntry.text.contains('#' + tag))

		return query.limit(limit).offset(offset).all()


orm.mapper(LogEntry, t_log_entry)
