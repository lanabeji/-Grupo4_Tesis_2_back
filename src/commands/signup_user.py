from .base_command import BaseCommannd
from ..models.user import User, UserSchema, UserJsonSchema
from ..session import Session
from ..errors.errors import InvalidParams, UserAlreadyExists
from datetime import datetime

class SignupUser(BaseCommannd):
  def __init__(self, data):
    self.data = data
    if 'birth_day' in data:
      self.data['birth_day'] = str(datetime.strptime(data['birth_day'], "%Y-%m-%d"))
  
  def execute(self):
    session = Session()
    try:
      posted_user = UserSchema(
        only=('name', 'email', 'birth_day', 'city', 'phone', 'password')
      ).load(self.data)
      user = User(**posted_user)

      if self.email_exist(session, self.data['email']):
        session.close()
        raise UserAlreadyExists()

      session.add(user)
      session.commit()

      new_user = UserJsonSchema().dump(user)
      session.close()

      return new_user
    except TypeError:
      raise InvalidParams()
    except Exception as error:
      session.close()
      raise error

  def email_exist(self, session, email):
    return len(session.query(User).filter_by(email=email).all()) > 0