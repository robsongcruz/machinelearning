
# amostragem simnples
# set.seed([valor]) pode ser usado para fixar semente e garantir a repetibilidade
amostra = sample(c(0,1), 150, replace=TRUE, prob=c(0.5, 0.5))
summary(amostra)

# amostra
install.packages("sampling")
library(sampling)

# method="srswor" indica sem reposição
amostrairis = strata(iris, c("Species"), size=c(25, 25, 25), method = "srswor")
summary(amostrairis)

amostra_infert = strata(infert, c("education"), size=c(round(12 / 248 * 100), round(120 / 248 * 100), round(116 / 248 * 100)), method="srswor")
summary(amostra_infert)

install.packages("TeachingSampling")
library("TeachingSampling")
pos_amostra = S.SY(150, 10)
amostra_sist_iris = iris[pos_amostra,]
