#!/usr/bin/env python
import site
site.addsitedir('/srv/www/domains/mhjones.org')
site.addsitedir('/srv/www/domains/mhjones.org/virtualenv/lib/python2.6/site-packages')

import logging
import wsgiref

from sqlalchemy import create_engine
import tornado.wsgi

import config
from model import init_model
import handlers

logging.basicConfig(filename=config.app_log, level=logging.INFO)
log = logging.getLogger('app.wsgi')

application = tornado.wsgi.WSGIApplication(handlers.app_urls.urls, **config.http_params)

read_conn = create_engine(config.engine_url, **config.engine_params)
init_model(read_conn)

if __name__ == "__main__":
	wsgiref.handlers.CGIHandler().run(application)
