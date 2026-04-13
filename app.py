import click
from flask import Flask
from flask.cli import with_appcontext
from flask_login import LoginManager
from flask_migrate import Migrate

from database import db
from models import User


def create_app():
    app = Flask(__name__)
    app.secret_key = "abax"

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///dados.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)


    db.init_app(app)

    app.cli.add_command(init_db_command)
    app.cli.add_command(create_admin_user)

    # 🔄 Migrate
    migrate = Migrate(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


    from auth import bp
    app.register_blueprint(bp)

    from ctrl_home import bp
    app.register_blueprint(bp)

    from controller import bp
    app.register_blueprint(bp)

    return app

def init_db():
    db.drop_all()
    db.create_all()


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Banco inicializado!")


@click.command("createsuperuser")
@with_appcontext
def create_admin_user():
    from getpass import getpass
    from auth import create_user

    senha = getpass("Digite a senha para admin: ")
    create_user(senha)
    click.echo("Usuário admin criado!")

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)