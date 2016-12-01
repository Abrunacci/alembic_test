# Standard Lib Imports

# Third-Party Imports

# CUSTOM Imports
from .models import ModelTwo
from ..config import session


class ModelTwoObject(object):
    """
    ModelTwo Object
    Parameters:
     description - String
    """

    def __init__(self, description=None):
        self.description = description

    def create(self):
        """ This function insert an 'ModelTwo' object in the database"""
        model_two = ModelTwo(description=self.description)
        session.add(model_two)
        session.commit()

    def list(self):
        """ This function lists all the 'ModelTwo' objects from the database"""
        objects = ", ".join([object.description
                             for object
                             in session.query(ModelTwo).all()])
        return objects
