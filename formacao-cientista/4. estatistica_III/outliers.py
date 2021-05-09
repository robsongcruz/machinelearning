# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from pyod.models.knn import KNN


iris = pd.read_csv('iris.csv')

plt.boxplot(iris.iloc[:, 1], showfliers=False)  # showfliers: exibir ou não outliers

outliers = iris[(iris['sepal width'] > 4.0) | (iris['sepal width'] < 2.1) ]

sepal_width = pd.DataFrame(iris.iloc[:, 1])

detector = KNN()
detector.fit(sepal_width)
previsoes = detector.labels_
print(previsoes)

sepal_width['prevision'] = previsoes





