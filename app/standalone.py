#!/usr/bin/env python
import os.path

from sqlalchemy import create_engine
from tornado import web, ioloop, httpserver, options

import site

site.addsitedir(os.path.dirname(os.path.dirname(__file__)))

import config
from model import init_model
import handlers

log = options.logging.getLogger('app.tornado')
app = web.Application(handlers.app_urls.urls, **config.http_params)

read_conn = create_engine(config.engine_url, **config.engine_params)
init_model(read_conn)

options.define("port", default=8888, help="run on the given port", type=int)

if __name__ == "__main__":
    options.parse_command_line()

    http_server = httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(options.options.port)

    log.info("Serving blog on http://127.0.0.1:%d" % options.options.port)
    ioloop.IOLoop.instance().start()
