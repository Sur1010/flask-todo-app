from flask import Flask
from controllers.todo_controller import todo_app

app = Flask(__name__, template_folder='views')
app.register_blueprint(todo_app)

if __name__ == '__main__':
    app.run(debug=True)