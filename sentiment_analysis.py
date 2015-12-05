from flask import Flask, render_template, request, jsonify
from lib.classifier import Classifier

print("#" * 80)
print(" - Starting up application")
app = Flask(__name__)
print(" - Building new classifier - might take a while.")
classifier = Classifier().build()
print("#" * 80)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/predict')
def predict():
    q = request.args.get('q')
    label, prediction = classifier.classify(q)
    return jsonify(q=q, predicted_class=label, prediction=prediction)

@app.route('/examples')
def examples():
    examples = [
        dict(q="teste 1", actual=1.0, predicted=0.0),
        dict(q="teste 2", actual=1.0, predicted=1.0)
    ]
    return jsonify(items=examples)

if __name__ == '__main__':
    app.run(debug=True)
