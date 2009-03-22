import sqlalchemy
import meta
from post import Post

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
