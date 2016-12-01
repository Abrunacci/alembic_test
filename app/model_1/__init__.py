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