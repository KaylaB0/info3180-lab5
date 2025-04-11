from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
app.config.from_object(Config)

crsf = CSRFProtect(app)

# Initialize database and migration objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import views, models


