# Standard Lib Imports

# Third-Party Imports

# CUSTOM Imports
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DB CONFIGURATION

DB_STRING = 'sqlite:///alembic_test.db'

engine = create_engine(DB_STRING)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
