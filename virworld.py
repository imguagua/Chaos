##-*- coding: utf-8 -*-
from app import create_app, db
from app.models import User
from flask.ext.script import Manager, Shell

app = create_app('default')
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, User=User)
manager.add_command("shell", Shell(make_context=make_shell_context))

if '__main__' == __name__:
    manager.run()
