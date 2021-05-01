# Código para automatizar visualizações de um vídeo no YouTube
import time
from selenium import webdriver

video_link = 'https://youtu.be/LDbzjw-PGjw' #  Link do vídeo
views = 3 #  Quantidade de visualizações
video_duration = 8 #  Tempo de duração do vídeo em segundos

driver = webdriver.Chrome() #  Utilizar o navegador chrome
driver.get(video_link) #  Acessar o link no navegador
time.sleep(5) #  Esperar 5 segundos
driver.find_element_by_xpath('//*[@id="movie_player"]/div[4]/button').click() #  Clicar no ícone de play do YouTube

for i in range(views):
    time.sleep(video_duration)
    driver.refresh() #  Atualizar a página do link acessado

driver.quit() #  Fechar o navegador
print(f'Vídeo assistido {views} vezes.') #  Imprimir para o usuário
