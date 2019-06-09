# Importing the libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
import pickle
import requests
import json
# Importing the dataset
df = pd.read_csv('cleaned-fifa-data.csv')

#Setting feature and predicted variables
features = ['Height','Age','Crossing','Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
       'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
       'Marking', 'StandingTackle', 'SlidingTackle','Skill Moves']
features2 = ['Age','Crossing','Finishing', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Strength', 'LongShots',
       'Interceptions', 'Positioning', 'Vision', 'Penalties',
       'Marking', 'StandingTackle', 'SlidingTackle','Skill Moves']
X = df[features]
y = df.Position
y = y.astype(int)
y = df.Position
# Splitting the dataset into the Training set and Test set
train_X, val_X, train_y, val_y = train_test_split(X,y,test_size=0.2,random_state=0)

# Fitting Simple Linear Regression to the Training set
rf_mod = RandomForestClassifier(max_depth=100,random_state=0,max_features=14,min_samples_split=40)
rf_mod.fit(train_X,train_y)

# Predicting the Test set results
rf_pred = rf_mod.predict(val_X)

# Saving model to disk
pickle.dump(rf_mod, open('model.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))