# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from yellowbrick.regressor import ResidualsPlot


base = pd.read_csv('cars.csv')

base = base.drop(['Unnamed: 0'], axis = 1)

speed = base.iloc[:, 1].values

distance = base.iloc[:, 0].values

#np.corrcoef(x, y)
correlacao = np.corrcoef(speed, distance)

X = speed.reshape(-1, 1)    #turn into matrix format
y = distance

model = LinearRegression()
model.fit(X, y)

print(model.intercept_)
print(model.coef_)

plt.scatter(X, y)
plt.plot(X, model.predict(X), color='red')

#distance = 22, speed = ?
print(model.intercept_ + model.coef_*22)

model.predict([[22]])

visualizador = ResidualsPlot(model)
visualizador.fit(X, y)
visualizador.poof()