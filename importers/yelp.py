import datetime
import re
import urllib2
from xml.etree import ElementTree

from batch import Batch
import config
from model import Review, meta

BIZ_NAME_RE = re.compile("^(?P<biz>.*) \(\d/\d\) on Yelp$")
RATING_RE = re.compile("\((?P<rating>\d)/\d\)")

class Yelp(object):
	@classmethod
	def load_reviews(cls, user_id):
		user_info = urllib2.urlopen("http://yelp.com/syndicate/user/%s/rss.xml" % user_id).read()
		user_rss = ElementTree.fromstring(user_info)

		xml_reviews = [item for item in user_rss[0] if item.tag == 'item']
		reviews = [[(c.tag, c.text) for c in xml_review] for xml_review in xml_reviews]

		return reviews


def _value_for_key(alist, key):
	for k, v in alist:
		if k == key: return v
	return None

class ImportReviews(Batch):
	def arguments(self):
		self.opt_parser.add_option("-u", "--user-id", dest="user_id", default=config.yelp_user)

	def run(self):
		if not self.options.user_id:
			raise Exception("Need a user to load from!")

		review_urls = Review.all_urls()
		rss_reviews = Yelp.load_reviews(self.options.user_id)
		added = []

		for review in rss_reviews:
			written = _value_for_key(review, 'pubDate')
			title = _value_for_key(review, 'title')
			link = _value_for_key(review, 'link')
			description = _value_for_key(review, 'description')
			geo_long = _value_for_key(review, '{http://www.w3.org/2003/01/geo/wgs84_pos#}long')
			geo_lat = _value_for_key(review, '{http://www.w3.org/2003/01/geo/wgs84_pos#}lat')

			if link in review_urls:
				continue
			else:
				added.append(review)

			business = BIZ_NAME_RE.search(title).groupdict()['biz']
			rating = int(RATING_RE.search(title).groupdict()['rating'])
			author_time = datetime.datetime.strptime(written, "%a, %d %b %Y %H:%M:%S  %Z")

			db_review = Review(business, rating, description, geo_long, geo_lat, link, author_time)
			meta.session.add(db_review)

		meta.session.commit()
		if added:
			print "Imported %d new reviews" % len(added)

if __name__ == "__main__":
	batch = ImportReviews()
	batch.start()
