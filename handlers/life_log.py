from tornado import web

from model import meta, LogEntry
from handlers.base import BaseHandler

class LifeLog(BaseHandler):
	"""Life log servlet"""
	_path = '/log'

	@web.authenticated
	def get(self):
		offset = int(self.get_argument('start', '0'))

		self.write({'entries': [entry.jsonable for entry in LogEntry.list(10, offset)]})

	@web.authenticated
	def post(self):
		text = self.get_argument('entry')

		try:
			entry = LogEntry(text)
			meta.session.add(entry)
			meta.session.commit()
		except:
			meta.session.rollback()
			raise

		self.redirect('/log/%d' % entry.id)


class LifeLogTag(BaseHandler):
	"""Life log tag"""
	_path = '/log/([a-z]+)'

	@web.authenticated
	def get(self, tag):
		offset = int(self.get_argument('start', '0'))

		self.write({'entries': [entry.jsonable for entry in LogEntry.list(10, offset, tag=tag)]})


class LifeLogEntry(BaseHandler):
	"""Life log entry"""
	_path = '/log/([0-9]+)'

	@web.authenticated
	def get(self, entry_id):
		entry_id = int(entry_id)

		entry = LogEntry.get(entry_id)

		if not entry:
			self.send_error(404)

		self.write(entry.jsonable)
