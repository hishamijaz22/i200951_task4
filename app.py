from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Load the trained model
# For simplicity, we'll use the global scope here
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
clf.fit(X, y)  # Assuming X and y are already loaded from the Iris dataset

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array(data['features']).reshape(1, -1)
    prediction = clf.predict(features)
    return jsonify({'prediction': prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
