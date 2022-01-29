from flask import Flask
from .config import DevConfig

# instance of our class
app = Flask(__name__, instance_relative_config=True)

#  settup configurations
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')


from app import views