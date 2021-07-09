# Importar bibliotecas necessárias
import random

# Declarar caracteres a serem usados para geras senhas aleatórias
caracteres = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%&*ABCDEFGHIJKLMNOPQRSTUVWXYZ'
tamanho = 8 # Definir tamanho da senha a ser gerada
senha = ''.join(random.sample(caracteres, tamanho)) # Gerar senha

print('A senha aleatória gerada é: {}'.format(senha)) # Apresentar ao usuário
