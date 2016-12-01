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