from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/predict')
def predict():
    return jsonify(q=request.args.get('q'), predicted_class=0.0, prediction=0.9541)

if __name__ == '__main__':
    app.run(debug=True)
