#!/usr/bin/env python
import logging

from sqlalchemy import create_engine
from tornado import web, ioloop, httpserver

import config
from model import init_model
import handlers

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('app.tornado')

app = web.Application(handlers.app_urls.urls, **config.http_params)

read_conn = create_engine(config.engine_url, **config.engine_params)
init_model(read_conn)

if __name__ == "__main__":
	http_server = httpserver.HTTPServer(app)
	http_server.listen(8888)
	
	log.info("Serving blog on http://127.0.0.1:8888")
	ioloop.IOLoop.instance().start()
