# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:40:03 2019

@author: Tanay
"""
'''
for getting normalized-age-data change path_out
change if("waf" not in )
change 23 to 9 in df.insert(23,'Age on Chart', [0 for i in range(len(df))], True)
'''
import pandas as pd
import os

#setting both read and write path
path = os.getcwd() + '../normalized-data/'
path_out = os.getcwd() + '../normalized-age-data-waf/'

#now when a song first appears this adds the song as key to a dictionary and
#increments the dictionary value by 1. When a song appears again, if it is in
#he dictionary it will increment value giving it's age on chart till that day 
for i in os.listdir(path):
    if("waf" in i):
        dictofsongs = dict()
        df = pd.read_csv(path+i)
        df.insert(23,'Age on Chart', [0 for i in range(len(df))], True)
        for idx,row in df.iterrows():
            if(row['Track Name'] not in dictofsongs):
                dictofsongs[row['Track Name']] = 0
            else:
                dictofsongs[row['Track Name']]+=1
                df.at[idx,'Age on Chart'] = dictofsongs[row['Track Name']]

        df.to_csv(path_out+i)
            
