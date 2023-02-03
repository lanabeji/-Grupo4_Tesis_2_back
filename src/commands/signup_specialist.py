from .base_command import BaseCommannd
from ..models.specialist import Specialist, SpecialistSchema, SpecialistJsonSchema
from ..session import Session
from ..errors.errors import InvalidParams, SpecialistAlreadyExists
from datetime import datetime

class SignupSpecialist(BaseCommannd):
  def __init__(self, data):
    self.data = data
    if 'birth_day' in data:
      self.data['birth_day'] = str(datetime.strptime(data['birth_day'], "%Y-%m-%d"))
  
  def execute(self):
    session = Session()
    try:
      posted_specialist = SpecialistSchema(
        only=('name', 'email', 'birth_day', 'city', 'phone', 'password', 'specialty')
      ).load(self.data)
      user = Specialist(**posted_specialist)

      if self.email_exist(session, self.data['email']):
        session.close()
        raise SpecialistAlreadyExists()

      session.add(user)
      session.commit()

      new_user = SpecialistJsonSchema().dump(user)
      session.close()

      return new_user
    except TypeError:
      raise InvalidParams()
    except Exception as error:
      session.close()
      raise error

  def email_exist(self, session, email):
    return len(session.query(Specialist).filter_by(email=email).all()) > 0