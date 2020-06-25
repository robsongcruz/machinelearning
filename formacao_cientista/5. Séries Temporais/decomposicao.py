# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

dados = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col=['Month'], date_parser=dateparse)

print(dados.index)

ts = dados['Passengers']

decomposicao = seasonal_decompose(ts)

tendencia = decomposicao.trend
sazonal = decomposicao.seasonal
aleatorio = decomposicao.resid

plt.plot(aleatorio)
plt.plot(sazonal)
plt.plot(tendencia)

plt.subplot(4, 1, 1)
plt.plot(ts, label='Original')
plt.legend(loc = 'best')

plt.subplot(4, 1, 2)
plt.plot(tendencia, label='Tendência')
plt.legend(loc = 'best')

plt.subplot(4, 1, 3)
plt.plot(sazonal, label='Sazonalidade')
plt.legend(loc = 'best')

plt.subplot(4, 1, 4)
plt.plot(ts, label='Aleatoriedade')
plt.legend(loc = 'best')

plt.tight_layout()
