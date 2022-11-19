#USE the US_CARRIER_DATASET to train a regression model 
#that predicts fuel burn (and thus carbon emissions) 
import numpy as np 
import pandas as pd 
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#IMPORTING THE DATASET 
df = pd.read_csv('US_CARRIER_DATASET.csv')

#CLEANING THE DATA 
df = df.dropna() #Remove Null Value Records 
df = df[df.PASSENGERS != 0] #only considering passenger flights
df = df[df.DISTANCE != 0] # distance must not be 0

#PREPROCESSING 
# PAYLOAD, PASSENGERS, FREIGHT, DISTANCE, RAMP_TO_RAMP, AIR_TIME, AIRCRAFT_GROUP
# are all the factors that we will use from the database to train the model 

X = np.array(df[['PAYLOAD', 'PASSENGERS', 'FREIGHT', 'DISTANCE', 'RAMP_TO_RAMP', 'AIR_TIME','AIRCRAFT_GROUP']]).reshape(-1, 7)
y = np.array(df['FUEL_BURN']).reshape(-1, 1)
 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, stratify=y)
regr = LinearRegression()
  
regr.fit(X_train, y_train)
print(regr.score(X_test, y_test))