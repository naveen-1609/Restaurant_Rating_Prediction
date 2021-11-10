# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 23:30:17 2021

@author: NAVEEN
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import  ExtraTreesRegressor
from sklearn.model_selection import train_test_split
df = pd.read_csv("C:/Users/NAVEEN/Restaurent_Rating_Prediction/Restaurent_Rating_Prediction/2. DATA CLEANING/NewDataSetwithouen.csv")

#Defining the independent variables and dependent variables
x = df.iloc[:,[2,3,5,6,7,8,9,11]]
y = df['rate']
#Getting Test and Training Set
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=353)
x_train.head()
y_train.head()



ETree=ExtraTreesRegressor(n_estimators = 100)
ETree.fit(x_train,y_train)
y_predict=ETree.predict(x_test)
ETR = r2_score(y_test,y_predict)

print(ETR)