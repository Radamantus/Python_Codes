# Importando as bibliotecas necessárias
import pyttsx3

# Iniciar a bibliotca
engine = pyttsx3.init()

# Texto a ser falado
engine.say('Corre que o corno tá puto!')
engine.say('Vacina sim! Gostoso demais.')

# Executar ação de falar
engine.runAndWait()