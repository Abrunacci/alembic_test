#! /usr/bin/env python

# Standard Lib Imports

# Third-Party Imports

# CUSTOM Imports
from .model_1 import ModelOneObject
from .model_2 import ModelTwoObject


def create_model_one_object(description=None):
    ModelOneObject(description=description).create()


def create_model_two_object(description=None):
    ModelTwoObject(description=description).create()
    

def run(value=None):
    if not value:
        return 'You must insert a value'
    try:
        for i in range(0, int(value)):
            description = "Object %s" % i
            if i % 2 == 0:
                create_model_two_object(description=description)
            else:
                create_model_one_object(description=description)
    except ValueError:
        return 'Value must be an Integer'