

#x = rnorm(100) - numeros aleatorios normais
#qqnorm(x)  - gráfico de teste de normalidade
#qqline(x) - gera gráfico de linha de melhor ajuste
#shapiro.test(x) - verificar se dados são normais

x = rnorm(100)
qqnorm(x)
qqline(x)
shapiro.test(x)
