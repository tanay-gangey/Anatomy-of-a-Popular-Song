# -*- coding: utf-8 -*-

# This file trains a decision tree classifier on the data
# for one country.

from sklearn import tree
import pandas as pd
import numpy as np

# mean absolute percentage error
def mape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return (np.mean(np.abs((y_true - y_pred)/y_true)) * 100)

# prints the accuracy for a country
# the data is divided in 80-20 ratio, and is tested through mape
def acc(country):

    # data for a given country is read from it's corresponding file
    data = pd.read_csv(f"../../datasets/normalized-age-data-waf/{country}_waf.csv")
    data1=pd.read_csv(f"../../datasets/normalized-age-data-waf/{country}_waf.csv")
    age=data1['Age on Chart']
    data["Age_on_Chart"]=age

    # dropping the columns that we don't need to classify
    data=data.drop(['Unnamed: 0', 'Track Name', 'Artist', 'URL', 'Year','Month','Day','Region'], axis = 1)
    
    # splitting data into train and test
    data_train = data.iloc[0:15100]
    data_test = data.iloc[15100:]
    
    x_train, y_train = data_train.drop('Position', axis = 1) , data_train['Position']
    x_test, y_test = data_test.drop('Position', axis = 1), data_test['Position']

    clf = tree.DecisionTreeRegressor(max_depth = 10, min_samples_split = 30)
    clf = clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)
    
    print(f"Accuracy for {country}: ", 100-mape(y_test, y_pred))
    
acc("us")
acc("ph")
acc("au")
acc("gb")
acc("ch")