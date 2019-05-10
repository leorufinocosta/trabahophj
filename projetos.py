from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL
from bd import *

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'projetos'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        cursor = mysql.get_db().cursor()

        idlogin = get_idlogin(cursor, login, senha)

        if idlogin is None:
            return render_template('index.html', erro='Login/senha incorretos!')
        else:
            #conn =mysql.connect()
            #cursor = conn.cursor()
            #projetos = get_projetos(cursor)
            #cursor.close()
            #conn.close()
            cursor = mysql.get_db().cursor()
            return render_template('listaprojetos.html', projetos=get_projetos(cursor))

    else:
        return render_template('index.html', erro='Método incorreto. Use POST!')

@app.route('/listaatividades/<proj>')
def ativi(proj):
    cursor = mysql.get_db().cursor()
    return render_template('listaatividades.html', projeto=exibir_atividades(cursor, idlistadeprojetos=proj))

if __name__ == '__main__':
    app.run(debug=True)