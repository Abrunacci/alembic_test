#! /usr/bin/env python

# Standard Lib Imports

# Third-Party Imports

# CUSTOM Imports
from .model_1 import ModelOne
from .model_2 import ModelTwo


def create_model_one(description=None):
    ModelOne(description=description).create()


def create_model_two(description=None):
    ModelTwo(description=description).create()
    

def run(value=None):
    if not value:
        return 'You must insert a value'
    try:
        for i in range(0, int(value)):
            description = "Object %s" % i
            if i % 2 == 0:
                create_model_two(description=description)
            else:
                create_model_one(description=description)
    except ValueError:
        return 'Value must be an Integer'