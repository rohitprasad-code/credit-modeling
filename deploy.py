from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# load the model
model = pickle.load(open('./model/loan_v1.sav', 'rb'))

# home page
@app.route('/')
def home():
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    p1 = float(request.form['Column Name'])
    # Add multiple columns here
    
    res = model.predict([[p1]]) [0]
    
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run()