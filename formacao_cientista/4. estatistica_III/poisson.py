# -*- coding: utf-8 -*-
from scipy.stats import poisson

# media de acidentes = lambda = 2 / dia
# prob(x = 3) = ?

lambd = 2
print(poisson.pmf(3, lambd))

# media de acidentes = lambda = 2 / dia
# prob(x <= 3) = ?

lambd = 2
print(poisson.cdf(3, lambd))

# media de acidentes = lambda = 2 / dia
# prob(x > 3) = ?

lambd = 2
print(poisson.sf(3, lambd))
