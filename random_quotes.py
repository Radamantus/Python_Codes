# Gerador de citações aleatórias
import requests

url = 'https://api.quotable.io/random' #  Link
r = requests.get(url) #  Realizar a requisição
quote = r.json() #  Informações da citação

# print(quote)
# print(len(quote['author']))
# print(quote['content'])
# print('-',quote['author'])
print(quote['author'] + ' once said: ' + quote['content']) # Imprime para o usuário