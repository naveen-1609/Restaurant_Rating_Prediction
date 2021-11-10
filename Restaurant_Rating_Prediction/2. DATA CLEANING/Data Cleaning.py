# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:43:09 2021

@author: NAVEEN
"""
import pandas as pd
import numpy as np
import pandas_profiling
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/NAVEEN/Restaurent_Rating_Prediction/Datasets/zomato.csv")

df1 = df.copy()
df1 = df.drop(['url','phone','dish_liked'],axis = 1)

  ## Removing Duplicates
df1.duplicated().sum()
df1.drop_duplicates(inplace=True)

  ## Removing NAN values from dataset
df1.isnull().sum()
df1.dropna(how="any",inplace=True)

  ## Changing the column names

df1 = df1.rename(columns={'approx_cost(for two people)':'cost','listed_in(type)':'type','listed_in(city)':'city'})

## Exploring Cuisines
#drop all cuisines with less than 500 frequency

all_cuisines = dict()
for j in df1['cuisines']:
    for i in str(j).split(','):
        i = i.strip()
        if i not in all_cuisines:
            all_cuisines[i] = 1
        else:
            all_cuisines[i] = all_cuisines[i] + 1
#print(sorted(popular_cusines.items(), key=operator.itemgetter(1))[::-1])

cuisines_todel = []
for i in all_cuisines:
    if all_cuisines[i] < 500:
        cuisines_todel.append(i)
#the cuisines to be dropped
#cuisines_todel

#plot bar charts top cuisines 
popular_cuisines = all_cuisines.copy()
labels = []
freq = [] 

for i in cuisines_todel:
    del popular_cuisines[i]
#popular_cuisines contains all the cuisines which have frequency > 500

#drop all restaurant types with less than 500 frequency

#all_types contains all the types of restaurants available with their count
all_types = dict()
for j in df1['rest_type']:
    for i in str(j).split(','):
        i = i.strip()
        if i not in all_types:
            all_types[i] = 1
        else:
            all_types[i] = all_types[i] + 1
print("all types",all_types)

#todel_type consists of all the rest_types with freq < 500
todel_type = []
for i in all_types:
    if(all_types[i] < 500):
        todel_type.append(i)
        
#all_types contains all the types of restaurants available    
popular_rest_types = all_types.copy()        
for i in todel_type:
    del popular_rest_types[i]
print("popular types",popular_rest_types)
#popular_rest_types contains all the types of popular restaurants available

#bar graph for restaurant type

fig, ax = plt.subplots(figsize=(18, 8))
plt.bar(range(len(popular_rest_types)), list(popular_rest_types.values()))
plt.xticks(range(len(popular_rest_types)), list(popular_rest_types.keys()),fontsize=13, rotation=90)
plt.xlabel('Restaurant type', fontsize=16)
plt.ylabel('No of restaurants', fontsize=16)
plt.title('Restaurant Types ',fontsize=17)
plt.show()

# Drop the locations that have less than 100 restaurants
all_loc = dict()
for j in df1['location']:
    for i in str(j).split(','):
        i = i.strip()
        if i not in all_loc:
            all_loc[i] = 1
        else:
            all_loc[i] = all_loc[i] + 1
            
#popular_loc consists of all the locations that more than 100 restaurants
popular_loc = all_loc.copy()
for i in all_loc:
    if(all_loc[i] < 100):
        del popular_loc[i]
print("POPULAR LOCATIONS:  ",popular_loc)

#bar graph of all the popular locations 
fig, ax = plt.subplots(figsize=(18, 8))
plt.bar(range(len(popular_loc)), list(popular_loc.values()))
plt.xticks(range(len(popular_loc)), list(popular_loc.keys()),fontsize=13, rotation=90)
plt.xlabel('Locations', fontsize=16)
plt.ylabel('No of restaurants', fontsize=16)
plt.title('No of restaurants in the location',fontsize=17)
plt.show()

  ## Some transformations

df1['cost'] = df1['cost'].astype(str)  #changing cost to string
df1['cost'] = df1['cost'].apply(lambda x: x.replace(',','.')) #using lambda function to replace ',' from cost
df1['cost'] = df1['cost'].astype(float) #changing cost to float

# reading the costs
b = df1.cost.unique()

  ## Reading the ratings
a = df1['rate'].unique()

  ## Removing '/5' from rates
df1 = df1.loc[df1.rate != 'NEW'] #it skips if there is no rating for the restaurant
df1 = df1.loc[df1.rate != '-'].reset_index(drop=True) # it deletes the index instead of inserting it back
remove_slash5 = lambda x: x.replace('/5','') if type(x) == np.str else x
df1.rate = df1.rate.apply(remove_slash5).str.strip().astype('float') #applying lambda function onto the data

  ## Adjusting the Column names
df1.name = df1.name.apply(lambda x:x.title()) #returns the first leter of every record as an upper case
df1.online_order.replace(('Yes','No'),(True,False),inplace=True)
df1.book_table.replace(('Yes','No'),(True,False),inplace=True)
#%%
  ## Encode the input variables
# for converting variables int enumerables
def Encode(df1):
    for column in df1.columns[~df1.columns.isin(['rate','cost','votes'])]:
        df1[column],label = df1[column].factorize()[0]
    return df1

#%%
df1_en = Encode(df1.copy())

# Performing pandas profiling once again
profile = df1_en.profile_report(title="Restaurant Data Profile (Encoded)")
profile.to_file(output_file="Encoded_RestoProfile.html")

## Distribution of the ratings
df1New = df1_en.copy()
sns.set(style='white', palette='muted', color_codes=True)
fig, ax = plt.subplots(figsize=(12, 5))
sns.despine(left=True)
sns.distplot(df1New['rate'], bins=30, color='navy')
ax.set_title("Restaurant's Rate Distribution", size=14)
ax.set_xlabel('Restaurant Rate')
plt.setp(ax, yticks=[])
plt.show()

## Box Plot
fig, ax = plt.subplots(figsize=(18, 8))
bx = df1New.boxplot('rate')
# we see that there are a few outliers below rating 2.5
# Since there are few outliers, we have to count these outliers and deal with them

c1 = 0
for i in df1New['rate']:
    if i<2.5:
        c1+=1
print(c1)


#there are a total of 183 outliers so when compared to the remaining data it is of small size so we can eliminate or discard these outliers

# Dropping the data points less where ratings less than 2.5
dfNew = df1New.copy()
dfNew = df1New[dfNew.rate >= 2.5]
dfNew.head()

#%%
DF = df1.copy()
DF = df1[df1.rate>=2.5]
DF.head()
#%%
fig, ax = plt.subplots(figsize=(18, 8))
plt.bar(range(len(popular_cuisines)), list(popular_cuisines.values()))
plt.xticks(range(len(popular_cuisines)), list(popular_cuisines.keys()),fontsize=13, rotation=90)
plt.xlabel('Cuisines', fontsize=16)
plt.ylabel('No of restaurants', fontsize=16)
plt.title('No of restaurants serving the cuisine',fontsize=17)
plt.show()

dfNew.to_csv('NewDataSeten.csv', index=False)
#%%
DF.to_csv('DATASET.csv', index = False)