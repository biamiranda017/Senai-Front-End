"""
Esse arquivo é um exemplo de controller
"""

from flask import Blueprint, request, redirect, url_for, render_template, flash, session
from werkzeug.security import check_password_hash, generate_password_hash

from database import db
from models import User

bp = Blueprint(__name__, "HomeController")

@bp.route("/") # cria uma rota
def index(): # função que gerencia rota
    """ Página inicial"""
    if 'user' not in session:
        return redirect(url_for("auth.login"))
    
    return render_template("dashboard/index.html") # Renderiza um template

@bp.route("/dashboard")  # cria uma rota para navegador http://127.0.0.1:5000/dashboard
def dashboard(): # função que gerencia rota deve ser única
    """Painel de Vendas"""
    # remova o login
    return render_template("dashboard/index.html")  # Renderiza um template
    

