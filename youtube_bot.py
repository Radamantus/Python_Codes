# Código para automatizar visualizações de um vídeo no YouTube
import time
from selenium import webdriver

video_link = 'https://youtu.be/LDbzjw-PGjw'
views = 3
video_duration = 8

driver = webdriver.Chrome()
driver.get(video_link)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="movie_player"]/div[4]/button').click()

for i in range(views):
    time.sleep(video_duration)
    driver.refresh()

driver.quit()
print(f'Vídeo assistido {views} vezes.')
