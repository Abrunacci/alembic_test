v2.0 Creating connection and models
===================================

We add the following code in `app/model_1 / models.py` where we declare a class called 'ModelOne' that inherits from Base (now will fail, but we will deal with this later) and contains 3 columns:

~~~
# Standard Lib Imports

# Third-Party Imports
from sqlalchemy import Column, String, Integer, Boolean

# CUSTOM Imports
from ..config import Base


class ModelOne(Base):
    __tablename__ = 'model_one'
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(256))
    enabled = Column(Boolean, default=True)
~~~

Repeat the process on `app/model_2/models.py` replacing lines 10 and 11 with:

~~~
# ...
class ModelOne(Base):
    __tablename__ = 'model_one'
# ...
~~~


Now we add the following code to `app/config.py` to start the database connection:

~~~
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

~~~

On this example we create a sqlite database, if you want to change that and create other database connection, change the connection string with some of [this](http://docs.sqlalchemy.org/en/latest/core/engines.html)