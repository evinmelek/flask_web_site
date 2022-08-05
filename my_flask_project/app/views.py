from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def definition():
    return render_template("articles.html")


@app.route("/hello")
def hello():
    return render_template("articles.html")


@app.route("/admin")
def hello_admin():
    return render_template("hello_admin.html")


@app.route("/user/<name>")
def hello_user(name):
    if name.lower() == "admin":
        return redirect(url_for("hello_admin"))
    return render_template("hello_user.html", username=name)


@app.route("/add/<int:number1>/<int:number2>")
def add(number1, number2):
    calculation_result = number1 + number2
    return render_template("add.html", number1=number1, number2=number2, result=calculation_result)


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # if "username" in request.form:
        username = request.form["username"]
        return redirect(url_for("user", name=username))
    else:
        return render_template("login.html")


@app.route("/student", methods=['POST'])
def student():
    return render_template("student.html")


@app.route("/result", methods=['POST'])
def result():
    ContextData = {
        'name': request.form["name"],
        'physics': request.form["physics"],
        'mathematics': request.form["mathematics"],
        'chemistry': request.form["chemistry"]
    }
    return render_template("student_result.html", **ContextData)
