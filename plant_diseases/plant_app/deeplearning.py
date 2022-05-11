import tensorflow as tf
from keras.models import load_model
# global graph, model, output list

graph = tf.get_default_graph()
model = load_model('plant_app/AlexNetModel.hdf5')

output_dict = {'Apple-Apple scab': 0,
               'Apple-Black rot': 1,
               'Apple-Cedar apple rust': 2,
               'Apple-healthy': 3,
               'Blueberry-healthy': 4,
               'Cherry (including sour)-Powdery mildew': 5,
               'Cherry (including sour)-healthy': 6,
               'Corn (maize)-Cercospora leaf spot Gray leaf spot': 7,
               'Corn (maize)-Common rust ': 8,
               'Corn Northern Leaf Blight': 9,
               'Corn (maize)-healthy': 10,
               'Grape-Black rot': 11,
               'Grape-Esca (Black Measles)': 12,
               'Grape-Leaf blight (Isariopsis Leaf Spot)': 13,
               'Grape-healthy': 14,
               'Orange-Haunglongbing (Citrus greening)': 15,
               'Mango-Bacterial spot': 16,
               'Peach-healthy': 17,
               'Pepper bell-Bacterial spot': 18,
               'Pepper bell-healthy': 19,
               'Potato-Early blight': 20,
               'Potato-Late blight': 21,
               'Potato-healthy': 22,
               'Raspberry-healthy': 23,
               'Soybean-healthy': 24,
               'Squash-Powdery mildew': 25,
               'Strawberry-Leaf scorch': 26,
               'Strawberry-healthy': 27,
               'Tomato-Bacterial spot': 28,
               'Tomato-Early blight': 29,
               'Mango-healthy': 30,
               'Tomato-Leaf Mold': 31,
               'Tomato-Septoria leaf spot': 32,
               'Tomato-Spider mites Two-spotted spider mite': 33,
               'Tomato-Target Spot': 34,
               'Tomato-Tomato Yellow Leaf Curl Virus': 35,
               'Tomato-Tomato mosaic virus': 36,
               'Tomato-healthy': 37}

output_list = list(output_dict.keys())
