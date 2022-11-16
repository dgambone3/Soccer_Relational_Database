from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__, instance_relative_config=True)

# Load views
from app import app

# Setting up app configuration
app.config.from_object('config')

# Initializing flask extensions
db.init_app(app)