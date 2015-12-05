import re
import codecs

class Vocabulary:
    def __init__(self, vocab_path='dataset/imdb.vocab'):
        self.vocab = dict()
        self.vocab_path = vocab_path

    def build(self):
        with codecs.open(self.vocab_path, 'r', 'UTF-8') as trainfile:
            words = [x.strip().rstrip('\n') for x in trainfile.readlines()]
            self.vocab = dict((c, i + 1) for i, c in enumerate(words))
        return self

    def size(self):
        return len(self.vocab)

    def tokenize(self, text):
        return [x.strip() for x in re.split('(\W+)', text) if x.strip()]

    def vectorize(self, text):
        text = text.lower()
        words = filter(lambda x: x in self.vocab, tokenize(text))
        return [self.vocab[w] for w in words]
