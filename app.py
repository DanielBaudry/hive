import os

from flask import Flask
from flask_login import LoginManager
from sqlalchemy import orm

from repository.db import db
from repository.user import UserRepository

app = Flask(__name__,
            template_folder='views',
            static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/hive.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ.get('FLASK_SECRET', '+%+3Q23!zbc+!Dd@')
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id: int):
    return UserRepository().get_user_by_id(user_id)


db.init_app(app)
login_manager.init_app(app)

with app.app_context():
    import controllers
    orm.configure_mappers()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    app.run(use_reloader=True)
