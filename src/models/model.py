from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Model():
  id = Column(Integer, primary_key=True)
  created_at = Column(DateTime)
  updated_at = Column(DateTime)

  def __init__(self):
    self.created_at = datetime.now()
    self.updated_at = datetime.now()