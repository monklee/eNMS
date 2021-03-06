from .database import *

class CustomBase(Base):
    
    __abstract__ = True
    
    # simplifies the syntax for flask forms
    @classmethod
    def choices(cls):
        return [(obj, obj) for obj in cls.query.all()]
        
    def __repr__(self):
        return self.name
