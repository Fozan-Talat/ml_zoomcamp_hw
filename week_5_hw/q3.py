import pickle

input_dv = 'dv.bin'

with open(input_dv,'rb') as f_in:
    dv = pickle.load(f_in)

dv

input_model = 'model1.bin'

with open(input_model,'rb') as f_in:
    model = pickle.load(f_in)

model

client_data = {"job": "retired", "duration": 445, "poutcome": "success"}

X_client = dv.transform([client_data])

y_pred = model.predict_proba(X_client)[0][1]

print('Client in put data :' , client_data)

print('Probability that this client will get the credit:', y_pred)



