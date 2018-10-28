from keras.models import load_model
import numpy as np

class AI():

    def __init__(self):
        pass

    def predict(self, input_list):
        model = load_model("data/model.npy")
        input_array = np.array(input_list).reshape((1, 10))
        output = model.predict(input_array)
        return str(round(float(output[0][0]), 2))

