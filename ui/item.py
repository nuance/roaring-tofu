import tornado.web

class Item(tornado.web.UIModule):
	def render(self, item, el, id, last_item=None):
		last_title = last_item.title if last_item else None
		return self.render_string('item.thtml', item=item, el=el, id=id, last_title=last_title)

