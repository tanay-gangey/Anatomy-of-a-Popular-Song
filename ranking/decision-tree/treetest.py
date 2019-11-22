# -*- coding: utf-8 -*-

from sklearn import tree
import pandas as pd
import numpy as np

data = pd.read_csv("../../datasets/normalized-age-data-waf/us_waf.csv")
data1=pd.read_csv("../../datasets/normalized-age-data-waf/us_waf.csv")
age=data1['Age on Chart']

data["Age_on_Chart"]=age
data=data.drop(['Unnamed: 0', 'Track Name', 'Artist', 'URL', 'Year','Month','Day','Region'], axis = 1)

data_train = data.iloc[0:15100]
data_test = data.iloc[15100:]

x_train, y_train = data_train.drop('Position', axis = 1) , data_train['Position']
x_test, y_test = data_test.drop('Position', axis = 1), data_test['Position']

clf = tree.DecisionTreeRegressor(max_depth = 10, min_samples_split = 30)
clf = clf.fit(x_train, y_train)
print(clf.tree_.node_count)
print(clf.tree_.max_depth)
y_pred_t = clf.predict(x_test)

def mape(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return (np.mean(np.abs((y_true - y_pred)/y_true)) * 100)

tree.export_graphviz(clf,out_file = 'tree.dot')
print(clf.score(x_test,y_test))
print(mape(y_test, y_pred_t))