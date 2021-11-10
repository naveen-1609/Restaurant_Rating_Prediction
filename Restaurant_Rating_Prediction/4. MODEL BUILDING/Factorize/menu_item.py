# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 22:29:22 2021

@author: NAVEEN
"""

# importing libraries
import numpy as np
import pandas as pd
import json
from pandas.api.types import CategoricalDtype

df = pd.read_csv('C:/Users/NAVEEN/Restaurent_Rating_Prediction/Restaurent_Rating_Prediction/2. DATA CLEANING/DATASET.csv')

labels, uniques = pd.factorize(df.menu_item)
  


menu_item_dict = dict(zip(uniques,range(len(uniques))))
menu_item_dict=pd.DataFrame.from_dict(menu_item_dict, orient='index')
menu_item_dict.to_csv('menu_item.csv')