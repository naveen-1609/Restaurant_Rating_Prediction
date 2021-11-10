# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 23:17:00 2021

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
df = pd.read_csv("C:/Users/NAVEEN/Restaurent_Rating_Prediction/Datasets/NewDataSet.csv")


#Defining the independent variables and dependent variables
x = df.iloc[:,[2,3,5,6,7,8,9,11]]
y = df['rate']
#Getting Test and Training Set
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=353)
x_train.head()
y_train.head()

# Linear Regression
#Prepare a Linear Regression Model
reg = LinearRegression()
reg.fit(x_train,y_train)
y_pred=reg.predict(x_test)
linear = r2_score(y_test,y_pred)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.1,random_state=105)
DTree=DecisionTreeRegressor(min_samples_leaf=.0001)
DTree.fit(x_train,y_train)
y_predict=DTree.predict(x_test)
DT = r2_score(y_test,y_predict)

#Preparing Random Forest REgression
RForest=RandomForestRegressor(n_estimators=500,random_state=329,min_samples_leaf=.0001)
RForest.fit(x_train,y_train)
y_predict=RForest.predict(x_test)
RF = r2_score(y_test,y_predict)

ETree=ExtraTreesRegressor(n_estimators = 100)
ETree.fit(x_train,y_train)
y_predict=ETree.predict(x_test)
ETR = r2_score(y_test,y_predict)

#%%
print("Accuracy of Linear Model = {0} \n Accuracy of Decision Tree = {1} \n Accuracy of Random Forest = {2} \n Accuracy of Extra Tree Regressor = {3}".format(linear,DT,RF,ETR))