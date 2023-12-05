#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
import numpy as np

def sort_dataset(dataset_df):
	#TODO: Implement this function
    sort_df=dataset_df.sort_values(by='year')
    return sort_df

def split_dataset(dataset_df):	
	#TODO: Implement this function
    dataset_df['salary']*=0.001
    train_df=dataset_df.iloc[:1718]
    test_df=dataset_df.iloc[1718:]
    
    X_train=train_df.drop(columns="salary",axis=1)
    Y_train=train_df['salary']
    
    X_test=test_df.drop(columns="salary",axis=1)
    Y_test=test_df['salary']

    return X_train,X_test,Y_train,Y_test

def extract_numerical_cols(dataset_df):
	#TODO: Implement this function
    num_f=['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']
    df=dataset_df[num_f]
    return df

def train_predict_decision_tree(X_train, Y_train, X_test):
	#TODO: Implement this function
    dt_cls=DecisionTreeRegressor()
    dt_cls.fit(X_train, Y_train)
    return dt_cls.predict(X_test)

def train_predict_random_forest(X_train, Y_train, X_test):
	#TODO: Implement this function
    rf_cls=RandomForestRegressor()
    rf_cls.fit(X_train,Y_train)
    return rf_cls.predict(X_test)

def train_predict_svm(X_train, Y_train, X_test):
	#TODO: Implement this function
    svm_cls=SVR()
    svm_cls.fit(X_train,Y_train)
    return svm_cls.predict(X_test)

def calculate_RMSE(labels, predictions):
	#TODO: Implement this function
    return np.sqrt(np.mean((predictions-labels)**2))

if __name__=='__main__':
	#DO NOT MODIFY THIS FUNCTION UNLESS PATH TO THE CSV MUST BE CHANGED.
	data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')
	
	sorted_df = sort_dataset(data_df)	
	X_train, X_test, Y_train, Y_test = split_dataset(sorted_df)
	
	X_train = extract_numerical_cols(X_train)
	X_test = extract_numerical_cols(X_test)

	dt_predictions = train_predict_decision_tree(X_train, Y_train, X_test)
	rf_predictions = train_predict_random_forest(X_train, Y_train, X_test)
	svm_predictions = train_predict_svm(X_train, Y_train, X_test)
	
	print ("Decision Tree Test RMSE: ", calculate_RMSE(Y_test, dt_predictions))	
	print ("Random Forest Test RMSE: ", calculate_RMSE(Y_test, rf_predictions))	
	print ("SVM Test RMSE: ", calculate_RMSE(Y_test, svm_predictions))


# In[ ]:




