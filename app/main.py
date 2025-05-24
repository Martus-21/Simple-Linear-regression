import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)) 

from flask import Flask, request, jsonify
from model import SimpleLinearRegression

app = Flask(__name__)
model = SimpleLinearRegression()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    if not data or 'x' not in data:
        return jsonify({'error': 'Please provide x value'}), 400
    
    try:
        prediction = model.predict(data['x'])
        return jsonify({'prediction': prediction})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/')
def home():
    return jsonify({
        "message": "Linear Regression API",
        "usage": {
            "method": "POST",
            "endpoint": "/predict",
            "required": {"x": "numeric value"},
            "example_request": {"x": 5},
            "example_response": {"prediction": model.predict(5)}
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)