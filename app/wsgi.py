#!/usr/bin/env python
import wsgi_environ

import logging
import wsgiref

from sqlalchemy import create_engine
import tornado.wsgi

import config
from model import init_model
import handlers

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('app.wsgi')

application = tornado.wsgi.WSGIApplication(handlers.app_urls.urls, **config.http_params)

read_conn = create_engine(config.engine_url, **config.engine_params)
init_model(read_conn)

if __name__ == "__main__":
	wsgiref.handlers.CGIHandler().run(application)
