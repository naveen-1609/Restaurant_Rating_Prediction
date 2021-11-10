# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 08:34:38 2021

@author: NAVEEN
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

df = pd.read_csv("NewDataSet.csv")

df.head()

df1 = pd.read_csv('DATASET.csv')

labels1, uniques1 = pd.factorize(df1.rest_type)
resrt_type_dict = dict(zip(uniques1,range(len(uniques1))))

labels2, uniques2 = pd.factorize(df1.menu_item)
menu_item_dict = dict(zip(uniques2,range(len(uniques2))))

labels3, uniques3 = pd.factorize(df1.location)
location_dict = dict(zip(uniques3,range(len(uniques3))))

labels4, uniques4 = pd.factorize(df1.cuisines)
cuisine_dict = dict(zip(uniques4,range(len(uniques4))))

from sklearn.metrics import r2_score
from sklearn.ensemble import  ExtraTreesRegressor
from sklearn.model_selection import train_test_split

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
pickle.dump(ETree, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))