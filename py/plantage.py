# -*- coding: utf-8 -*-
"""Approche ML (salad).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12cOSuWNh363BApANRyGoh5SiGWtxYQnv

### **DATA LOAD**
"""

import pandas as pd

df = pd.read_csv('/content/data.csv')
df

"""### **DATA PREPARATION**

**Data separation as X and Y**
"""

y = df['day']
y

X = df.drop('day', axis=1)
X

"""**Data splitting**"""

from sklearn.model_selection import train_test_split


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=100)

X_train

X_test

"""### **MODEL BUILDING**

**RANDOM FOREST**

**Training the model**
"""

from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor(max_depth=2, random_state=100)
rf.fit(X_train, y_train)

"""**Applying the model to make a prediction**"""

y_rf_train_pred = rf.predict(X_train)
y_rf_test_pred = rf.predict(X_test)
y_rf_test_pred

"""**Evaluate model performance**"""

from sklearn.metrics import mean_squared_error, r2_score

rf_train_mse = mean_squared_error(y_train, y_rf_train_pred)
rf_train_r2 = r2_score(y_train, y_rf_train_pred)

rf_test_mse = mean_squared_error(y_test, y_rf_test_pred)
rf_test_r2 = r2_score(y_test, y_rf_test_pred)

rf_results = pd.DataFrame(['Random forest', rf_train_mse, rf_train_r2, rf_test_mse, rf_test_r2]).transpose()
rf_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
rf_results

"""**Data visualization of prediction results**"""

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5,5))
plt.scatter(x=y_test, y=y_rf_test_pred, c="#7CAE00" )

z = np.polyfit(y_test, y_rf_test_pred, 1)
p = np.poly1d(z)

plt.plot(y_test, p(y_test), '#F8766D')
plt.ylabel('Predicted values')
plt.xlabel('real test values')

"""**LINEAR REGRESSION** """

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

y_lr_train_pred = lr.predict(X_train)
y_lr_test_pred = lr.predict(X_test)

y_lr_train_pred

from sklearn.metrics import mean_squared_error, r2_score

lr_train_mse = mean_squared_error(y_train, y_lr_train_pred)
lr_train_r2 = r2_score(y_train, y_lr_train_pred)

lr_test_mse = mean_squared_error(y_test, y_lr_test_pred)
lr_test_r2 = r2_score(y_test, y_lr_test_pred)

lr_results = pd.DataFrame(['Linear regression', lr_train_mse, lr_train_r2, lr_test_mse, lr_test_r2]).transpose()
lr_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
lr_results

lr_results

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5,5))
plt.scatter(x=y_test, y=y_lr_test_pred, c="#7CAE00" ,alpha=0.3)

z = np.polyfit(y_test, y_lr_test_pred, 1)
p = np.poly1d(z)

plt.plot(y_test, p(y_test), '#F8766D')
plt.ylabel('Predicted values')
plt.xlabel('real test values')

"""**XGBoost regression**"""

from xgboost import XGBRegressor

my_model = XGBRegressor()
# Add silent=True to avoid printing out updates with each cycle (verbose = False)
my_model.fit(X_train,y_train, verbose=False)

test_predictions = my_model.predict(X_test)
train_predictions = my_model.predict(X_train)
from sklearn.metrics import mean_absolute_error
print("Mean Absolute Error : " + str(mean_absolute_error(test_predictions,y_test)))
print("Mean Absolute Error (train data): " + str(mean_absolute_error(train_predictions,y_train)))

from sklearn.metrics import mean_squared_error, r2_score

xgb_test_mse = mean_squared_error(y_test, test_predictions)
xgb_test_r2 = r2_score(y_test, test_predictions)

xgb_train_mse = mean_squared_error(y_train, train_predictions)
xgb_train_r2 = r2_score(y_train, train_predictions)

xgb_results = pd.DataFrame(['XGBregressor', xgb_train_mse, xgb_train_r2, xgb_test_mse, xgb_test_r2]).transpose()
xgb_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
xgb_results

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5,5))
plt.scatter(x=y_test, y=test_predictions, c="#7CAE00" )

z = np.polyfit(y_test, test_predictions, 1)
p = np.poly1d(z)

plt.plot(y_test, p(y_test), '#F8766D')
plt.ylabel('Predicted values')
plt.xlabel('real values')

"""**Support Vector Machine**"""

from sklearn import svm

model = svm.SVR()
model.fit(X_train,y_train)

svm_pred_test = model.predict(X_test)
svm_pred_train = model.predict(X_train)
from sklearn.metrics import mean_absolute_error
print("Mean Absolute Error : " + str(mean_absolute_error(svm_pred_test,y_test)))
print("Mean Absolute Error (train data): " + str(mean_absolute_error(svm_pred_train,y_train)))

from sklearn.metrics import mean_squared_error, r2_score

svm_test_mse = mean_squared_error(y_test, svm_pred_test)
svm_test_r2 = r2_score(y_test, svm_pred_test)

svm_train_mse = mean_squared_error(y_train, svm_pred_train)
svm_train_r2 = r2_score(y_train, svm_pred_train)

svm_results = pd.DataFrame(['SVM', svm_train_mse, svm_train_r2, svm_test_mse, svm_test_r2]).transpose()
svm_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
svm_results

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5,5))
plt.scatter(x=y_test, y=svm_pred_test, c="#7CAE00", alpha = 0.4 )

z = np.polyfit(y_test, svm_pred_test, 1)
p = np.poly1d(z)

plt.plot(y_test, p(y_test), '#F8766D')
plt.ylabel('Predicted values')
plt.xlabel('real values')

"""**k-nearest neighbors**"""

from sklearn.neighbors import KNeighborsRegressor
knr = KNeighborsRegressor(n_neighbors=1)
knr.fit(X_train, y_train)

knr_pred_test = knr.predict(X_test)
knr_pred_train = knr.predict(X_train)
from sklearn.metrics import mean_absolute_error
print("Mean Absolute Error : " + str(mean_absolute_error(knr_pred_test,y_test)))
print("Mean Absolute Error (train data): " + str(mean_absolute_error(knr_pred_train,y_train)))

from sklearn.metrics import mean_squared_error, r2_score

knr_test_mse = mean_squared_error(y_test, knr_pred_test)
knr_test_r2 = r2_score(y_test, knr_pred_test)

knr_train_mse = mean_squared_error(y_train, knr_pred_train)
knr_train_r2 = r2_score(y_train, knr_pred_train)

knr_results = pd.DataFrame(['K-nearest neighbors', knr_train_mse, knr_train_r2, knr_test_mse, knr_test_r2]).transpose()
knr_results.columns = ['Method', 'Training MSE', 'Training R2', 'Test MSE', 'Test R2']
knr_results

import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5,5))
plt.scatter(x=y_test, y=knr_pred_test, c="#7CAE00", alpha = 0.35 )

z = np.polyfit(y_test, knr_pred_test, 1)
p = np.poly1d(z)

plt.plot(y_test, p(y_test), '#F8766D')
plt.ylabel('Predicted values')
plt.xlabel('real test values')

"""### **MODEL COMPARISON**"""

df_models = pd.concat([lr_results, rf_results, xgb_results, svm_results,knr_results], axis=0)
df_models