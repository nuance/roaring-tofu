# Namespace for app urls
urls = []

def connect(path, handler):
	print '%s => %s' % (path, handler.__name__)
	urls.append((path, handler))
