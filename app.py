from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

# ---------------- VERCEL SAFE SQLITE ----------------
db_path = "/tmp/todo.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + db_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# ---------------- MODEL ----------------
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(100), default="Pending")
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# ---------------- CREATE TABLES ----------------
with app.app_context():
    db.create_all()

# ---------------- ROUTES ----------------
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        description = request.form.get("description")

        if task and description:
            new_task = Todo(task=task, description=description)
            db.session.add(new_task)
            db.session.commit()

        return redirect("/")

    todos = Todo.query.order_by(Todo.date_created.desc()).all()
    return render_template("index.html", todos=todos)


@app.route("/delete/<int:id>")
def delete(id):
    task = Todo.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect("/")


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == "POST":
        task.task = request.form.get("task")
        task.description = request.form.get("description")
        task.status = request.form.get("status")
        db.session.commit()
        return redirect("/")

    return render_template("update.html", task=task)


# ---------------- VERCEL ENTRY POINT ----------------
application = app