from src.session import Session, engine
from src.models.model import Base
from src.main import app
import json

class TestRoutes():
  def setup_method(self):
    Base.metadata.create_all(engine)
    self.session = Session()

  def test_create_route(self):
    with app.test_client() as test_client:
      response = test_client.get(
        '/health'
      )
      response_json = json.loads(response.data)
      assert response.status_code == 200
      assert 'status' in response_json

  def teardown_method(self):
    self.session.close()
    Base.metadata.drop_all(bind=engine)