from flask import jsonify
from feshesblog_flask import db
from feshesblog_flask.api import bp_api
from feshesblog_flask.api.auth import basic_auth, token_auth


@bp_api.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = basic_auth.current_user().get_token()
    db.session.commit()
    return jsonify({'token': token})


@bp_api.route('/tokens', methods=['DELETE'])
@token_auth.login_required
def revoke_token():
    token_auth.current_user().revoke_token()
    db.session.commit()
    return '', 204
