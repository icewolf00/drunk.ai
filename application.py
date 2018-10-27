from flask import Flask, render_template, redirect, request
from bot.facebook import Messenger
import random
import keras
# import tensorflow

application = Flask(__name__)
port = random.randrange(1000, 9999)
messenger = Messenger
print(keras)

@application.route("/")
def index():
    return render_template(
        'index.html', 
        title = 'Drunk.AI',
        messenger = 'OK',
        )

@application.route("/webhook", methods=['POST', 'GET'])
def webhook():
        verify_code = 'webhook'
        verify_token = request.args.get('hub.verify_token')
        if verify_code == verify_token:
            return request.args.get('hub.challenge')
        else:
            return 'False'


@application.route("/index.html")
def home():
    return render_template(
        'index.html', 
        title = 'Drunk.AI',
        )

@application.route("/widgets.html")
def widgets():
    return render_template(
        'widgets.html', 
        title = 'Drunk.AI',
        )

@application.route("/charts.html")
def charts():
    return render_template(
        'charts.html', 
        title = 'Drunk.AI',
        )        

@application.route("/elements.html")
def elements():
    return render_template(
        'elements.html', 
        title = 'Drunk.AI',
        )        

@application.route("/panels.html")
def panels():
    return render_template(
        'panels.html', 
        title = 'Drunk.AI',
        )        

@application.route("/login.html")
def login():
    return render_template(
        'login.html', 
        title = 'Drunk.AI',
        )        


@application.route("/query", methods=['POST', 'GET'])
def query():
    return render_template(
        'index.html', 
        title = 'Drunk.AI'
        )

if __name__ == "__main__":
    application.run(debug=True, host='0.0.0.0', port=port)