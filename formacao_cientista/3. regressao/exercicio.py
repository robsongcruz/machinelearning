# -*- coding: utf-8 -*-
import pandas as pd
from sklearn.linear_model import LinearRegression

base = pd.read_csv('women.csv')

base = base.drop(['Unnamed: 0'], axis = 1)

height = base.iloc[:, 0].values
height = height.reshape(-1, 1)

weight = base.iloc[:, 1].values
weight = weight.reshape(-1, 1)

modelo = LinearRegression()

modelo.fit(height, weight)

#y = b + ax ; weight=? ; height = 70
print(modelo.intercept_ + modelo.coef_*70)

print(16 + (-3)*3)