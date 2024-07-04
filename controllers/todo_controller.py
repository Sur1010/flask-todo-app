from flask import Blueprint, render_template, request, redirect, url_for
from models.todo import Todo

todo_app = Blueprint('todo_app', __name__)

todos = []

@todo_app.route('/')
def index():
    return render_template('index.html', todos=todos)

@todo_app.route('/add', methods=['POST'])
def add():
    todo_text = request.form['todo']
    status = request.form.get('status', 'todo')
    todos.append(Todo(todo_text, status=status))
    return redirect(url_for('.index'))

@todo_app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo.text = request.form['todo']
        todo.status = request.form.get('status', 'todo')
        return redirect(url_for('.index'))
    else:
        return render_template('edit.html', todo=todo, index=index)

@todo_app.route('/check/<int:index>')
def check(index):
    todos[index].toggle_done()
    return redirect(url_for('.index'))

@todo_app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('.index'))
