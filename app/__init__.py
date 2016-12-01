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
