# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 13:13:24 2021

@author: NAVEEN
"""

import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'online_order': 1,'book_table': 1,'votes': 100,'location': 32,'rest_type': 7,'cuisines': 33,'cost': 400,'menu_item':0})

print(r.json())