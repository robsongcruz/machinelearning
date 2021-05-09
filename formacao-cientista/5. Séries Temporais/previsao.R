#install.packages('forecast')

library('forecast')

# order: janela
media_movel = ma(AirPassengers, order=3)

# h: número de previsoes (meses)
previsao = forecast(media_movel, h=12)

previsao

plot(previsao)

#ARIMA

arima_set = auto.arima(AirPassengers)

previsao_arima = forecast(arima_set, h=12)

plot(previsao_arima)
