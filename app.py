from feshesblog_flask import create_app, db, cli
from feshesblog_flask.models import User, Post, Message, Notification, Task
from waitress import serve

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 
        'User': User, 
        'Post': Post, 
        'Message': Message,
        'Notification': Notification, 
        'Task': Task
    }


if __name__ == '__main__':
    serve(
        app,
        host='127.0.0.1',
        port=5000
    )
