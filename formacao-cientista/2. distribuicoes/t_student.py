# -*- coding: utf-8 -*-
from scipy.stats import t
# T de student

# media_salrio=75; amostra=9; dp=10
# p(salario<80)=? ; t=1,5 (calculado); t=(media_amostra - media)/(S / sqrt(n))
# p/ t = 1.5, P ~ 92.5%

media_salario = 75
n_amostras = 9
dp = 10

graus_liberdade = n_amostras - 1
prob = t.cdf(1.5, 8)

# p(salario>=80)=?
prob1 = t.sf(1.5, 8) # or 1 - prob

print(f'P(sal<80) = {prob * 100}%')
print(f'P(sal>=80) = {prob1 * 100}%')