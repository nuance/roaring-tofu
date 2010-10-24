import datetime
import re
from mako.template import Template
from mako.lookup import TemplateLookup

template_lookup = TemplateLookup(directories=['templates'], module_directory='/tmp/mako_modules')

def render_mako(templatename, **kwargs):
    template = template_lookup.get_template(templatename)
    return template.render(**kwargs)

def batch(fun):
	"""
	no-op for now, but this should signify functions that can only be ran in batch mode (eg from the command line)
	"""
	return fun


def relative_time(date): 
	now = datetime.datetime.now()
	diff = now.date() - date.date()

	if diff.days == 0:
		hours = diff.seconds / 3600
		minutes = diff.seconds / 60
		if hours == 0:
			return "%d minute%s ago" % (abs(minutes), "s" if minutes != 1 else "")
		return "%d hour%s ago" % (abs(hours), "s" if hours != 1 else "")
	elif abs(diff.days) < 7:
		return "%d day%s ago" % (abs(diff.days), "s" if diff.days != 1 else "")
	elif abs(diff.days) < 28:
		return "%d week%s ago" % (abs(diff.days) / 7, "s" if (diff.days / 7) > 1 else "")
	else:
		return "on %s" % date.strftime("%B %e")

def _link(frmt, group=1):
	def _sub_fn(match):
		groups = dict((str(k), v) for k, v in enumerate(match.groups()))
		return frmt % groups
	return _sub_fn

def linkify_tweet(text):
	url_re = "(http?:\/\/\S+)"
	user_re = "(^|\s)@(\w+)"
	tag_re = "(^|\s)#(\w+)"

	text = re.sub(url_re, _link("<a rel=\"nofollow\" href=\"%(0)s\">%(0)s</a>"), text)
	text = re.sub(user_re, _link("<a rel=\"nofollow\" href=\"http://twitter.com/%(1)s\">@%(1)s</a>"), text)
	text = re.sub(tag_re, _link("<a rel=\"nofollow\" href=\"http://search.twitter.com/search?q=%(1)s\">#%(1)s</a>"), text)

	return text

base_37_re = re.compile('[^0123456789abcdefghijklmnopqrstuvwxyz]')
def to_base37(text, repl='-'):
	ltext = text.lower()
	return base_37_re.sub(repl, ltext)
