from flask import Flask,render_template,request
import pandas as pd
import pickle
car=pd.read_csv("cleaned data.csv")
model_loaded = pickle.load(open('pipe.pkl', 'rb'))
app=Flask(__name__)

@app.route('/')
def index():
    company=sorted(car["company"].unique())
    car_model=sorted(car["name"].unique())
    fuel_type=sorted(car["fuel-type"].unique(),reverse=True)
    year=sorted(car["year"].unique())
    return render_template('index.html',companies=company,car_models=car_model,years=year,fuel_types=fuel_type)

@app.route('/predict',methods=['POST'])
def predict():
    company=request.form.get('company')
    model=request.form.get('model')
    Year=(request.form.get('Year'))
    fuel_type=request.form.get('fuel_type')
    kilo_driven=int(request.form.get('kilo-driven'))
    prediction=model_loaded.predict(pd.DataFrame([[model,company,Year,kilo_driven,fuel_type]],columns=['name','company','year','kms_driven','fuel-type']))
    return str(prediction[0]);

if __name__=="__main__":
    app.run(debug=True)