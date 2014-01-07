from flask import Flask, flash, session, redirect, url_for, escape, request, render_template
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    if 'username' in session:
        return 'Index page - logado como: %s' % escape(session['username'])
    return render_template('index.html') #'Index page - nao logado - apenas busca de veiculos'

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
	if request.form['username'] == request.form['password']:
            session['username'] = request.form['username']
	    flash('Logado com sucesso, '+session['username'])
            return redirect(url_for('index'))
	else:
	    error = 'usuario ou senha incorretos'
    return render_template('login.html', error=error)
    return '''
        <form action="" method="post">
            <p>Usuario:<input type=text name=username>
            <p>Senha:<input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
