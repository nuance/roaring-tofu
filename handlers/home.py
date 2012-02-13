import operator

from handlers.base import BaseHandler
from model import Post, Article, Commit, Me, Review, Tweet, meta

class Home(BaseHandler):
    _path = '/(\d*)'

    def item_feed(self, limit, offset):
        blog_posts = Post.recent(offset+limit)
        articles = Article.recent(offset+limit)
        commits = Commit.recent(offset+limit)
        reviews = Review.recent(offset+limit)
        tweets = Tweet.recent(offset+limit)

        all_items = blog_posts + articles + commits + reviews + tweets
        sorted_items = sorted(all_items, key=operator.attrgetter('time_created'), reverse=True)
        items = sorted_items[offset:offset+limit]

        for pos, item in enumerate(items):
            item.pos = pos

        return items

    def get(self, offset):
        items = self.item_feed(25, 0)

        self.render('blog.thtml', items=items, me=Me())
