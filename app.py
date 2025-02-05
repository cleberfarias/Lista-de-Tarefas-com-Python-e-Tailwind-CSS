from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tarefas.db'
db = SQLAlchemy(app)

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    completa = db.Column(db.Boolean, default=False)

with app.app_context():
    db.create_all()

@app.route('/')
def listar_tarefas():
    tarefas = Tarefa.query.all()
    return render_template('lista.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar_tarefa():
    descricao = request.form['descricao']
    nova_tarefa = Tarefa(descricao=descricao)
    db.session.add(nova_tarefa)
    db.session.commit()
    return redirect(url_for('listar_tarefas'))

@app.route('/completar/<int:id>')
def completar_tarefa(id):
    tarefa = Tarefa.query.get(id)
    tarefa.completa = not tarefa.completa
    db.session.commit()
    return redirect(url_for('listar_tarefas'))

@app.route('/excluir/<int:id>')
def excluir_tarefa(id):
    tarefa = Tarefa.query.get(id)
    db.session.delete(tarefa)
    db.session.commit()
    return redirect(url_for('listar_tarefas'))


if __name__ == '__main__':
    app.run(debug=True)

