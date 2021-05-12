# Algoritmo para traduzir idiomas
from translate import Translator

options = Translator(from_lang = 'pt-br', to_lang = 'english')

phrase01 = 'Curta e compartilhe essa publicação.'
phrase02 = 'Um dia de cada vez meu amigo.'

frase01 = options.translate(phrase01)
frase02 = options.translate(phrase02)

print(frase01)
print(frase02)
