v0.1 Creating data structure
============================

First we create the data structure as follows:

~~~
.
├── app
│   ├── config.py
│   ├── __init__.py
│   ├── model_1
│   │   ├── __init__.py
│   │   └── models.py
│   └── model_2
│       ├── __init__.py
│       └── models.py
├── README.md
├── requirements.txt
└── run.py
~~~

Then we set `run.py` as executable with:

~~~
$ chmod a+x run.py
~~~

Create the virtualenv:

~~~
$ mkvirtualenv -p $(which python3) alembic_test
~~~

and install the requirements.

this is the requirements.txt content:

~~~
Mako==1.0.6
MarkupSafe==0.23
SQLAlchemy==1.1.2
alembic==0.8.8
psycopg2==2.6.2
python-editor==1.0.3
~~~

we install it executing...

~~~
(alembic_test)$ pip install -r requirements.txt
~~~

v0.2 Creating connection and models
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


v0.3 Doing some stuff with data
===============================

We add the following code in `app/model_1 / __init__.py` where we declare a class called 'ModelOneObject'.

This class is simple, the `__init__()` receives one argument called description, this is used in `create()` 

~~~
# Standard Lib Imports

# Third-Party Imports

# CUSTOM Imports
from .models import ModelOne
from ..config import session


class ModelOneObject(object):
    """
    ModelOne Object
    Parameters:
     description - String
    """
    def __init__(self, description=None):
        self.description = description
    
    def create(self):
        """ This function insert an 'ModelOne' object in the database"""
        model_one = ModelOne(description=self.description)
        session.add(model_one)
        session.commit()
    
    def list(self):
        """ This function lists all the 'ModelOne' objects from the database"""
        objects = ", ".join([object.description
                             for object
                             in session.query(ModelOne).all()])
        return objects
~~~

we duplicate this code on `app/model_2/__init__.py` but replacing all the ModelOne references with ModelTwo (and changing the class name to 'ModelTwoObject').

Now we create the `app/__init__.py` file with this code:

~~~
#! /usr/bin/env python

# Standard Lib Imports

# Third-Party Imports

# CUSTOM Imports
from .model_1 import ModelOneObject
from .model_2 import ModelTwoObject


def create_model_one_object(description=None):
    """
    This method execute the 'create' method from ModelOneObject class.
    Parameters:
        description - String
    """
    ModelOneObject(description=description).create()


def create_model_two_object(description=None):
    """
    This method execute the 'create' method from ModelTwoObject class.
    Parameters:
        description - String
    """
    ModelTwoObject(description=description).create()


def run(value=None):
    '''
    This method execute the create functions and then list the results
    Parameters:
        value - Integer
    '''
    if not value:
        print('You must insert a value')
    try:
        print('Creating %s objects. Please, wait...' % value)
        for i in range(0, int(value)):
            description = "Object %s" % i
            if i % 2 == 0:
                create_model_two_object(description=description)
            else:
                create_model_one_object(description=description)
        print('Creationg finished.')
        print('Model 1 Objects: %s' % ModelOneObject().list())
        print('Model 2 Objects: %s' % ModelTwoObject().list())
    except ValueError:
        print('Value must be an Integer')
~~~

And finally, we add this code on `run.py`
 
~~~
#! /usr/bin/env python

# Standard Lib Imports

# Third-Party Imports

# CUSTOM Imports
from app import run


if __name__ == '__main__':
    run()

~~~


v0.4 Configuring Alembic
========================

This process is really simple and fast... said nobody ever. But! we are here to make it fast.

First we start 'alembic' by executing this command in the root folder of our project

~~~
(alembic_test) $ alembic init --template generic ./migrations
~~~

This process will generate the necessary configuration files and folders so that alembic can be executed

~~~
(alembic_test)[alembic_test] alembic init --template generic ./migrations                                                                                         master 
  Creating directory /home/ale/Develops/tests/alembic_test/migrations ... done
  Creating directory /home/ale/Develops/tests/alembic_test/migrations/versions ... done
  Generating /home/ale/Develops/tests/alembic_test/alembic.ini ... done
  Generating /home/ale/Develops/tests/alembic_test/migrations/README ... done
  Generating /home/ale/Develops/tests/alembic_test/migrations/script.py.mako ... done
  Generating /home/ale/Develops/tests/alembic_test/migrations/env.py ... done
  Please edit configuration/connection/logging settings in '/home/ale/Develops/tests/alembic_test/alembic.ini' before proceeding.                                                                                                        
~~~

This is our proyect now
~~~
.
├── alembic.ini
├── app
│   ├── config.py
│   ├── __init__.py
│   ├── model_1
│   │   ├── __init__.py
│   │   └── models.py
│   └── model_2
│       ├── __init__.py
│       └── models.py
├── migrations
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
├── README.md
├── requirements.txt
└── run.py
~~~

Now we have to configure it.

First we edit the line 32 on `alembic.ini` setting our connection string (same that we set on `app/config.py` but without quotation marks)

~~~
sqlalchemy.url = sqlite:///alembic_test.db
~~~

Then we add to `migrations/env.py` the following code on the line:

