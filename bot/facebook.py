from .ai import AI
from .microsoft import FaceAPI
from flask import request
import requests
import json

# img = 'https://scontent.xx.fbcdn.net/v/t1.15752-9/44919995_454820941707879_6369963221872279552_n.jpg?_nc_cat=100&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=139f661141bcae5b6a6fb2f149592fea&oe=5C43F318'
# face_api = FaceAPI()
# feature = face_api.get_feature(img)
# ai = AI()
# ratio = ai.predict(feature)
# print(ratio)

class Messenger():

    def __init__(self):
        pass

    def get_message(self):
        data = request.get_json()
        # print(data)
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):
                    sender_id = messaging_event["sender"]["id"]        
                    # recipient_id = messaging_event["recipient"]["id"] 
                    # text = messaging_event["message"]["text"]                        
                    try:                    
                        img = messaging_event['message']['attachments'][0]['payload']['url']
                        # face_api = FaceAPI()
                        # feature = face_api.get_feature(img)
                        # ai = AI()
                        # text = ai.predict(feature)
                        text = '0.9'
                        with open('data/img.csv', 'w') as csvfile:
                            csvfile.writelines(img)
                            csvfile.writelines('\n')
                            csvfile.writelines(text)
                        self.send_message(sender_id, img)
                    except:
                        return 'send message fail'             

    def send_message(self, sender_id, text):
        access_token = 'EAADymmUJFN0BAGJ18T95ZAk6RY3gDUXYvKLIRE7GBxFoZA9yZCJ3YtQ6ajL94yEZBsdKtmoYZAoZCaLqpLp8ShpGNu2AsvrMIaGI1MZBY55ddyoPE6n667vfFZCMWDRIzZBrTcbEcmhrq6Vbvz5dvdOLghZCZANQFTCdZBh7HGqk7ICTvQZDZD'
        requests.post("https://graph.facebook.com/v3.2/me/messages",
        params = {"access_token": access_token},
        headers = {"Content-Type": "application/json"}, 
        data = json.dumps({
        "recipient": {"id": sender_id},
        "message": {"text": text}
    }))