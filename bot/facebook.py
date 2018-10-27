class Messenger():

    def test():
        return 'Hello World!'

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
                            face = Face
                            keras = Keras
                            # email = Email
                            img_url0 = 'https://scontent-ort2-2.xx.fbcdn.net/v/t1.15752-9/31131203_776020582588623_6646175892982726656_n.jpg?_nc_cat=0&_nc_ad=z-m&_nc_cid=0&oh=1ed2e2290fd43fd2e79dfde19650d59e&oe=5B705AB4'
                            img_url = message['message']['attachments'][0]['payload']['url']
                            # is_same = face.is_same(img_url0, img_url)
                            # if is_same:
                            #     identity = True
                            # else:
                            #     identity = False
                            face_feature = face.get_feature(img_url)
                            output_list = face.choose_feature(face_feature)
                            score = float(keras.predict(output_list)[0, 0])
                            score = round(score, 2)
                            with open('html.csv', 'w') as csvfile:
                                spamwriter = csv.writer(csvfile)
                                spamwriter.writerow([score])
                            # if identity == True:
                            #     identity_str = 'Danny'
                            # else:
                            #     identity_str = 'Unknown'
                            #     button = 'Unknown'
                                # email.send('[Warning] Driver identity is unknown.', img_url)
                            if score >= 0.9:
                                status = False
                                button = 'Drunk'
                                # email.send('[Warning] Driver status is disabled.', img_url)
                            else:
                                status = True
                                button = 'Normal'
                            score = str(score * 100)
                            score = score[:-2]
                            output = 'Drunk Detect: %s%%' % (score)
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
