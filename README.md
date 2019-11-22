# Anatomy-of-a-Popular-Song

## Problem Statement
Using audio features of a sound track, we try to find out what makes a song popular.
Through  our  work  we  try  to  glean  insights  into  what
attributes  make  a  song  popular  in  different  regions  of  the
world.  We  also  try  to  rank  songs  in  a  relative  order  using
Machine Learning algorithms.

## Datasets
The datasets are collected through spotify's spotifycharts website. The dataset was collected through the script [here](https://github.com/davafons/spotify-worldwide-ranking). 

The datasets are present in the [datasets](datasets) folder.

The attribute descriptions are given in the [Attributes_Descriptions](Attributes_Descriptions.md) file.

## How-to-execute files

### Collecting data

To collect the data just run the makefile on [spotify-worldwide-ranking](https://github.com/davafons/spotify-worldwide-ranking).

### Preprocessing data

First run [preprocessing-data/normalization.py](preprocessing-data/normalization.py). This will normalize loudness, instrumentalness, duration to minutes, and tempo, and save the files to [datasets/normalized-data](datasets/normalized-data).

Then [preprocessing-data/add_age.py](preprocessing-data/add_age.py) will add 'Age on Chart' column to all the files.

### Drawing inferencing through plots

The files for these are present in attribute-inference folder.

[attribute-inference/correlograms.R](attribute-inference/correlograms.R) draws out the graphs showing how the attributes are correlated to each other for a given country.

[attribute-inference/plot.rmd](attribute-inference/plot.rmd) contains the plots for other inferences that we've drawn in the report.

### Ranking the songs

The ranking folder contains three folders, decision-tree, knn, and learn-to-rank. 

#### decision-tree

[ranking/decision-tree/R-tree.R](ranking/decision-tree/R-tree.R) plots the recursive partitioning and regression tree for the attributes. 

[ranking/decision-tree/tree_self_country.py](ranking/decision-tree/tree_self_country.py) applies a decision tree classifier (80/20 train/test) to the data for a given country and outputs the accuracy based on MAPE (mean absolute percentage error).

[ranking/decision-tree/tree_multiple_countries.py](ranking/decision-tree/tree_multiple_countries.py) learns a decision tree classifier from one country and tests it on different country.

#### knn

[ranking/knn/Testtrain on same.ipynb](ranking/knn/Testtrain on same.ipynb) Given a countries name it applies a KNN-Regressor model and gives the K value that gives the best accuracy. It also plots the elbow curve andd prints the value of accuracy for that perticular K value
[ranking/knn/Diff Countries KNN.ipynb](ranking/knn/Diff Countries KNN.ipynb)This contains 2 funcction train and test .The train function trains the KNN modelgiven the country name. The test basically finds the accuracy of a model on a particular country

#### learn-to-rank

[ranking/learn-to-rank/LTR.py](ranking/learn-to-rank/LTR.py) uses LambdaMART to try to predict the relative ranking between songs. This however does not give satisfactory results.