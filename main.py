from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

# Flask-App erstellen
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Eingabe als JSON empfangen
    data = request.json  # Erwartet {"Open": 100.0, "High": 102.0, "Low": 99.0, "Close": 101.0, "Volume": 500000}
    
    # In NumPy umwandeln
    X_input = np.array([[data["Open"], data["High"], data["Low"], data["Close"], data["Volume"]]])
    
    # Vorhersage generieren (Hier Dummy-Wert)
    probability = np.random.rand()  # Zufallswert als Platzhalter

    return jsonify({"probability_up": float(probability)})

# Flask-App starten
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
