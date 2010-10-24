#!/usr/bin/env python
import logging

logging.basicConfig(level=logging.DEBUG)

from sqlalchemy import create_engine
from tornado import web, ioloop, httpserver

from base import BaseHandler
import blog, read
import config
from model import Post, init_model, meta
from yelp_redir import yelp_redir
import app_urls

log = logging.getLogger('roaringtofu')

class index(BaseHandler):
	def get(self, offset):
		count = meta.session.query(Post).count()

		if offset:
			offset = int(offset)
		else:
			offset = 0

		if offset > count:
			# temp redirect to home
			pass

		self.render_blog(post_count=count, offset=offset, rpp=5)

urls = [('/(\d*)', index)]
app_urls.urls.extend(urls)

log.info(app_urls.urls)
app = web.Application(app_urls.urls, **config.http_params)

read_conn = create_engine(config.engine_url, **config.engine_params)
init_model(read_conn)

if __name__ == "__main__":
	http_server = httpserver.HTTPServer(app)
	http_server.listen(8888)
	ioloop.IOLoop.instance().start()
