from flask import request
import requests
import json


class Messenger():

    def test():
        return 'Hello World!'

    def get_message():
        data = request.get_json()
        print(data)
        try:
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]        
                        recipient_id = messaging_event["recipient"]["id"]  
                        text = messaging_event["message"]["text"]  
                        return sender_id, text
        except:
            return 'False'

    def send_message(sender_id, text):
        post_message_url = 'https://graph.facebook.com/v3.2/me/messages?access_token=EAADymmUJFN0BAAlZCTYsNVvUCNHQ2wUJGcVD0ctugsWP9EUFrG6kJk2LfpZBMAJp8gxkyUYNq64KFsDbRXHEYbZCZBA4u9ABpUkP5o5lMwqFLhArc8V1hXiigRVN9rwZAZBHTpHI9ZBZB3HeD1r0C45h76B1GRDvXQmOx6L2O7XikwZDZD'
        response_message = json.dumps({
            "recipient": {
                "id": sender_id
            },
            "message": {
                'attachment':{
                    'type':'template',
                    'payload':{
                        "template_type":"button",
                        "text": text,
                        "buttons":[
                            {
                                "type":"web_url",
                                "url": 'url',
                                "title": 'title',
                            },
                        ]
                    }
                }
            }
        })
        status = requests.post(
            post_message_url,
            headers = {"Content-Type": "application/json"},
            data = response_message)
        print(status.json())
