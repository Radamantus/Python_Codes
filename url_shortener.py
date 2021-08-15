# Importar bibliotecas necessárias
import pyshorteners

url = 'https://www.youtube.com/channel/UC4VNzZ3_7Dl6v9r3jLdYuJw'

shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(url)

# Apresentar ao usuário
print(f'URL encurtada é: {short_url}'.format(short_url))