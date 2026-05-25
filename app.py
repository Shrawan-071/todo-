from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# Database configuration
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(BASE_DIR, "todo.db")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todo'

    sno = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(100), nullable=False)
    date_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.task} {self.description} {self.status} {self.date_time}"


@app.route("/", methods=['GET', 'POST'])
def add_todo():

    if request.method == 'POST':

        task = request.form.get('task')
        description = request.form.get('description')

        status = "Pending"

        if task and description:
            new_entry = Todo(
                task=task,
                description=description,
                status=status
            )

            db.session.add(new_entry)
            db.session.commit()

        return redirect("/")

    showing = Todo.query.all()

    return render_template("index.html", showing=showing)


@app.route("/show")
def displaying():

    showing = Todo.query.all()

    print(showing)

    return "Data printed in console"


@app.route("/delete/<int:sno>")
def delete(sno):

    todo_to_delete = Todo.query.get_or_404(sno)

    db.session.delete(todo_to_delete)
    db.session.commit()

    return redirect("/")


@app.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):

    todo_item = Todo.query.get_or_404(sno)

    if request.method == "POST":

        todo_item.task = request.form.get("task")
        todo_item.description = request.form.get("description")
        todo_item.status = request.form.get("status")

        db.session.commit()

        return redirect("/")

    return render_template("update.html", todo=todo_item)


with app.app_context():
    db.create_all()


# IMPORTANT FOR VERCEL
app = app