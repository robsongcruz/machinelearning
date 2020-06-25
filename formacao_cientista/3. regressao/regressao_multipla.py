# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

import statsmodels.formula.api as sm


base = pd.read_csv('mt_cars.csv')

base = base.drop(['Unnamed: 0'], axis = 1)

X = base.iloc[:, 2].values

y = base.iloc[:, 0].values

correlacao = np.corrcoef(X, y)

X = X.reshape(-1, 1)

modelo = LinearRegression()
modelo.fit(X, y)

print(modelo.intercept_)

print(modelo.coef_)

#R2 - coeficiente de determinação
print(modelo.score(X, y))

#Coeficiente de determinação ajustado -  modelos de variaveis multiplas
previsoes = modelo.predict(X)
modelo_ajustado = sm.ols(formula='mpg ~ disp', data=base)

modelo_treinado = modelo_ajustado.fit()

print(modelo_treinado.summary())

plt.scatter(X, y)
plt.plot(X, previsoes, color='red')

print('Previsão')
print(modelo.predict([[200]]))

# Modelo com multiplas variaveis

X1 = base.iloc[:, 1:4].values
y1 = base.iloc[:, 0].values

modelo_multiplo = LinearRegression()
modelo_multiplo.fit(X1, y1)

print(modelo_multiplo.score(X1, y1))

modelo_m_ajustado = sm.ols(formula='mpg ~ disp + cyl + hp', data=base)
modelo_m_treinado = modelo_m_ajustado.fit()
print(modelo_m_treinado.summary())

#Previsao Multiplp
print('Predicao Multiplas Variaveis')
Xmult = np.array([[4, 200, 100]])
print(modelo_multiplo.predict(Xmult))









