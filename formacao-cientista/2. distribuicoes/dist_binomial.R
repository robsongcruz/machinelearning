
# dbinom -> probabilidade individual
num_sucessos = 3
num_experimentos = 5
prob = 0.5

psucessos = dbinom(num_sucessos, num_experimentos, prob)
psucessos

#4 sinais de quatro tempos; p=? / 0, 1, 2, 3, 4 de sinais verdes

vnum_sucessos = c(0, 1, 2, 3, 4)
vnum_experimentos = 4
vprob = 0.25

vpsucessos = dbinom(vnum_sucessos, vnum_experimentos, vprob)
vpsucessos

# pbinom -> probabiidade cumulativa
num_sucessos = 4  # 0-4
num_experimentos = 4
prob = 0.25

cpsucessos = pbinom(cnum_sucessos, cnum_experimentos, cprob)
cpsucessos

# prova 12 questoes
#Chance de acertar 7, com cad aquestão tendo 4 alternativas

num_sucessos = 7
num_experimentos = 12
prob = 0.25

psucessos = dbinom(num_sucessos, num_experimentos, prob)
psucessos

