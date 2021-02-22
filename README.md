# lcs-neuralnet-predictor
This neural net uses team stats as features in order to predict the overall win rate.

## Usage

Running model-repl will pull up an interactive user interface. From here there are a few commands,
with **create** initializing an empty net, **train** training the model on the dataset, **evaluate** testing the model
against a test set, **save** *filepath* saving
the weights at the given *filepath*, load filepath loading the weights at filepath, and predict x predicting
the output given a vector of features x.

## About

The network trains in cycles of 500 epochs, and the loss algorithm uses mean squared error. The optimizer is Adam which
uses a learning rate of 0.001.

## Data

All data was retrieved from https://gol.gg/esports/home/
