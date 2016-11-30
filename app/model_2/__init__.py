# Standard Lib Imports

# Third-Party Imports

# CUSTOM Imports
from .models import ModelTwo
from ..config import session


class ModelTwoObject(object):
    def __init__(self, description=None):
        self.description = description
    
    def create(self):
        model_one = ModelTwo(description=self.description)
        session.add(model_one)
        session.commit()
