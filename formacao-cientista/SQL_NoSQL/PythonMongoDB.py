# -*- coding: utf-8 -*-
from pymongo import MongoClient


cliente = MongoClient('mongodb://localhost:27017')

db = cliente.twitterdb

conexao = db.tweets

registros = [item for item in conexao.find()]

#.find_one({atributos})

print(registros)