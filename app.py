import os
from functools import wraps

import bcrypt
import pymysql
from dotenv import load_dotenv
from flask import Flask, request, redirect, render_template, session
from pymysql.err import IntegrityError

from db import get_connection

load_dotenv()

app = Flask(__name__)
secret_key = os.getenv("SECRET_KEY")

if not secret_key:
    raise RuntimeError("SECRET_KEY is missing from .env")

app.secret_key = secret_key


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect("/login")

        return func(*args, **kwargs)

    return wrapper


@app.route("/")
def home():
    if "user_id" in session:
        return redirect("/todos")

    return redirect("/register")


@app.route("/register", methods=["GET", "POST"])
def register():
    errors = []

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not name:
            errors.append("Name is required")

        if not email:
            errors.append("Email is required")

        if not password:
            errors.append("Password is required")

        if not confirm_password:
            errors.append("Confirm password is required")

        if password and confirm_password and password != confirm_password:
            errors.append("Passwords do not match")

        if len(name) > 100:
            errors.append("Name is too long")

        if not errors:
            password_hash = bcrypt.hashpw(
                password.encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")

            connection = get_connection()
            cursor = connection.cursor()

            try:
                cursor.execute(
                    "INSERT INTO users (email, name, password_hash) "
                    "VALUES (%s, %s, %s)",
                    (email, name, password_hash)
                )

                connection.commit()

                cursor.execute(
                    "SELECT user_id, name FROM users WHERE email = %s",
                    (email,)
                )

                user = cursor.fetchone()

                session.clear()
                session["user_id"] = user[0]
                session["name"] = user[1]

                return redirect("/todos")

            except IntegrityError:
                connection.rollback()
                errors.append("Email Already Exists")

            finally:
                cursor.close()
                connection.close()

    return render_template("register.html", errors=errors)


@app.route("/login", methods=["GET", "POST"])
def login():
    errors = []

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not email:
            errors.append("Email is required")

        if not password:
            errors.append("Password is required")

        if not errors:
            connection = get_connection()
            cursor = connection.cursor()

            try:
                cursor.execute(
                    "SELECT user_id, name, password_hash "
                    "FROM users WHERE email = %s",
                    (email,)
                )

                user = cursor.fetchone()

                if user:
                    try:
                        valid_password = bcrypt.checkpw(
                            password.encode("utf-8"),
                            user[2].encode("utf-8")
                        )
                    except ValueError:
                        valid_password = False
                else:
                    valid_password = False

                if user and valid_password:
                    session.clear()
                    session["user_id"] = user[0]
                    session["name"] = user[1]

                    return redirect("/todos")

                errors.append("Invalid email or password")

            finally:
                cursor.close()
                connection.close()

    return render_template("login.html", errors=errors)


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect("/login")


@app.route("/todos")
@login_required
def todos():
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "SELECT todo_id, title, is_done, created_at "
            "FROM todos WHERE user_id = %s ORDER BY todo_id DESC",
            (session["user_id"],)
        )

        tasks = cursor.fetchall()

    finally:
        cursor.close()
        connection.close()

    return render_template(
        "todos.html",
        tasks=tasks,
        name=session["name"],
        error=request.args.get("error", "")
    )


@app.route("/add_todo", methods=["GET", "POST"])
@login_required
def add_todo():
    errors = []

    if request.method == "POST":
        title = request.form.get("title", "").strip()

        if not title:
            errors.append("Title is required")
        elif len(title) > 200:
            errors.append("Title is too long (200 characters at most)")

        if not errors:
            connection = get_connection()
            cursor = connection.cursor()

            try:
                cursor.execute(
                    "INSERT INTO todos (user_id, title) VALUES (%s, %s)",
                    (session["user_id"], title)
                )

                connection.commit()

                return redirect("/todos")

            finally:
                cursor.close()
                connection.close()

    return render_template("add_todo.html", errors=errors)


@app.route("/edit_todo/<int:todo_id>", methods=["POST"])
@login_required
def edit_todo(todo_id):
    title = request.form.get("title", "").strip()

    if not title:
        return redirect("/todos?error=Title%20is%20required")

    if len(title) > 200:
        return redirect(
            "/todos?error=Title%20is%20too%20long%20(200%20characters%20at%20most)"
        )

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "UPDATE todos SET title = %s "
            "WHERE todo_id = %s AND user_id = %s",
            (title, todo_id, session["user_id"])
        )

        connection.commit()

    finally:
        cursor.close()
        connection.close()

    return redirect("/todos")



@app.route("/toggle_todo/<int:todo_id>", methods=["POST"])
@login_required
def toggle_todo(todo_id):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        
        cursor.execute(
            "SELECT is_done FROM todos "
            "WHERE todo_id = %s AND user_id = %s",
            (todo_id, session["user_id"])
        )

        task = cursor.fetchone()

        
        if task:
            new_status = 1 - task[0]

            cursor.execute(
                "UPDATE todos SET is_done = %s "
                "WHERE todo_id = %s AND user_id = %s",
                (new_status, todo_id, session["user_id"])
            )

            connection.commit()

    finally:
        cursor.close()
        connection.close()

    return redirect("/todos")



@app.route("/delete_todo/<int:todo_id>", methods=["POST"])
@login_required
def delete_todo(todo_id):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "DELETE FROM todos WHERE todo_id = %s AND user_id = %s",
            (todo_id, session["user_id"])
        )

        connection.commit()

    finally:
        cursor.close()
        connection.close()

    return redirect("/todos")


if __name__ == "__main__":
    app.run(debug=True)