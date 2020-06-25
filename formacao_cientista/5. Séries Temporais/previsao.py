# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from statsmodels.tsa.arima_model import ARIMA
from pyramid.arima import auto_arima


dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

dados = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col=['Month'], date_parser=dateparse)

ts = dados['Passengers']

plt.plot(ts)

# ARIMA

# p: Número de termos autoregressivos
# q: janela da média móvel
# d: número de diferenças não sazonais

p = 2
q = 1
d = 2 
modelo = ARIMA(ts, order=(p, q, d))

modelo_treinado = modelo.fit()

print(modelo_treinado.summary())

previsoes = modelo_treinado.forecast(steps = 3)[0]

# Os graficos vão ser unidos
eixo = ts.plot()

modelo_treinado.plot_predict('1960-01-01', '1962-01-01', ax = eixo, plot_insample=True)

#ARIMA autoajustado
#pip install pyramid-arima

modelo_auto = auto_arima(ts=12, n=12, seasonal=True, trace=True)
modelo_auto.summary()
novas_previsoes = modelo_auto.predict(n_periods=2)







