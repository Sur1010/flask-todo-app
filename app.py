from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), nullable=False, default='todo')

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    todo_text = request.form['todo']
    status = request.form['status']
    new_todo = Todo(text=todo_text, status=status)

    try:
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue adding your task'

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = Todo.query.get_or_404(id)
    if request.method == 'POST':
        todo.text = request.form['todo']
        todo.status = request.form['status']
        try:
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('edit.html', todo=todo)

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get_or_404(id)
    try:
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'There was an issue deleting your task'

if __name__ == "__main__":
    app.run(debug=True)

