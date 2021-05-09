# -*- coding: utf-8 -*-
import numpy as np
from scipy.stats import chi2_contingency

novela = np.array([[19, 6], [43, 32]])

#H0: Não há diferença significativa além do acaso
print(chi2_contingency(novela))



