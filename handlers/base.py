from tornado.options import logging
from tornado import web

from model import Article, Commit, Review, Tweet
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
