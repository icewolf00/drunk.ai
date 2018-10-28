from keras.models import load_model
import numpy as np
model = load_model("model.npy")

class AI():

    def __init__(self):
        pass

    def predict(self, input_list):
        input_array = np.array(input_list).reshape((1, 10))
        output = model.predict(input_array)
        return output

