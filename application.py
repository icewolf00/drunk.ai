from flask import Flask, render_template, redirect, request
from bot.facebook import Messenger
from bot.crawler import Craw
import random
import requests
from bs4 import BeautifulSoup
import re
# import keras

application = Flask(__name__)
port = random.randrange(1000, 9999)
messenger = Messenger
craw = Craw

@application.route("/")
def index():
    return render_template(
        'index.html', 
        title = 'Drunk.AI',
        messenger = 'AWS',
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

@application.route("/map.html")
def map():
    return render_template(
        'map.html', 
        title = 'Drunk.AI',
        )

@application.route("/charts.html")
def charts():
    return render_template(
        'charts.html', 
        title = 'Drunk.AI',
        )        

@application.route("/pic.html")
def pic():
    return render_template(
        'pic.html', 
        title = 'Drunk.AI',
        image = craw.get_from_web()[0].text,
        ratio = craw.get_from_web()[1].text,
        )     


@application.route("/panels.html")
def panels():
    return render_template(
        'panels.html', 
        title = 'Drunk.AI',
        )        



@application.route("/query", methods=['POST', 'GET'])
def query():
    return render_template(
        'index.html', 
        title = 'Drunk.AI'
        )

if __name__ == "__main__":
    # application.run(debug=True, host='0.0.0.0', port=port)
    application.run(debug=True)
