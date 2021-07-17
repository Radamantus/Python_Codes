# Importar bibliotecas necessárias
import moviepy.editor

# Carregar arquivo de vídeo
video = moviepy.editor.VideoFileClip('video_file.mp4')

# Apresentar o vídeo ao usuário
# video.ipython_display(maxduration = 3*60)

# Extrair somente o áudio do vídeo
audio = video.audio

# Salvar o áudio extraído do vídeo no computador
audio.write_audiofile('audio_file.mp3')
