# Medidas de posição

# Definir pasta de trabalho

setwd("C:/Users/Dovahkiin/Documents/machinelearning/dsa/microsoft-powerbi-para-data-science/capitulo-12/")
getwd()
 
# Carregar Dataset
vendas <- read.csv("Vendas.csv", fileEncoding = "windows-1252")

# Resumo do dataset
View(vendas)
str(vendas)
summary(vendas$Valor)
summary(vendas$Custo)

# Média
?mean
mean(vendas$Valor)
mean(vendas$Custo)

# Media Ponderada
?weighted.mean
weighted.mean(vendas$Valor, w = vendas$Custo)

# Moda
# Criando uma função
moda <- function(v) {
  valor_unico <- unique(v)
  valor_unico[which.max(tabulate(match(v, valor_unico)))]
}

#Obtendo a Moda
resultado <- moda(vendas$Valor)
print(resultado)