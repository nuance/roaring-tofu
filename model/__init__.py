import sqlalchemy
import meta
from article import Article
from commit import Commit
from log_entry import LogEntry
from me import Me
from post import Post
from review import Review
from tweet import Tweet

def init_model(engine):
	"""Call me before using any of the tables or classes in the model."""

	meta.engine = engine

	session_maker = sqlalchemy.orm.sessionmaker(autoflush=True, autocommit=False, bind=engine)
	meta.session = sqlalchemy.orm.scoped_session(session_maker)

if __name__ == "__main__":
	# force all the tables to be created
	conn = sqlalchemy.create_engine('sqlite:///blog.sqlite', echo=True)
	init_model(conn)
	meta.metadata.create_all(conn)
