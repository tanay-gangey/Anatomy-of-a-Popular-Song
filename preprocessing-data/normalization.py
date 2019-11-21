# -*- coding: utf-8 -*-

import pandas as pd
from sklearn import preprocessing
import os
readpath = "path/to/read/from/"
writepath = "path/to/write/to/"
files = list()
for p,d,f in os.walk(readpath):
    for i in f:
        if "waf" in i:
            files.append(i)
        
        
minmaxscaler = preprocessing.MinMaxScaler()

for file in files:
    orig_data = pd.read_csv(readpath+file)
    orig_data['tempo'] = (orig_data['tempo'] - orig_data['tempo'].min())/(orig_data['tempo'].max()-orig_data['tempo'].min())
    orig_data['duration_ms'] = orig_data['duration_ms']/ 60000
    orig_data['duration_ms'] = (orig_data['duration_ms'] - orig_data['duration_ms'].min())/(orig_data['duration_ms'].max()-orig_data['duration_ms'].min())
    orig_data['instrumentalness'] = (orig_data['instrumentalness'] - orig_data['instrumentalness'].min())/(orig_data['instrumentalness'].max()-orig_data['instrumentalness'].min())
    orig_data['loudness'] = (orig_data['loudness'] - orig_data['loudness'].min())/(orig_data['loudness'].max()-orig_data['loudness'].min())
    orig_data = orig_data.rename(columns={'tempo':'norm_tempo','duration_ms':'norm_duration_min','instrumentalness':'norm_instrumentalness','loudness':'norm_loudness'})
    orig_data.to_csv(writepath+file)