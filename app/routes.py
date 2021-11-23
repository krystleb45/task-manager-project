from app.database.task import Task
from flask import (
    Flask,
    render_template,
    request,
    redirect
)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)


TLIST = []


@app.get("/")
def index():
    tasks = [
        {
            "id": 1,
            "name": "First task",
            "body": "Do something."
        },
        {
            "id": 2,
            "name": "Second task",
            "body": "Do something else."
        }
    ]
    return render_template("home.html", task_list=TLIST)


@app.get("/about")
def about_me():
    me = {
        "first_name": "krystle",
        "last_name": "berry",
        "bio": "analyst"
    }
    return render_template("about.html", user=me)


@app.get("/tasks/create")
def get_form():
    return render_template("create_task.html")


@app.post("/tasks")
def create_task():
    task_data = request.form
    task_dict = {
        "name": task_data.get("name"),
        "body": task_data.get("body")
    }
    TLIST.append(task_dict)
    return redirect("/")
