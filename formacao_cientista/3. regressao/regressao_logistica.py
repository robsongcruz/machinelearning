# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

base = pd.read_csv('Eleicao.csv', sep=";")
plt.scatter(base.DESPESAS, base.SITUACAO, color='blue')

correlacao = np.corrcoef(base.DESPESAS, base.SITUACAO)

X = base.iloc[:, 2].values
X = X[:, np.newaxis]

y = base.iloc[:, 1].values
modelo = LogisticRegression()
modelo.fit(X, y)

print('Params: ')
print(modelo.coef_)
print(modelo.intercept_)

plt.scatter(X, y)
X_teste = np.linspace(10, 3000, 100)

def model(x):
    return 1 / (1 + np.exp(-x))

r = model(X_teste * modelo.coef_ + modelo.intercept_).ravel()   #ravel(): matrix into array format
plt.plot(X_teste, r, color='red')

base_previsoes = pd.read_csv('NovosCandidatos.csv', sep=";")
despesas = base_previsoes.iloc[:, 1].values
despesas = despesas.reshape(-1, 1)

#predict_proba output => [prob to be zero, prob to be one] = [(1-p(x), p(x))]
previsoes_prob = modelo.predict_proba(despesas) 

previsoes_teste = modelo.predict(despesas)
base_previsoes = np.column_stack((base_previsoes, previsoes_prob, previsoes_teste))

print(base_previsoes)

    