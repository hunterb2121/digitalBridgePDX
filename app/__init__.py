from flask import Flask
from flask_session import Session
from flask_login import LoginManager
import redis

from app.routes import register_blueprints


def create_app():
    app = Flask(__name__)

    app.config["SESSION_TYPE"] = "redis"
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_USE_SIGNER"] = True
    app.config["SESSION_KEY_PREFIX"] = "flask-session:"
    app.config["SESSION_REDIS"] = redis.StrictRedis(host="127.0.0.1", port=6379)

    Session(app)
    login_manager = LoginManager(app)
    login_manager.login_view = "auth.login"

    register_blueprints(app)

    return app