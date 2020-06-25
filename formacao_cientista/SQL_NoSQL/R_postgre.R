# install.packages("RPostGreSQL")
library("RPostGreSQL")

conexao = dbConnect("PostgreSQL", dbname="CD", host="localhost", 
                     port=5432, user="postgres", password=123456)

sql = "comando sql"

dataset = dbGetQuery(conexao, sql)