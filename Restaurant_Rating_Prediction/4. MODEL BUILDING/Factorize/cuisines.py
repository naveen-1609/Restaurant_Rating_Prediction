# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 22:25:33 2021

@author: NAVEEN
"""

# importing libraries
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype
import json

df = pd.read_csv('C:/Users/NAVEEN/Restaurent_Rating_Prediction/Restaurent_Rating_Prediction/2. DATA CLEANING/DATASET.csv')

labels, uniques = pd.factorize(df.cuisines)


cuisine_dict = dict(zip(uniques,range(len(uniques))))
cuisine_dict=pd.DataFrame.from_dict(cuisine_dict, orient='index')
cuisine_dict.to_csv('cuisine.csv')