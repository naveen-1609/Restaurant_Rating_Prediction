# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:58:44 2021

@author: NAVEEN
"""
import numpy as np 
from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import logging


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
logging.basicConfig(filename='record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

@app.route('/')
def home():
    try:
        app.logger.info("This is a home page")
        return render_template('home.html')
    
    except "Error":
        app.logger.error("Error occured please check your route")
features_list = []
@app.route('/predict',methods=['POST'])
def predict():
    '''
    for rendering resutla on HTML GUI
    '''
    try:
        int_features = [int(x) for x in request.form.values()]
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = round(prediction[0],2)
        app.logger.info("This is predicted value rounded to two decimal values and the value is {0}".format(output))
        return render_template('home.html', prediction_text= "Restaurant Review is {}".format(output))
    
    except "Error":
        app.logger.error("Something is wrong :(")

    
@app.route('/locations',methods=['GET'])
def loc():
    try:
        filename = 'C:/Users/NAVEEN/Restaurent_Rating_Prediction/Restaurent_Rating_Prediction/4. MODEL BUILDING/Factorize/location.csv'
        data = pd.read_csv(filename, header=0)
        loclist = list(data.values.flatten())
        app.logger.info("This is a list of locations page")
        return render_template('listOfLoc.html', loclist = loclist)
    
    except "Error":
            app.logger.error("Unexpected error occured, please check the route")

@app.route('/cuisine')
def cui():
    try:
        filename = 'C:/Users/NAVEEN/Restaurent_Rating_Prediction/Restaurent_Rating_Prediction/4. MODEL BUILDING/Factorize/cuisine.csv'
        data = pd.read_csv(filename, header=0)
        cuilist = list(data.values.flatten())
        app.logger.info("This is a list of Cuisines page")
        return render_template('listOfCui.html', cuilist = cuilist)

    except "Error":
        app.logger.error("Unexpected error occured, please check the route")

@app.route('/menuitem')
def mi():
    try:
        filename = 'C:/Users/NAVEEN/Restaurent_Rating_Prediction/Restaurent_Rating_Prediction/4. MODEL BUILDING/Factorize/menu_item.csv'
        data = pd.read_csv(filename, header=0)
        milist = list(data.values.flatten())
        app.logger.info("This is a list of Menu items page")
        return render_template('listOfMI.html', milist = milist)
    
    except "Error":
        app.logger.error("Unexpected error occured, please check the route")
        
@app.route('/resttype')
def rt():
    try:
        filename = 'C:/Users/NAVEEN/Restaurent_Rating_Prediction/Restaurent_Rating_Prediction/4. MODEL BUILDING/Factorize/rest_type.csv'
        data = pd.read_csv(filename, header=0)
        rtlist = list(data.values.flatten())
        app.logger.info("This is a list of restaurant types page")
        return render_template('listOfRT.html', rtlist = rtlist)

    except "Error":
        app.logger.error("Unexpected error occured, please check the route")
        
@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    for direct API calls trought request
    '''
    try:
        data = request.get_json(forece = True)
        prediction = model.predict([np.array(list(data.values()))])
        output = prediction[0]
        app.logger.info("This displays the predited value onto the home page")
        return jsonify(output)
    
    except "Error":     
        app.logger.error("An unexpected error has occured")

if __name__ == "__main__":
    app.run(debug=True)