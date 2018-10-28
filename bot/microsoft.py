import cognitive_face as CF
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import json

class FaceAPI():

    def __init__(self):
        pass

    def test(self):
        print('Hello World!')

    def get_feature(self, img_url):
        img_url = img_url
        KEY = '9d31ad59e78148ee842db3797c734b50'  
        CF.Key.set(KEY)
        BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0/'
        CF.BaseUrl.set(BASE_URL)
        faces = (CF.face.detect(img_url, landmarks=True, attributes='age,gender,headPose,smile,facialHair,glasses,emotion,makeup,accessories,occlusion,blur,exposure,noise,hair'))
        img_str = json.dumps(faces, sort_keys=True, indent=2)
        feature = self.choose_feature(img_str)
        return feature

    def choose_feature(self, img_str):
        img_list = json.loads(img_str)
        output_list = list()
        output_list.append(img_list[0]['faceAttributes']['smile'])
        output_list.append(img_list[0]['faceAttributes']['emotion']['anger'])
        output_list.append(img_list[0]['faceAttributes']['emotion']['contempt'])
        output_list.append(img_list[0]['faceAttributes']['emotion']['disgust'])
        output_list.append(img_list[0]['faceAttributes']['emotion']['fear'])
        output_list.append(img_list[0]['faceAttributes']['emotion']['happiness'])
        output_list.append(img_list[0]['faceAttributes']['emotion']['neutral'])
        output_list.append(img_list[0]['faceAttributes']['emotion']['sadness'])
        output_list.append(img_list[0]['faceAttributes']['emotion']['surprise'])
        output_list.append(img_list[0]['faceAttributes']['occlusion']['eyeOccluded'])
        if output_list[-1] == 'True':
            output_list[-1] = 1
        else:
            output_list[-1] = 0
        return output_list

        

