
AirPassengers

#Indices Limites da sequência

start(AirPassengers)

end(AirPassengers)

plot(AirPassengers)

#Anual
plot(aggregate(AirPassengers))
# Mensal
monthplot(AirPassengers)

# Extrair umna janela de dados
subst = window(AirPassengers, start=c(1960, 1), end=c(1960, 12))

plot(subst)

