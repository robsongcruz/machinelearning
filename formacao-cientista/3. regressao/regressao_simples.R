dim(cars)

head(cars)

cor(cars)

modelo = lm(speed ~ dist, data=cars) #Linear Model => lm(y, x, data)

modelo

#plot(modelo)

#plot(speed ~ dist, data=cars)

#abline(modelo)


predict(modelo, data.frame(dist=22))

summary(modelo)