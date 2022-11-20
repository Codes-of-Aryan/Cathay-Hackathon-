#USE the US_CARRIER_DATASET to train a regression model 
#that predicts fuel burn (and thus carbon emissions) 
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

from sklearn.feature_selection import RFE
from sklearn.model_selection import GridSearchCV



#IMPORTING THE DATASET 
df = pd.read_csv('US_CARRIER_DATASET.csv')

#CLEANING THE DATA 
df = df.dropna() #Remove Null Value Records 
df = df[df.PASSENGERS != 0] #only considering passenger flights
df = df[df.DISTANCE != 0] # distance must not be 0
df = df[df.RAMP_TO_RAMP != 0] #Airtime must not be zero 

#PREPROCESSING 
# PAYLOAD, PASSENGERS, FREIGHT, DISTANCE, RAMP_TO_RAMP, AIR_TIME, AIRCRAFT_GROUP
# are all the factors that we will use from the database to train the model 

X = np.array(df[['PAYLOAD', 'PASSENGERS', 'FREIGHT', 'DISTANCE', 
                'RAMP_TO_RAMP', 'AIR_TIME','AIRCRAFT_GROUP']]).reshape(-1, 7) #Features 
y = np.array(df['FUEL_BURN']).reshape(-1, 1) #Target labels 
 
#Training a Linear Regression Model, STEPS INVOLVED: 
# 1. Fitting Data to Linear Regression Model 
# 2. Feature Regularization 
# 3. Hyperparameter Tuning using Grid Search CV 
# 4. Scoring the model using Test Data 

#Splitting dataset into training and testing data 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)

li_reg= LinearRegression()
li_reg.fit(X_train, y_train) #Fitting the model to Linear Regression

rfe = RFE(li_reg) #Feature Regularization 

hyper_params = [{'n_features_to_select': list(range(1, 14))}]   

#Hyperparameter tuning using Grid Search Cross Validation 
model_cv = GridSearchCV(estimator = rfe, 
                        param_grid = hyper_params, 
                        scoring= 'r2', 
                        cv = 5, 
                        verbose = 1,
                        return_train_score=True)  

model_cv.fit(X_train, y_train)   
accuracy = model_cv.score(X_test, y_test)

accuracy = round(accuracy*100, 3)
print('The accuracy of our model is {} %'.format(accuracy))