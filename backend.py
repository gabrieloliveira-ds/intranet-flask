from turtle import title
from flask import Flask, redirect, render_template, request, redirect, session, flash, url_for

#configurando o app
app = Flask(__name__, template_folder='template')

#paginas
@app.route('/')
def index():
    return render_template('index.html',title= 'Atenas Intranet|HOME') 

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html',title= 'Atenas Intranet|CADASTRO')

@app.route('/cadastro-funcionario')
def cadastro_funcionario():
    return render_template('cadastro-funcionario.html',title='Atenas Intranet|CADASTRO')

@app.route('/cadastro-cliente')
def cadastro_cliente():
    return render_template('cadastro-cliente.html',title='Atenas Intranet|CADASTRO')
#rotas

#inicialização 
if __name__ == "__main__":
    app.run(debug=True)
