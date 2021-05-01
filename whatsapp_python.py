# Algoritmo para enviar mensagens automáticas via WhatsApp
import pandas as pd

contatos_df = pd.read_excel("enviar.xlsx") #  Acessar planilha do excel
display(contatos_df) # Imprimir para o usuário

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib

navegador = webdriver.Chrome() # Configurar chrome como navegador
navegador.get("https://web.whatsapp.com/") #  Acessar o link

while len(navegador.find_elements_by_id("side")) < 1: #  Esperar o link acessado carregar
    time.sleep(1) # Esperar um segundo

# Laço para enviar as mensagens para cada contato na planilha excel
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Celular"]
    texto = urllib.parse.quote(f"Oi {pessoa}, {mensagem}") #  Codificar texto para ser enviado
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}" #  Link para cada conversa
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(2) #  Espera 2 segundos
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]').send_keys(Keys.ENTER) # Envia a mensagem
    time.sleep(10) #  Espera 10 segundos

navegador.quit() #  Fechar o navegador
print(f'Mensagens enviadas no WhatsApp para {i+1} contatos.') #  Imprime para o usuário
