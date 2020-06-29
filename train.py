import cv2
import numpy as np
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

IMG_SAVE_PATH_TRAIN = 'image_data\\train'
IMG_SAVE_PATH_TEST = 'image_data\\test'

def get_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),
        tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(2, 2),

        # Flatten the results
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.5),

        # Hidden layer
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(4, activation='softmax')
    ])
    return model


def train_and_save_model(learning_rate, epochs):
    # load images from the directory
    training_dir = IMG_SAVE_PATH_TRAIN
    training_dataGen = ImageDataGenerator(rescale=1.0 / 255)
    train_generator = training_dataGen.flow_from_directory(training_dir, target_size=(150, 150),
                                                           class_mode='categorical')
    testing_dir = IMG_SAVE_PATH_TEST
    testing_dataGen = ImageDataGenerator(rescale=1.0 / 255)
    test_generator = testing_dataGen.flow_from_directory(testing_dir, target_size=(150, 150), class_mode='categorical')

    model = get_model()
    model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.RMSprop(lr=learning_rate), metrics=['accuracy'])

    history = model.fit_generator(train_generator, epochs=epochs, validation_data=test_generator, verbose=1, )

    test_loss, test_acc = model.evaluate_generator(test_generator)
    print('\nTest accuracy:', test_acc)

    # save the model for later use
    model.save("rock-paper-scissors-model.h5")

    return test_acc
