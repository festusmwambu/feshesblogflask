from flask import Blueprint

bp_auth = Blueprint('auth', __name__)

from feshesblog_flask.auth import routes
