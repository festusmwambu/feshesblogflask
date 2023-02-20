from flask import Blueprint

bp_errors = Blueprint('errors', __name__)

from feshesblog_flask.errors import handlers
