

boxplot(iris$Sepal.Width)

boxplot.stats(iris$Sepal.Width)$out

#install.packages('outliers')

library(outliers)

# default = outliers superiores
outlier(iris$Sepal.Width)

# outliers inferiores
outlier(iris$Sepal.Width, opposite = T)

detector = KNN()
detector.fit(sepal_width)