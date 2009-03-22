from sqlalchemy import create_engine, MetaData, Table, Integer, String, DateTime, Column	
from sqlalchemy.sql import func
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

read_conn = create_engine('sqlite:///blog.sqlite', echo=True)
meta = MetaData(read_conn)

if __name__ == "__main__":
	# force all the tables to be created
	posts = Table("post", meta,
				Column("id", Integer, primary_key=True),
				Column("title", String, nullable=False),
				Column("file_name", String, nullable=False),
				Column('time_created', DateTime, default=func.current_timestamp(), nullable=False),
				Column('time_modified', DateTime, default=None, nullable=True))

	meta.create_all(bind=read_conn)
