# -*- coding: utf-8 -*-
from scipy.stats import norm

#prob=? / peso < 6
lim = 6
media = 8
desvio_padrao = 2
print(norm.cdf(lim, media, desvio_padrao))

#prob=? / peso > 6 OBS: 1 - prob(peso < 6)
print(norm.sf(lim, media, desvio_padrao))

#prob=? / peso < 6 ou peso > 10
lim_2 = 10
prob = norm.cdf(lim, media, desvio_padrao) + norm.sf(lim_2, media, desvio_padrao)
print(prob)

#prob=? / peso > 6 e peso < 10
prob2 = norm.cdf(lim_2, media, desvio_padrao) - prob = norm.cdf(lim, media, desvio_padrao)