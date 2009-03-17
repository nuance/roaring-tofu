import web

import rst
from util import render_mako
import uri

urls = ('/view/(\d+)', 'view_post')

app_blog = web.application(urls, globals())

class Post(object):
	def __init__(self, id, title, content, date_created, date_modified):
		self.id = id
		self.title = title
		self.content = content
		self.date_created = date_created
		self.date_modified = date_modified

	@property
	def updated(self):
		return self.date_created != self.date_modified

	@property
	def body_html(self):
		return rst.html_body(unicode(self.content))

class Blog(object):
	"""
	Blog logic / data methods
	"""
	@classmethod
	def load_posts(cls, start=0, limit=5):
		post = Post(1, "Test", "test post", 0, 0)
		return [post]

	@classmethod
	def load_post(cls, id=0):
		post = Post(id, "Test %d" % id, "* test post\n* test post", 0, 0)
		return post

class view_post(object):
	"""
	Blog servlet
	"""
	def GET(self, id):
		post = Blog.load_post(int(id))
		recent_tweet = "foo"
		commits = []
		reviews = []
		articles = []

		return render_mako('index', posts=[post], recent_tweet=recent_tweet, commits=commits, reviews=reviews, articles=articles)
