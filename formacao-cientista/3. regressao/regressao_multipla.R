

colnames(mtcars)

dim(mtcars)

cor(mtcars[1:4])

modelo = lm(mpg ~ disp, data=mtcars)
modelo

summary(modelo)$r.squared

summary(modelo)$adj.r.squared


plot(mpg ~ disp, data=mtcars)
abline(modelo)

predict(modelo, data.frame(disp=200))

modelo_multiplo = lm(mpg ~ disp + hp + cyl, data=mtcars)

#R2 - coeficiente de determinação
summary(modelo_multiplo)$r.squared

#R2 - coeficiente de determinação ajustado
summary(modelo_multiplo)$adj.r.squared

predict(modelo_multiplo, data.frame(disp=200, hp=100, cyl=4))