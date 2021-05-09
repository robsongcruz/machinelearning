# -*- coding: utf-8 -*-
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

dados = norm.rvs(size = 100)   #gerar 100 amostras normalmente distribuidas

stats.probplot(dados, plot=plt)
teste = stats.shapiro(dados)
print(f'Teste: {teste}')


