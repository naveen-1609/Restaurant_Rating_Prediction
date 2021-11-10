# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 11:28:39 2021

@author: NAVEEN
"""

import pandas as pd
import numpy as np
import pandas_profiling

df = pd.read_csv("Datasets/zomato.csv")

profile = df.profile_report(title="Restaurant Data Profile")
profile.to_file(output_file="RestoProfile.html")

# Pandas profiling makes Exploratory data analysis easy. The profile which is returned in the form of an HTML file.

#After perfoming EDA we can remove ['url','phone','dishes_liked']
# url and phone doesn't hold any chance in effecting the review and being said that dishesh_liked slightly may effect the rating but our problem statement is predicting the review .
# If our problem statement include recommendation system then we can include this param

#Location, approx_cost, cuisine, type, online, booking tables, review list. these are the params that effect the rating and review list can be used with NLP concepts.
