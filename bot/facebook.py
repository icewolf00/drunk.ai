from flask import request
import requests
import json


class Messenger():

    def get_message():
        data = request.get_json()
        print(data)
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]        
                    # recipient_id = messaging_event["recipient"]["id"] 
                    # text = messaging_event["message"]["text"]                        
                    try:                    
                        img = messaging_event['message']['attachments'][0]['payload']['url']
                        return sender_id, img
                    except:
                        return sender_id, 'error'                    

    def send_message(sender_id, text):
        access_token = 'EAADymmUJFN0BAGJ18T95ZAk6RY3gDUXYvKLIRE7GBxFoZA9yZCJ3YtQ6ajL94yEZBsdKtmoYZAoZCaLqpLp8ShpGNu2AsvrMIaGI1MZBY55ddyoPE6n667vfFZCMWDRIzZBrTcbEcmhrq6Vbvz5dvdOLghZCZANQFTCdZBh7HGqk7ICTvQZDZD'
        r = requests.post("https://graph.facebook.com/v3.2/me/messages",
            params={"access_token": access_token},
            headers={"Content-Type": "application/json"}, 
            data=json.dumps({
            "recipient": {"id": sender_id},
            "message": {"text": text}
    }))