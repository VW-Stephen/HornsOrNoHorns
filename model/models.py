"""
Contains Keras model definitions for the various types of NN's to test
"""
from keras.layers import Conv2D, Activation, MaxPooling2D, Flatten, Dense, Dropout
from keras.models import Sequential


class BasicModel(object):
    @staticmethod
    def compile(image_width, image_height):
        model = Sequential()
        model.add(Conv2D(32, (3, 3), input_shape=(image_height, image_width, 1)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(32, (3, 3)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3)))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(64))
        model.add(Activation("relu"))
        model.add(Dropout(0.5))
        model.add(Dense(1))
        model.add(Activation("sigmoid"))

        model.compile(
            loss="binary_crossentropy",
            optimizer="rmsprop",
            metrics=["accuracy"]
        )
        return model
