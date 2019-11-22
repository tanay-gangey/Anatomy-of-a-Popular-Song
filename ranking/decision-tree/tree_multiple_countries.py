# -*- coding: utf-8 -*-

from sklearn import tree
import pandas as pd
import numpy as np

# return mean absolute percentage error
def mape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return (np.mean(np.abs((y_true - y_pred)/y_true)) * 100)

# train the tree on a country and return the model
def train(country):
    data = pd.read_csv(f"../../datasets/normalized-age-data-waf/{country}_waf.csv")
    data1=pd.read_csv(f"../../datasets/normalized-age-data-waf/{country}_waf.csv")
    age=data1['Age on Chart']
    
    data["Age_on_Chart"]=age
    data=data.drop(['Unnamed: 0', 'Track Name', 'Artist', 'URL', 'Year','Month','Day','Region'], axis = 1)
    
    x_train, y_train = data.drop('Position', axis = 1) , data['Position']
    clf = tree.DecisionTreeRegressor(max_depth = 10, min_samples_split = 30)
    clf = clf.fit(x_train, y_train)

    return clf

# test the model on a different country
def test(country, model):
    data = pd.read_csv(f"../../datasets/normalized-age-data-waf/{country}_waf.csv")
    data1=pd.read_csv(f"../../datasets/normalized-age-data-waf/{country}_waf.csv")
    age=data1['Age on Chart']
    
    data["Age_on_Chart"]=age
    data=data.drop(['Unnamed: 0', 'Track Name', 'Artist', 'URL', 'Year','Month','Day','Region'], axis = 1)
    
    x_test, y_test = data.drop('Position', axis = 1), data['Position']
    
    y_pred = model.predict(x_test)
    
    return mape(y_test, y_pred)

model=train("us")
print("MAPE for ph: ", test("ph",model))
print("MAPE for gb: ", test("gb",model))
print("MAPE for ch: ", test("ch",model))