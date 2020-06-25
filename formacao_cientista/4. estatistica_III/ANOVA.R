

tratamento = read.csv(file.choose(), se=";", header=T)
fix(tratamento)

boxplot(tratamento$Horas ~ tratamento$Remedio)

# Análise de variância de um fator
an = aov(Horas ~ Remedio, data = tratamento)

summary(an)

# Análise de variância de dois fatores
an1 = aov(Horas ~ Remedio * Sexo, data = tratamento)

summary(an1)

tutkey_test = TukeyHSD(an)
tutkey_test

plot(tutkey_test)
