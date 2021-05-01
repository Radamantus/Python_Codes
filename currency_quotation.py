# Cotação do Dólar Americano e do Euro
import requests  # Importa a biblioteca
request01 = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')  # Busca a informação
request02 = requests.get('https://economia.awesomeapi.com.br/all/EUR-BRL')  # Busca a informação
quotation01 = request01.json()  # Desserialização do retorno da API
quotation02 = request02.json()  # # Desserialização do retorno da API
print('O valor do dólar hoje ' + quotation01['USD']['create_date'], 'é R$:' + quotation01['USD']['bid'])  # Mostra ao usuário o resultado
print('O valor do euro hoje ' + quotation02['EUR']['create_date'], 'é R$:' + quotation02['EUR']['bid'])  # Mostra ao usuário o resultado
