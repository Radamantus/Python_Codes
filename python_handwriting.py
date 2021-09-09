# Importar as bibliotecas necessárias
import pywhatkit as Kit

# Escrever mensagens
msg01 = f'Hello there.\nmy name is Jotaro.\n'
msg02 = f'See you later.\nHugs.'

# Escrever mensagens à mão
Kit.text_to_handwriting(msg01 + msg02)
