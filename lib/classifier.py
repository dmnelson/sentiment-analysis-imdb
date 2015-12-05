from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.preprocessing.sequence import pad_sequences
from keras.regularizers import l2
import numpy as np
from lib.vocabulary import Vocabulary

class Classifier:
    def __init__(self, max_words = 500):
        self.model = None
        self.vocab = Vocabulary()
        self.max_words = max_words

    def build(self):
        self.vocab.build()
        model = Sequential()
        model.add(Embedding(self.vocab.size(), 128))
        model.add(LSTM(128))
        model.add(Dropout(0.5))
        model.add(Dense(1, W_regularizer=l2(0.01)))
        model.add(Activation('sigmoid'))

        model.load_weights("lib/imdb_lstm.w")
        model.compile(loss='binary_crossentropy', optimizer='adam', class_mode="binary")

        self.model = model
        return self

    def pad(self, X):
        return pad_sequences(X, maxlen=self.max_words)

    def classify(self, X):
        inp = [self.vocab.vectorize(X)]
        inp = np.array(self.pad(inp))
        y = self.model.predict(inp)[0][0]
        return (round(y), y)
