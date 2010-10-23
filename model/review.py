from sqlalchemy import Table, Column, func, types
from sqlalchemy import orm
from sqlalchemy.sql import not_, select

import meta

t_review = Table("yelp_review", meta.metadata,
				 Column("id", types.Integer, primary_key=True),
				 Column("business", types.String, nullable=False),
				 Column("rating", types.Integer, nullable=False),
				 Column("review_text", types.String, nullable=False),
				 Column("long", types.Float, nullable=False),
				 Column("lat", types.Float, nullable=False),
				 Column("url", types.String, nullable=False),
				 Column('time_authored', types.DateTime, nullable=False))

class Review(object):
	def __init__(self, business, rating, review_text, long, lat, url, time_authored):
		self.business = business
		self.rating = rating
		self.review_text = review_text
		self.long = long
		self.lat = lat
		self.url = url
		self.time_authored = time_authored

	@classmethod
	def all_urls(cls):
		return set(review.url for review in meta.session.query(cls).all())

	@classmethod
	def recent_reviews(cls, number=2):
		query = meta.session.query(cls).group_by(cls.business).order_by(cls.time_authored.desc())
		return query.limit(number).all()

	@property
	def stars_img(self):
		return "http://media1.px.yelpcdn.com/static/200911302843250757/i/ico/stars/stars_mobile_%d.gif" % self.rating

	@property
	def snippet(self):
		return self.review_text[:55] + "..."

orm.mapper(Review, t_review)
