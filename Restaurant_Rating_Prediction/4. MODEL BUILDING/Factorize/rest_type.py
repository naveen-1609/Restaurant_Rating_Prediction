# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 22:01:10 2021

@author: NAVEEN
"""

# importing libraries
import json
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype

df = pd.read_csv('C:/Users/NAVEEN/Restaurent_Rating_Prediction/Restaurent_Rating_Prediction/2. DATA CLEANING/DATASET.csv')

labels, uniques = pd.factorize(df.rest_type)
  


rest_type_dict = dict(zip(uniques,range(len(uniques))))
rest_type_dict=pd.DataFrame.from_dict(rest_type_dict, orient='index')
rest_type_dict.to_csv('rest_type.csv')