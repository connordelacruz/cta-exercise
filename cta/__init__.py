import logging
import flask
from config import Config

logging.basicConfig(level=logging.DEBUG)

app = flask.Flask(__name__)
app.config.from_object(Config)

from cta import routes
