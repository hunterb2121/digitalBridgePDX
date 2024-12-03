from flask import Flask
from flask_session import Session
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from flask_compress import Compress
import os
import redis


def create_app():
    print("Creating Flask app...")
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "temp_secret_key_1")
    """
    app.config["SESSION_TYPE"] = "redis"
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_USE_SIGNER"] = True
    app.config["SESSION_KEY_PREFIX"] = "flask-session:"
    app.config["SESSION_REDIS"] = redis.StrictRedis(host=os.getenv("REDIS_HOST"), port=6379)

    Session(app)
    login_manager = LoginManager(app)
    login_manager.login_view = "auth.login"
    """
    csrf = CSRFProtect(app)
    csrf.init_app(app)

    compress = Compress()
    compress.init_app(app)

    print("Registering blueprints...")
    from .routes import register_blueprints
    register_blueprints(app)

    return app