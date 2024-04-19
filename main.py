import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib
import warnings
warnings.filterwarnings('ignore')




app = Flask(__name__)


model = joblib.load("model.pkl")



@app.route('/')
def home():

    return render_template('admin.html')

@app.route('/index')
def index():

    return render_template('index1.html')

@app.route('/adminval',methods=['POST','GET'])
def adminval():
    if request.method == 'POST':
        uname = request.form.get('username')
        upass = request.form.get('password')
        if uname == 'admin' and upass == '1234':
            return render_template('index1.html')
        else:
            return render_template('admin.html', msg = 'Invalid Data')

@app.route('/predict', methods=['POST'])
def predict():
    data = []
    loc = float(request.form.get('lines', False))
    vg= float(request.form.get('cc', False))
    evg= float(request.form.get('ec', False))
    ivg = float(request.form.get('dc', False))
    n = float(request.form.get('methods', False))
    v = float(request.form.get('hcm', False))
    l = float(request.form.get('tline', False))
    d = float(request.form.get('dp', False))
    

    data.append(loc)
    data.append(vg)
    data.append(evg)
    data.append(ivg)
    data.append(n)
    data.append(v)
    data.append(l)
    data.append(d)
    
    print(data)
    datas = [data]



    #df_transform = pd.DataFrame.from_dict([data])
    prediction = model.predict([data])
    print(prediction)
    msg = prediction[0]
    return render_template('result.html', msg = msg)


if __name__ == '__main__':
    app.run(debug=True, port=2000)
