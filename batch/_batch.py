"""
Generic batch framework
"""
from optparse import OptionParser
import logging

from sqlalchemy import create_engine

import config
from model import init_model

logging.basicConfig(level=logging.INFO)

class Batch(object):
	def __init__(self):
		self.engine = create_engine(config.engine_url, **config.engine_params)
		init_model(self.engine)

		self.log = logging.getLogger('batch.%s' % (self.__class__.__name__,))

		self.opt_parser = OptionParser()
		self.opt_parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False)
		self.arguments()
		
	def arguments(self):
		""" Override this to define additional command line arguments
		"""
		pass

	def run(self):
		raise Exception("You must override this")

	def start(self):
		(self.options, _) = self.opt_parser.parse_args()

		self.run()
