from tornado import web

from model import meta, LogEntry
from handlers.base import BaseHandler

class LifeLog(BaseHandler):
	"""Life log servlet"""
	_path = '/log'

	def get(self):
		offset = int(self.get_argument('start', '0'))

		self.write({'entries': [entry.jsonable for entry in LogEntry.list(10, offset)]})

	def post(self):
		text = self.get_argument('entry')

		entry = LogEntry(text)
		meta.session.add(entry)
		meta.session.commit()

		self.redirect('/log/%d' % entry.id)


class LifeLogTag(BaseHandler):
	"""Life log tag"""
	_path = '/log/([a-z]+)'

	def get(self, tag):
		offset = int(self.get_argument('start', '0'))

		self.write({'entries': [entry.jsonable for entry in LogEntry.list(10, offset, tag=tag)]})


class LifeLogEntry(BaseHandler):
	"""Life log entry"""
	_path = '/log/([0-9]+)'

	def get(self, entry_id):
		entry_id = int(entry_id)

		entry = LogEntry.get(entry_id)

		if not entry:
			self.send_error(404)

		self.write(entry.jsonable)
