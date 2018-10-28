from flask import request

class Messenger():

    def test():
        return 'Hello World!'

    def get_message():
        data = request.get_json()
        try:
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    if messaging_event.get("message"):
                        sender_id = messaging_event["sender"]["id"]        
                        recipient_id = messaging_event["recipient"]["id"]  
                        message_text = messaging_event["message"]["text"]  
                        print(message_text)
                        # send_message(sender_id, 'test', 'test', 'test')
                        return 'True'
        except:
            print(data)
            return 'False'

def send_message(sender_id, text, url, title):
    #post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAD6HcWbZAcEBAB1XGWqOZCh4N2LHdbl9G9yNDiOXjEqhIXtYzZAg8FyqxkUVtRnZBDiiWjxvUM1nlWjF6EwQuxUbhQN1XwSm26n11F9KQKNHZBTZCoAkqfnw4g3YFXMXM8ZCKpYZCKra5VExv5KO0zMhgshhfajMZBdNzeZBZBMZBeReAZDZD'
    # post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAD6HcWbZAcEBABN4AeWW0hi1PuFT6nrOBeRTqyBpIzElSTPNLkEEZARKXrM6PCWkBCGosgErrqekmJLhP02jy6ZCZAAY4H6UIN0P3CBRPZAZBxcg5WX6vDe8vyxxrcxvN3RDMXHRCNXOSDgv8s8FXabJnZASPIxBuV8AR9qZBKU3QZDZD'
    post_message_url = 'https://graph.facebook.com/v3.2/me/messages?access_token=EAADymmUJFN0BAAlZCTYsNVvUCNHQ2wUJGcVD0ctugsWP9EUFrG6kJk2LfpZBMAJp8gxkyUYNq64KFsDbRXHEYbZCZBA4u9ABpUkP5o5lMwqFLhArc8V1hXiigRVN9rwZAZBHTpHI9ZBZB3HeD1r0C45h76B1GRDvXQmOx6L2O7XikwZDZD'
    response_msg = json.dumps({
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
                            "url": url, 
                            "title": title,
                        },
                    ]
                }
            }
        }
    })
    status = requests.post(
        post_message_url,
        headers={"Content-Type": "application/json"},
        data=response_msg)
    print(status.json())
