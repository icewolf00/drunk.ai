from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)
port = random.randrange(1000, 9999)

@app.route("/")
def index():
    return render_template(
        'index.html', 
        title = 'Hello World!',
        )

@app.route("/index.html")
def home():
    return render_template(
        'index.html', 
        title = 'Hello World!',
        )

@app.route("/widgets.html")
def widgets():
    return render_template(
        'widgets.html', 
        title = 'Hello World!',
        )

@app.route("/charts.html")
def charts():
    return render_template(
        'charts.html', 
        title = 'Hello World!',
        )        

@app.route("/elements.html")
def elements():
    return render_template(
        'elements.html', 
        title = 'Hello World!',
        )        

@app.route("/panels.html")
def panels():
    return render_template(
        'panels.html', 
        title = 'Hello World!',
        )        

@app.route("/login.html")
def login():
    return render_template(
        'login.html', 
        title = 'Hello World!',
        )        


@app.route("/query", methods=['POST', 'GET'])
def query():
    return render_template(
        'index.html', 
        )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)