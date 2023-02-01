from src.commands.signup_user import SignupUser
from src.session import Session, engine
from src.models.model import Base
from src.models.user import User
from src.errors.errors import UserAlreadyExists, InvalidParams
from datetime import datetime
from sqlalchemy.orm import close_all_sessions


class TestSignupUser():
  USER_NAME = "William"
  USER_EMAIL = "wr.ravelo@uniandes.edu.co"
  USER_CITY = "Bogotá"
  USER_PHONE = "12312412"
  USER_PASSWORD = "123456"
  BASE_PATH = '/users'

  def setup_method(self):
    Base.metadata.create_all(engine)
    self.session = Session()

  def test_create_user_missing_fields(self):
    try:
      SignupUser({}).execute()

      assert False
    except InvalidParams:
      users = self.session.query(User).all()
      assert len(users) == 0

  def test_create_existing_email(self):
    first_data = {
      'name': self.USER_NAME,
      'email': self.USER_EMAIL,
      'birth_day': datetime.now().date().isoformat(),
      'city': self.USER_CITY,
      'phone': self.USER_PHONE,
      'password': self.USER_PASSWORD
    }
    SignupUser(first_data).execute()

    try:
      second_data = {
        'name': 'Otro',
        'email': self.USER_EMAIL,
        'birth_day': datetime.now().date().isoformat(),
        'city': 'Medellin',
        'phone': '5432432',
        'password': '654321'
      }

      SignupUser(second_data).execute()

      assert False
    except UserAlreadyExists:
      users = self.session.query(User).all()
      assert len(users) == 1

  def test_create_user(self):
    data = {
      'name': self.USER_NAME,
      'email': self.USER_EMAIL,
      'birth_day': datetime.now().date().isoformat(),
      'city': self.USER_CITY,
      'phone': self.USER_PHONE,
      'password': self.USER_PASSWORD
    }
    user = SignupUser(data).execute()

    assert user['email'] == data['email']
    assert user['name'] == data['name']

    users = self.session.query(User).all()
    assert len(users) == 1
  
  def teardown_method(self):
    self.session.close()
    Base.metadata.drop_all(bind=engine)