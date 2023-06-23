#!/usr/bin/env python3

from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

# updated the above code to use delcaritve_base() from sqlalchem.orm 
# the orignal code generates the warning:
#  
# from sqlalchemy import (Column, String, Integer)
# from sqlalchemy.ext.declarative import declarative_base 
# 
# changing the above, removing the parenthese around Column, String, Intger and updating 
# from to sqlalchemy.orm import to the delcarative_base will clear this warning: 
# lib/models.py:6
#   /home/tgart/Development/code/phase-3/python-p3-translating-from-orms-to-sqlalchemy-lab/lib/models.py:6: MovedIn20Warning: Deprecated API features detected! These feature(s) are not compatible with SQLAlchemy 2.0. To prevent incompatible upgrades prior to updating applications, ensure requirements files are pinned to "sqlalchemy<2.0". Set environment variable SQLALCHEMY_WARN_20=1 to show all deprecation warnings.  Set environment variable SQLALCHEMY_SILENCE_UBER_WARNING=1 to silence this message. (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
#     Base = declarative_base()
# -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())