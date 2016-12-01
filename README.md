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
[alembic_test] chmod a+x run.py
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
(alembic_test)[alembic_test] pip install -r requirements.txt
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
(alembic_test)[alembic_test] alembic init --template generic ./migrations
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

Then we add to `migrations/env.py` the following code on the line to set the PYTHONPATH:

~~~
# ...
import sys
import os
# ...


parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
sys.path.append(parent_dir)
# This is...

~~~

we import our Base right after the added code

~~~
parent_dir = os.path.abspath(os.path.join(os.getcwd(), "."))
sys.path.append(parent_dir)
from app.config import Base
~~~

and replace the line `target_metadata = None` with:
~~~
target_metadata = Base.metadata
~~~

v0.5 Ready to go...
===================

ok, we already installed the requirements, inserted the code, initiated alembic and configure it... What now?

Now we have to create the database, and that's one of the reasons we use alembic.

The first thing we have to do is generate the migrations file.

~~~
(alembic_test)[alembic_test] alembic revision --autogenerate -m "First migration"  
~~~

This command generates a revision file that detects if we have changes in the models comparing them with the existing database. If the database it's empty, all the created models are included on the revision. And if not, only generate the file with the model's modifications

If we check `migrations/versions/(hash)_first_migration.py` (the filename is generated with the argument settled on -m) we have this code:

~~~
"""First migration

Revision ID: <HASHED CODE>
Revises: 
Create Date: 2016-12-01 01:29:09.806471

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '<REVISION ID>'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model_one',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_model_one_id'), 'model_one', ['id'], unique=False)
    op.create_table('model_two',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_model_two_id'), 'model_two', ['id'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_model_two_id'), table_name='model_two')
    op.drop_table('model_two')
    op.drop_index(op.f('ix_model_one_id'), table_name='model_one')
    op.drop_table('model_one')
    ### end Alembic commands ###

~~~


Now we have to upgrade the database (in this case, with sqlite, if database doesn't exists, it's created)

~~~
(alembic_test)[alembic_test] alembic upgrade head
~~~

~~~
(alembic_test)[alembic_test] alembic upgrade head                                                                                                             master  ✭ ✱
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 6b924b946ceb, First migration

~~~


> NOTE: at this point I detect an error on v0.2, we have to add this on 'run.py':

>> ~~~
    # Standard Lib Imports
    import sys
    # ..
    value = sys.argv[1]
    ~~~

> and modify...  

>> ~~~
    if __name__ == '__main__':
    run(value=value)
    ~~~

>> sorry about this.

And we have the database created whit all the tables so if we run...
~~~
(alembic_test)[alembic_test] alembic upgrade head                                                                                                             master  ✭ ✱
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 6b924b946ceb, First migration

~~~