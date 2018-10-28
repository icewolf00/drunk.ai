from flask import request

class Messenger():

    def test():
        return 'Hello World!'

    def get_message():
        data = request.get_json()
        print(data)
        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:
                if messaging_event.get("message"):  

                    sender_id = messaging_event["sender"]["id"]        
                    recipient_id = messaging_event["recipient"]["id"]  
                    message_text = messaging_event["message"]["text"]  
                    print(message_text)
                    # send_message_response(sender_id, parse_user_message(message_text)) 
    
    def get(self, request, *args, **kwargs):
        verify_code = 'webhook'
        verify_token = request.GET.get('hub.verify_token')
        if verify_code == verify_token:
            return HttpResponse(request.GET.get('hub.challenge'))
        else:
            return HttpResponse('False')

    def post(self, request, *args, **kwargs):
        home_url = 'https://www.facebook.com/smart.drive.tw.2018/'
        button = 'Upload'
        output = 'Please upload the image.'
        message = json.loads(self.request.body.decode('utf-8'))
        for row in message['entry']:
            messagings = row['messaging']
            for message in messagings:
                sender_id = message['sender']['id']
                recipient_id = message['recipient']['id']
                try:
                    if message.get('message'):
                        try:
                            img_url = message['message']['attachments'][0]['payload']['url']
                            post_facebook_message(sender_id, output, img_url, button) 
                        except:
                            text = message['message']['text']
                            with open('html.csv', 'w') as csvfile:
                                spamwriter = csv.writer(csvfile)
                                spamwriter.writerow([0])
                            post_facebook_message(sender_id, output, home_url, button) 
                except:
                    with open('html.csv', 'w') as csvfile:
                        spamwriter = csv.writer(csvfile)
                        spamwriter.writerow([0])
                    post_facebook_message(sender_id, output, home_url, button)
        return HttpResponse()


def post_facebook_message(sender_id, text, url, title):
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
