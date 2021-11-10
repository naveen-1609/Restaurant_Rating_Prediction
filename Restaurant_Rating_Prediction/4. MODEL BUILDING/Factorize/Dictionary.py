# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 22:39:50 2021

@author: NAVEEN
"""
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype
import pickle

df = pd.read_csv('C:/Users/NAVEEN/Restaurent_Rating_Prediction/Restaurent_Rating_Prediction/2. DATA CLEANING/DATASET.csv')

labels1, uniques1 = pd.factorize(df.cuisines)
cuisine_dict = dict(zip(uniques1,range(len(uniques1))))

labels2, uniques2 = pd.factorize(df.location)
location_dict = dict(zip(uniques2,range(len(uniques2))))

labels3, uniques3 = pd.factorize(df.menu_item)
menu_item_dict = dict(zip(uniques3,range(len(uniques3))))

labels4, uniques4 = pd.factorize(df.rest_type)
resrt_type_dict = dict(zip(uniques4,range(len(uniques4))))

pickle.dump(cuisine_dict, open('list.pkl','wb'))
pickle.dump(location_dict, open('list.pkl','wb'))
pickle.dump(menu_item_dict, open('list.pkl','wb'))
pickle.dump(resrt_type_dict, open('list.pkl','wb'))
model = pickle.load(open('list.pkl','rb'))