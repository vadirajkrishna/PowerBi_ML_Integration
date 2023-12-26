# 'dataset' holds the input data for this script
# load the model from disk
import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

random.seed(0)
X_test = dataset[dataset['Train/Test']=='Test'][['age', 'gender', 'bmi', 'children', 'smoker', 'region']]
y_test = dataset[dataset['Train/Test']=='Test'][['charges']]
filename = '<path>/linear_model.sav'  # Repalce the model path variable here 
loaded_model = pickle.load(open(filename, 'rb'))
y_pred = loaded_model.predict(X_test)
score = loaded_model.score(X_test, y_test)
dataset['y_pred'] = y_pred
intercept = loaded_model.intercept_
co_eff = loaded_model.coef_

#for some reason straight assignment is not possible as we do in Jupyter
ser_intercept = pd.Series(np.full(269, intercept)) #avoid hardcoding here
dataset['intercept'] = ser_intercept

co_eff_0 = co_eff[0] #note this assigns the array, different from Jupyter


for i in range(len(co_eff_0)):
    str_i = str(i)
    ser_coeff = pd.Series(np.full(269, co_eff_0[i]))
    dataset['coeff_'+ str_i] = ser_coeff


