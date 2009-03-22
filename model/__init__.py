import sqlalchemy
from roaringtofu.model import meta

from roaringtofu.model.blog_post import BlogPost
from roaringtofu.model.user import User

def init_model(engine):
	"""Call me before using any of the tables or classes in the model."""

	meta.engine = engine

	session_maker = sqlalchemy.orm.sessionmaker(autoflush=True, transactional=True, bind=engine)
	meta.session = sqlalchemy.orm.scoped_session(session_maker)
