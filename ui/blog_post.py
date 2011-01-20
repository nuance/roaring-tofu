import tornado.web

class BlogPost(tornado.web.UIModule):
	def css_files(self):
		return ["css/blog_post.css"]

	def render(self, post, single_post=False):
		return self.render_string('blog_post.thtml', post=post, single_post=single_post)

