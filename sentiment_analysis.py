from flask import Flask, render_template, request, jsonify
from lib.classifier import Classifier
from lib.examples import Examples
import threading

print(" - Starting up application")
lock = threading.Lock()
app = Flask(__name__)

class App:
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state

    def classifier(self):
        with lock:
            if getattr(self, '_classifier', None) == None:
                print(" - Building new classifier - might take a while.")
                self._classifier = Classifier().build()
                print(" - Done!")
            return self._classifier

t = threading.Thread(target=App().classifier)
t.daemon = True
t.start()

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/predict')
def predict():
    q = request.args.get('q')
    label, prediction = App().classifier().classify(q)
    return jsonify(q=q, predicted_class=label, prediction=prediction)

@app.route('/examples')
def examples():
    examples = Examples(App().classifier()).load(5, 5)
    return jsonify(items=examples)

if __name__ == '__main__':
    app.run(debug=True)
