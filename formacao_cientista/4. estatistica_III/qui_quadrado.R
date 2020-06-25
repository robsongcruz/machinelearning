

novela = matrix(c(19, 6, 43, 32), nrow = 2, byrow = T)

rownames(novela) = c("Masculino","Feminino")
colnames(novela) = c("Assiste","Não Assiste")

fix(novela)


#H0: Não há diferença significativa além do acaso
chisq.test(novela)

# X-squared = 2.0374, df = 1, p-value = 0.1535
# Se p-value escolhido for de 0.05, a hipótese nula não é rejeitada



jogo = matrix(c(41,34, 18, 7), nrow = 2, byrow = T)

rownames(jogo) = c("Masculino","Feminino")
colnames(jogo) = c("Joga","Não Joga")
chisq.test(jogo)

