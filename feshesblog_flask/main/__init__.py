from flask import Blueprint

bp_main = Blueprint('main', __name__)

from feshesblog_flask.main import routes
