# 1. Importamos as ferramentas e as novas extensões
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

# 2. Criamos e configuramos a aplicação
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

# --- Definição das Rotas ---

# Rota 1: Página Principal (Home)
@app.route('/')
def index():
    # Passamos o objeto datetime diretamente. O Flask-Moment irá formatá-lo no template.
    return render_template('index.html', data_atual=datetime.now())

# Rota 2: Página de Identificação
@app.route('/user/<nome>/<prontuario>/<instituicao>')
def identificacao(nome, prontuario, instituicao):
    return render_template('identificacao.html', nome=nome, prontuario=prontuario, instituicao=instituicao)

# Rota 3: Página de Contexto da Requisição
@app.route('/contextorequisicao/<nome>')
def contexto_requisicao(nome):
    user_agent = request.headers.get('User-Agent')
    user_ip = request.remote_addr
    host = request.host
    return render_template('contexto.html', nome=nome, user_agent=user_agent, user_ip=user_ip, host=host)

# --- Manipuladores de Erro ---

# Rota para Erro 404 (Página Não Encontrada)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Rota para Erro 500 (Erro Interno do Servidor)
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500