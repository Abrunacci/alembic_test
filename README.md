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


