from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect
from .session import engine
from .models.model import Base
from .routes.health_routes import health_routes
from .errors.errors import ApiError

app = Flask(__name__)
app.register_blueprint(health_routes)

Base.metadata.create_all(engine)

@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
      "mssg": err.description 
    }
    return jsonify(response), err.code

csrf = CSRFProtect()
csrf.init_app(app)