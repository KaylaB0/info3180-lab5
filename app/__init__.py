from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

crsf = CSRFProtect(app)

# Initialize database and migration objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models
from app.views import api  # import the blueprint
app.register_blueprint(api)  # register the blueprint


