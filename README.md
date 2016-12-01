v1.0 Creating data structure
===

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

v2.0 Creating connection and models
===================================

We add the following code in 'model_1 / models.py' where we declare a class called 'ModelOne' that inherits from Base (now will fail, but we will deal with this later) and contains 3 columns:

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

Repeat the process on `model_2/models.py` changing `class ModelOne` for `class ModelTwo` and `__tablename__ = 'model_one'` for `__tablename__ = 'model_two'`

