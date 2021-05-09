from scipy.stats import binom

#AO JOGAR UMA MOEDA 5 VEZES, QUAL A PROBABILIDADE DE SAIR CARA?

num_sucessos = 3
num_experim = 5
prob_sucesso = 0.5

prob = binom.pmf(num_sucessos, num_experim, prob_sucesso)
print(f'Probabilidade 1: {prob}')

#4 sinais de quatro tempos; p=? / 0, 1, 2, 3, 4 de sinais verdes

num_sucessos = [0, 1, 2, 3, 4]
num_experim = 4
prob_sucesso = 0.25

prob = binom.pmf(num_sucessos, num_experim, prob_sucesso)
print(f'Probabilidade 2: {prob}')

cprob = binom.cdf(4, 4, 0.25)
print(f'Probabilidade 3: {cprob}')

# prova 12 questoes
#Chance de acertar 7, com cada aquestão tendo 4 alternativas
prob = binom.pmf(7, 12, 0.25)
print(f'Probabilidade 4: {prob}')

probc = binom.pmf(2, 2, 0.5)
print(f'Probabilidade 5: {probc}')

