"""SQLAlchemy Metadata and Session object"""
from sqlalchemy import MetaData

__all__ = ['engine', 'metadata', 'session']

# SQLAlchemy database engine.  Updated by model.init_model().
engine = None

# SqlSoup interface
db = None

session = None

metadata = MetaData()
