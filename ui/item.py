import tornado.web

class Item(tornado.web.UIModule):
	def render(self, item, el, id):
		return self.render_string('item.thtml', item=item, el=el, id=id)

