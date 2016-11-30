# Standard Lib Imports

# Third-Party Imports

# CUSTOM Imports
from .models import ModelOne
from ..config import session


class ModelOneObject(object):
    def __init__(self, description=None):
        self.description = description
    
    def create(self):
        model_one = ModelOne(description=self.description)
        session.add(model_one)
        session.commit()
