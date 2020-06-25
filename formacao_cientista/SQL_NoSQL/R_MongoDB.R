# install.packages("mongolite")

library("mongolite")

conexao = mongo(collection="tweets", db="twitterdb", url="mongodb://localhost")

dados = conexao$find()

dados