# Endereço a partir do código postal
import requests  # Importa a biblioteca
cep = input('Digite o CEP a ser localizado: ')
request = requests.get('https://cep.awesomeapi.com.br/json/' + cep)  # Busca a informação
address = request.json()  # Desserialização do retorno da API
print('O Endereço é ' + address['address'])  # Mostra ao usuário o resultado
print('O Bairro/Distrito é ' + address['district'])  # Mostra ao usuário o resultado
print('A cidade é ' + address['city'])  # Mostra ao usuário o resultado
print('O estado é ' + address['state'])  # Mostra ao usuário o resultado
