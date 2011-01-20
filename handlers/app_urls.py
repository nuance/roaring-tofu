import logging

# Namespace for app urls
urls = []
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('app_urls')

def connect(path, handler):
	log.info('Connecting %s => %s' % (path, handler.__name__))
	urls.append((path, handler))
