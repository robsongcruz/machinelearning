# Poisson
# prob(x=a)
# dpois(x, lambda)

# media de acidentes = lambda = 2 / dia
# prob(x = 3) = ?

lambda = 2
dpois(3, lambda)

# prob(x<a)
# ppois(x, lambda)

# media de acidentes = lambda = 2 / dia
# prob(x <= 3) = ?

ppois(3, lambda)

# media de acidentes = lambda = 2 / dia
# prob(x > 3) = ?

ppois(3, lambda, lower.tail=F)

