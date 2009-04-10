import datetime
import re

from web.contrib.template import render_mako

render = render_mako(directories=['templates'], input_encoding='utf-8', output_encoding='utf-8', default_filters=['unicode', 'h'])

def render_mako(tmpl, *args, **kwargs):
	template = render._lookup.get_template(tmpl + ".mako")
	return template.render(*args, **kwargs)

def batch(fun):
	"""
	no-op for now, but this should signify functions that can only be ran in batch mode (eg from the command line)
	"""
	return fun


def relative_time(date): 
	now = datetime.datetime.now()
	diff = date.date() - now.date()

	if diff.days == 0:
		if diff.hours == 0:
			return "%d minute%s ago" % (abs(diff.minutes), "s" if diff.minutes < -1 else "")
		return "%d hour%s ago" % (abs(diff.hours), "s" if diff.hours < -1 else "")
	elif abs(diff.days) < 7:
		return "%d day%s ago" % (abs(diff.days), "s" if diff.days < -1 else "")
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
