import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import inputScript
app = Flask(__name__)
model = pickle.load(open('Phishing_Website.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict')
def predict():
    return render_template('main.html')


ans = ""   
bns = ""   
@app.route('/predict2', methods=['POST'])
def y_predict():
    url=request.form['URL']
    checkprediction =inputScript.main(url)
    prediction = model.predict(checkprediction)
    output=prediction[0]
    if output==1:
        pred="This is a legitimate website"
        return render_template('main.html', bns=pred)
    else:
        pred="This site is unsafe"
        return render_template('main.html', ans=pred)
    
 

if __name__=='__main__':
    app.run( debug=True)