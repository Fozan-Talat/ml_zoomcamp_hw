import pickle
from flask import Flask, request, jsonify
import numpy as np


app = Flask('poutcome')

input_dv = 'dv.bin'

with open(input_dv,'rb') as f_in:
    dv = pickle.load(f_in)


model_file = 'model2.bin'

with open(model_file,'rb') as f_in:
    model = pickle.load(f_in)


@app.route('/q4_predict', methods=['POST'])
def predict():
    client = request.get_json()
    X_client = dv.transform([client])
    y_pred = model.predict_proba(X_client)[0][1]
    poutcome = y_pred >= 0.5

    result = {
        'poutcome_probability': float(y_pred),
        'poutcome': bool(poutcome)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

