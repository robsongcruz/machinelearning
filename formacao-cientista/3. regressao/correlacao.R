X = c(15,18,20,25,30,44)

Y = c(240,255,270,283,300,310)



correlacao = cov(X, Y) / sqrt(var(X) * var(Y))

correlacao_form = cor(X, Y)
