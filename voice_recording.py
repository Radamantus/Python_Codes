# Importar bibliotecas necessárias
import sounddevice
from scipy.io.wavfile import write

# Definir o tempo de gravação
Fs = 44100
Time = int(input('Quantos segundos de gravação? '))

# Apresentar ao usuário
print('\nGravando...\n')

# Capturar a gravação
record_voice = sounddevice.rec(int(Fs*Time), samplerate = Fs, channels = 2)
sounddevice.wait()

# Salvar o arquivo da gravação de voz no computador
write('voice_audio.wav', Fs, record_voice)

# Apresentar ao usuário
print('Gravação Finalizada. Arquivo salvo.')