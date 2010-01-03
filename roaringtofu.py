#!/usr/bin/env python
from sqlalchemy import create_engine
from tornado import web, ioloop, httpserver

import blog, read
import config
from model import Post, init_model, meta
from yelp_redir import yelp_redir
import app_urls

class index(web.RequestHandler):
	def get(self, offset):
		self.set_header("Content-Type","text/html; charset=utf-8")
		count = meta.session.query(Post).count()

		if offset:
			offset = int(offset)
		else:
			offset = 0

		if offset > count:
			# temp redirect to home
			pass

		posts = meta.session.query(Post).order_by(Post.time_created.desc()).limit(5).offset(offset).all()

		self.write(blog.render_blog(posts=posts, offset=offset, post_count=count, rpp=5))

urls = [('/(\d*)', index)]
		
app_urls.urls.extend(urls)
app = web.Application(app_urls.urls)

read_conn = create_engine(config.engine_url, **config.engine_params)
init_model(read_conn)

if __name__ == "__main__":
	http_server = httpserver.HTTPServer(app)
	http_server.listen(8888)
	ioloop.IOLoop.instance().start()
