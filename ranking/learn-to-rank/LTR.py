# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:40:21 2019

@author: Tanay
"""
####DOES NOT WORK####

import pandas as pd
import os
import pyltr as ltr
from sklearn.model_selection import train_test_split 
import numpy as np

path = "../../datasets"

#reading the file
data = pd.read_csv(path + "/normalized-age-data-waf/au_waf.csv")
agedata = pd.read_csv(path+"/normalized-age-data/au.csv")

data['Age on Chart'] = agedata['Age on Chart']

#dropping unnecessary columns in data
data = data.drop("Unnamed: 0", axis = 1)

#sorting the data by query id
data = data.sort_values('Track Name')
print(data)

#setting query id and dependent variable
data_y = data['Position']
data_qid = data['Track Name']

#dropping textual columns
data_x = data.drop(['Artist','URL','Track Name','Region'], axis = 1)

#splitting into train and test
x_train,x_test, y_train, y_test, qid_train, qid_test = train_test_split(data_x,data_y, data_qid, test_size = 0.3, shuffle = False)

print(x_train)

#converting to a numpy array
train_x = np.asarray(x_train)
train_y = np.asarray(y_train)
test_x = np.asarray(x_test)
test_y = np.asarray(y_test)

#setting the metric to evaluate LTR
metric = ltr.metrics.AP(k=100)

#defing the model
model = ltr.models.LambdaMART(metric=metric, learning_rate = 0.05, max_leaf_nodes=10, min_samples_leaf=20, verbose=1)

print(train_x)

#fitting model
model.fit(train_x, train_y,qid_train)

#predicting on test
test_pred = model.predict(test_x)

#printing metrics and predicted value
print('Random ranking:', metric.calc_mean_random(qid_test, test_y))
print('Our model:', metric.calc_mean(qid_test, test_y, test_pred))
print(test_pred, test_y)
