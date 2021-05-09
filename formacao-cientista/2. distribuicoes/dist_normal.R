
# media peso = 8 ; dp = 2 / prob=? para peso < 6 = ?

# pnorm(lim_inf, media, desvio_padrao)
prob1 = pnorm(6, 8, 2)
prob1

# media peso = 8 ; dp = 2 / prob=? para peso > 6 = ?

# pnorm(lim_inf, media, desvio_padrao, lower.tail=T)
prob2 = pnorm(6, 8, 2, lower.tail = F)
prob2

#alternativa
prob3 = 1 - pnorm(6, 8, 2)
prob3

# media peso = 8 ; dp = 2 / prob=? para peso < 6 ou peso > 10 ?
prob4 = pnorm(6, 8, 2) + pnorm(10, 8, 2, lower.tail = F)
prob4

# media peso = 8 ; dp = 2 / prob=? para peso > 8 e peso < 10 ?
prob5 = pnorm(10, 8, 2) - pnorm(8, 8, 2)
prob5



