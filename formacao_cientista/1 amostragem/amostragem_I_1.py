
import numpy as np
from math import ceil

populacao = 150
n_amostra = 15
k = ceil(populacao / n_amostra)

r = np.random.randint(low = 1, high = k + 1, size = 1)

indice_sps = []
for i in range(n_amostra):
    indice_sps.append(i * k + r[0])
    
print(indice_sps)