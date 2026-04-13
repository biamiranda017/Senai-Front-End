import click
from flask import current_app, g
from flask.cli import with_appcontext

# Simulação de conexão com banco (ajuste conforme seu projeto)
def get_db():
    if 'db' not in g:
        import sqlite3
        g.db = sqlite3.connect('database.db')
    return g.db


def init_db():
    db = get_db()
    db.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    db.commit()
    print("Banco criado!")


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Banco inicializado.')


@click.command('createsuperuser')
@with_appcontext
def create_superuser():
    username = input("Usuário: ")
    password = input("Senha: ")

    db = get_db()
    db.execute(
        "INSERT INTO user (username, password) VALUES (?, ?)",
        (username, password)
    )
    db.commit()

    click.echo('Usuário administrador criado!')


def init_app(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(create_superuser)
   