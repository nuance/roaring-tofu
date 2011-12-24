from tornado import web

from handlers.base import BaseHandler
import config

class Resume(BaseHandler):
	"""Resume viewer."""

	_path = '/resume/(.+)'

	def get(self, source):
		if source not in config.resume_sources:
			raise web.HTTPError(404)

		self.set_header("Content-Type", "application/pdf")

		with open(config.resume_path, 'rb') as resume:
			self.write(resume.read())
