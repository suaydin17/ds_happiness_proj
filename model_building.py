# -*- coding: utf-8 -*-
"""
Created on Fri May  5 17:43:11 2023

@author: susum
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df= pd.read_csv("C:/Users/susum/Documents/ds_happiness_proj/world-happiness-report-2021.csv")

#choose relevant columns
df_model = df.drop(['Country name','Standard error of ladder score','upperwhisker','lowerwhisker','Ladder score in Dystopia','Dystopia + residual'], 
                   axis = 1)

#get dummy data
df_dum = pd.get_dummies(df_model)

#train test split
from sklearn.model_selection import train_test_split

X= df_dum.drop('Ladder score', axis=1)
y= df_dum['Ladder score'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)


#multiple linear regression
import statsmodels.api as sm

X_sm= sm.add_constant(X)
model = sm.OLS(y, X_sm)
print(model.fit().summary())

#random forest model
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestRegressor
rf= RandomForestRegressor()
print(np.mean(cross_val_score(rf, X_train, y_train, scoring= 'neg_mean_absolute_error', cv=3)))

#gridsearch and hyperparameter optimization
from sklearn.model_selection import GridSearchCV

parameters = {'n_estimators':range(10,300,20), 'criterion':('mse','mae'), 'max_features': ('auto', 'sqrt','Log2')}

gs= GridSearchCV(rf, parameters, scoring='neg_mean_absolute_error', cv=3)
gs.fit(X_train,y_train)

print(gs.best_score_)
print(gs.best_estimator_)

#prediction
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(y_test, tpred_rf))