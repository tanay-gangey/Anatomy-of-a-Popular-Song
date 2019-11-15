# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:40:03 2019

@author: Tanay
"""
import pandas as pd
import os
path = os.getcwd() + '/normdata/'
path_out = os.getcwd() + '/norm-age-data/'

for i in os.listdir(path):
    if("waf"  not in i):
        dictofsongs = dict()
        df = pd.read_csv(path+i)
        df.insert(9,'Age on Chart', [0 for i in range(len(df))], True)
        for idx,row in df.iterrows():
            if(row['Track Name'] not in dictofsongs):
                dictofsongs[row['Track Name']] = 0
            else:
                dictofsongs[row['Track Name']]+=1
                df.at[idx,'Age on Chart'] = dictofsongs[row['Track Name']]

        df.to_csv(path_out+i)
            