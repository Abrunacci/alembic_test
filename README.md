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

