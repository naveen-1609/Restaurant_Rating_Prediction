# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:18:36 2021

@author: NAVEEN
"""
# importing libraries
import numpy as np
import json
import pandas as pd
from pandas.api.types import CategoricalDtype
df = pd.read_csv('C:/Users/NAVEEN/Restaurent_Rating_Prediction/Restaurent_Rating_Prediction/2. DATA CLEANING/DATASET.csv')
  
labels, uniques = pd.factorize(df.location)
  
print("Numeric Representation : \n", labels)
print("Unique Values : \n", uniques)

location_dict = dict(zip(uniques,range(len(uniques))))
location_dict=pd.DataFrame.from_dict(location_dict, orient='index')
location_dict.to_csv('location.csv')