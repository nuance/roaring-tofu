MHJones
===========

Source code for mhjones.org. It's a pretty simple blog + some social stuff. Written with tornado + sqlite (via sqlalchemy orm... not happy about that choice, but it's not worth replacing).

Layout
------

 * app/ - various ways of running the site. I normally run standalone.py for development and deploy via wsgi
 * batch/ - add posts, import social stuff. Includes some very basic scrapers for grabbing content for a single user.
 * batch/importers/ - the aforementioned scrapers
 * handlers/ - controllers
 * model/ - the orm classes
 * static/(css|js|images) - static assets
 * templates/ - templates, all inheriting from base.thtml
 * ui/ - ui modules. All my css / js / rss includes happen via ui modules. Seems to work pretty well.
 * util/ - some utility code. linkification, relative timestamps etc.

Interesting bits
----------------

handlers/base.py - a base class & metaclass that lets you define handlers with their urls. For example:

     class Home(BaseHandler):
       _path = '/(\d*)'
       
       def get(self, offset):
         self.write('You requested /%s' % offset)

What doesn't quite work right
-----------------------------

* ui module https handling for external assets. The tornado ui module code explicitly checks for http (and not https) when including 3rd party js. So using https google analytics doesn't work quite right. This would be really easy to fix, but I'm not actually serving https for anything, so this doesn't really matter.
