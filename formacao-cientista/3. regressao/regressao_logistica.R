eleicao = read.csv(file.choose(), sep=";", header = T)

fix(eleicao)

plot(eleicao$DESPESAS, eleicao$SITUACAO)
summary(eleicao)

cor(eleicao$DESPESAS, eleicao$SITUACAO)

modelo = glm('SITUACAO ~ DESPESAS', data=eleicao, family = 'binomial')
summary(modelo)

plot(eleicao$DESPESAS, eleicao$SITUACAO, col='red', pch=20)
points(eleicao$DESPESAS, modelo$fitted, pch=4)


prever_eleicao = read.csv(file.choose(), sep=";", header = T)

prever_eleicao$RESULT = predict(modelo, newdata = prever_eleicao, type="response")

fix(prever_eleicao)
