import handlers.base

class LoginHandler(handlers.base.BaseHandler):
	path = '/login'

	def get(self):
		self.send_error(404)
