from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    favourite_pizzas = ["bbq chicken ", "margaritha"]
    return render_template('index.html', favourite_pizzas=favourite_pizzas)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html")
