# Importar biblioteca
from pytube import YouTube

# Cria objeto com URL do vídeo a ser baixado
video = YouTube('https://www.youtube.com/watch?v=gF2qYW1hIVk')

# Configura a melhor qualidade de vídeo
stream = video.streams.get_highest_resolution()

# Faz o download do vídeo selecionado e o salva na pasta especificada do computador
folder = r'/Users/luism/Documents/MATLAB/'
stream.download(output_path = folder)
