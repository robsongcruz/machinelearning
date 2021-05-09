import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

base = pd.read_csv('iris.csv')

print(base.shape)
print(base['class'].value_counts())

# np.random.seed([valor]) para fixar semente ou repetibilidade

#amostragem simples
amostra = np.random.choice(a=(0, 1), size=150, replace=True, p=(0.5, 0.5))

#amostragem estratificada

x, _, y, _ = train_test_split(base.iloc[:, 0:4], base.iloc[:, 4], test_size = 0.5, stratify = base.iloc[:, 4])

print(y.value_counts())


base_infert = pd.read_csv('infert.csv')
print(base_infert['education'].value_counts())

x1, _, y1, _ = train_test_split(base_infert.iloc[:, 2:9], base_infert.iloc[:, 1], test_size = 0.595, stratify = base_infert.iloc[:, 1])
print(y1.value_counts())
