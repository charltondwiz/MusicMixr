import tensorflow as tf
from tensorflow import keras

import numpy as np
import pandas as pd

train = pd.read_excel("data/nujabes_training.xlsx")
test = pd.read_excel("data/nujabes_test.xlsx")
mix2 = pd.read_excel("data/nujabes_prediction.xlsx")

train.pop('song_name')
test.pop('song_name')
mix2_song_names = mix2.pop('song_name')

train_y = train.pop('rating')
test_y = test.pop('rating')
mix2_y = mix2.pop('rating')

print(train_y)

class_names = ["Don't like it", "Like it"]

model = keras.Sequential([keras.layers.Dense(128, activation='relu'),
                          keras.layers.Dense(64, activation='relu'),
                          keras.layers.Dense(32, activation='relu'),
                          keras.layers.Dense(16, activation='relu'),
                          keras.layers.Dense(8, activation='relu'),
                          keras.layers.Dense(4, activation='relu'),
                          keras.layers.Dense(2)])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train, train_y, epochs=5500)

test_loss, test_acc = model.evaluate(test, test_y, verbose=2)
print('\nTest accuracy:', test_acc)

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])
predictions = probability_model.predict(mix2)

print(np.argmax(predictions[0]))

counter = 0
for prediction in predictions:
    print(mix2_song_names[counter], '-', np.argmax(prediction), ' with predictions of ',
          "{0:.0%}".format(prediction[np.argmax(prediction)]), " ", prediction)
    counter += 1


