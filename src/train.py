import pickle
import tensorflow as tf
import keras
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import numpy as np
from keras import Sequential
from keras.layers import Conv2D,MaxPooling2D,Activation,Dropout,Flatten, Reshape,BatchNormalization,Dense
import random


import cv2

from keras import backend as K
K.tensorflow_backend._get_available_gpus()

result_dictionary = {}

X = []
Y = []
dictionary_angles = {}
print("Generating Sweet Pickle")
# with open('X.pkl', 'rb') as f:
#     X = pickle.load(f)
#     f.close()
# with open('Y.pkl', 'rb') as f:
#     Y = pickle.load(f)
#     f.close()
with open('dictionary.pkl','rb') as f:
    dictionary_angles = pickle.load(f)
    f.close()

print("Pickle is sweet")

model = Sequential()
model.add(Conv2D(16,(7,7),strides=1,input_shape=(240,240,3)))
model.add(Activation("relu"))
model.add(BatchNormalization(momentum=0.75, epsilon=0.0001))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))

model.add(Conv2D(16,(7,7),strides=1))
model.add(Activation("relu"))
model.add(BatchNormalization(momentum=0.75, epsilon=0.0001))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))

model.add(Conv2D(16,kernel_size=(7,7),strides=1))
model.add(Activation("relu"))
model.add(BatchNormalization(momentum=0.75, epsilon=0.0001))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))

model.add(Conv2D(64, kernel_size=(7,7), strides=1))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(25))
model.add(Activation("sigmoid"))

model.compile(loss="binary_crossentropy",
              optimizer="adam",
              metrics=['accuracy'])

angles = ["{0:03}".format(i) for i in range(0, 181, 18)]
# for angle in angles:
#     X = dictionary_angles[angle + '_X']
#     Y = dictionary_angles[angle + '_Y']
#     combined = list(zip(X, Y))
#     random.shuffle(combined)
#     X[:], Y[:] = zip(*combined)
#     x_train,  y_train = X, Y
#     y_train = to_categorical(y_train)
#     x_train = np.asarray(x_train)
#     model.fit(x_train, y_train, epochs=1, batch_size=128, validation_split=0.1)
#     model.save(angle + '.h5', overwrite=True)

for angle in angles:
    model = tf.keras.models.load_model(angle + '.h5')
    for angle2 in angles:
        print(angle, angle2)
        x_test, y_test = dictionary_angles[angle2 + '_X'], dictionary_angles[angle2 + '_Y']
        combined = list(zip(x_test, y_test))
        random.shuffle(combined)
        x_test[:], y_test[:] = zip(*combined)
        y_test = to_categorical(y_test)
        x_test = np.asarray(x_test)
        test_loss, test_acc = model.evaluate(x_test, y_test)
        result_dictionary[angle + '_' + angle2] = test_acc

# model.fit(x_train, y_train, epochs=5,batch_size=32,validation_split=0.1)
# model.save('all_angle_normalized.h5',overwrite=True)
# model = tf.keras.models.load_model('all_angle.h5')
#
# test_loss, test_acc = model.evaluate(x_test, y_test)
for result in result_dictionary:
    print(str(result_dictionary[result]))


# print(test_acc)