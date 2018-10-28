from flask import Flask, render_template, redirect, request
from bot.facebook import Messenger
from bot.crawler import Crawler
import random
import csv

application = Flask(__name__)
# port = random.randrange(1000, 9999)

@application.route("/", methods=['POST', 'GET'])
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
            messenger = Messenger()
            messenger.get_message()
            return 'get message'
            

@application.route("/data.html")
def data():
        data_list = list()
        with open('data/img.csv', newline='') as csvfile:                        
                rows = csv.reader(csvfile)
                for row in rows:
                    data_list.append(row[0])
        return render_template(
        'data.html', 
        img = data_list[0],
        text = data_list[1],
        )

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

@application.route("/elements.html")
def elements():
        return render_template(
                'elements.html', 
                title = 'Drunk.AI',
                )        

@application.route("/pic.html")
def pic():
        crawler = Crawler
        return render_template(
                'pic.html', 
                title = 'Drunk.AI',
                image = crawler.get_from_web()[0].text,
                ratio = crawler.get_from_web()[1].text,
                )     


@application.route("/panels.html")
def panels():
        return render_template(
                'panels.html', 
                title = 'Drunk.AI',                
                )        


if __name__ == "__main__":
    # application.run(debug=True, host='0.0.0.0', port=port)
    application.run(debug=True)
