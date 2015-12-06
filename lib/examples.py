import os
import random

class Examples:
    def __init__(self, classifier):
        self.classifier = classifier

    def load(self, positives, negatives):
        pos_dir = 'dataset/test/pos'
        neg_dir = 'dataset/test/neg'
        data = self.load_dir(pos_dir, 1, positives) + self.load_dir(neg_dir, 0, negatives)
        random.shuffle(data)
        return self.classify(data)

    def classify(self, data):
        predictions = []
        for X, y in data:
            label, _ = self.classifier.classify(X)
            predictions.append(dict(q=X, predicted=label, real=y))
        return predictions

    def load_dir(self, dirname, label, size):
        data = []
        files = os.listdir(dirname)
        random.shuffle(files)
        for fname in files[:size]:
            for line in open(os.path.join(dirname, fname)):
                data.append((line, label))
        return data
