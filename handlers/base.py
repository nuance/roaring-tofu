import logging

from tornado import web

from model import Article, Commit, Post, Review, Tweet, meta
from util import render_mako
import app_urls

class RegisterableClass(type):
	def __new__(meta, classname, bases, class_dict):
		constructed = type.__new__(meta, classname, bases, class_dict)

		if constructed._path is not None:
			constructed.register()

		return constructed


class BaseHandler(web.RequestHandler):
	__metaclass__ = RegisterableClass
	_path = None

	def initialize(self):
		self.log = logging.getLogger('handlers.%s' % (self.__class__.__name__))

	@classmethod
	def register(cls):
		return app_urls.connect(cls._path, cls)

	def render_blog(self, posts=None, offset=0, post_count=1, rpp=5):
		if posts is None:
			posts = meta.session.query(Post).order_by(Post.time_created.desc()).limit(rpp).offset(offset).all()
		articles = Article.recent_articles()
		commits = Commit.recent_commits()
		reviews = Review.recent_reviews()
		tweet = Tweet.recent_tweet()

		prev = None
		if offset:
			prev = max(offset - rpp, 0)
		next = None
		if offset + rpp < post_count:
			next = min(post_count - 1, offset + rpp)

		self.set_header("Content-Type","text/html; charset=utf-8")
		self.write(render_mako('index.mako',
						   posts=posts,
						   recent_tweet=tweet,
						   commits=commits,
						   reviews=reviews,
						   articles=articles,
						   start=offset,
						   end=offset + len(posts),
						   prev=prev,
						   next=next,
						   total=post_count))