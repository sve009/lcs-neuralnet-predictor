import tensorflow as tf

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Hyperconstants

num_epochs = 500

def plot_hist(hist, epochs):
    x = np.arange(epochs)
    y = hist.history['loss']

    plt.plot(x, y)
    plt.xlabel("Epochs")
    plt.ylabel("Mean Squared Error")

    plt.show()

# Main

data = pd.read_csv("formatted_data.csv", dtype=np.float32)

df = data.sample(frac=1).reset_index(drop=True)

test = df[:30]
train = df[30:]

train_features = train
train_labels = train.pop("Win Rate")

test_features = test
test_labels = test.pop("Win Rate")

def create_model():
    model = tf.keras.Sequential([
        tf.keras.Input(shape=(24,), dtype=tf.float32),
        tf.keras.layers.Dense(24, activation='relu'),
        tf.keras.layers.Dropout(.2),
        tf.keras.layers.Dense(8, activation='relu'),
        tf.keras.layers.Dense(1)
        ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.MeanSquaredError(),
                  metrics=['mean_squared_error'])

    return model

def train_model(model, num_epochs):
    hist = model.fit(train_features, train_labels, epochs=num_epochs, verbose=0)

    plot_hist(hist, num_epochs)

def evaluate_model(model):
    test_loss, test_acc = model.evaluate(test_features,  test_labels, verbose=2)

    print('\nTest accuracy:', test_acc)

def save_model(model, name):
    model.save_weights('./training/' + name)

def load_weights(model, name):
    model.load_weights('./training/' + name)

def model_predict(model, x):
    x = (np.expand_dims(x, 0))
    return model.predict(x, verbose=1)


