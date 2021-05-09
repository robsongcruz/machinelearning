# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')

dados = pd.read_csv('AirPassengers.csv', parse_dates=['Month'], index_col=['Month'], date_parser=dateparse)

print(dados.index)

ts = dados['#Passengers']
           
print(ts[datetime(1949, 2, 1)])

print(ts['1949'])

print(ts['1950-01' : '1950-07'])

print(ts[: '1950-03'])

# Data Máxima
print(ts.index.max())
# Data Mínima
print(ts.index.min())

#plt.plot(ts)

ts_ano = ts.resample('A').sum()

#plt.plot(ts_ano)

ts_mes = ts.groupby([lambda reg: reg.month]).mean()

plt.plot(ts_mes)


