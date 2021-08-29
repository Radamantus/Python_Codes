# Importar bibliotecas necessárias
import os 

shutdown = input('Deseja desligar o computador? (Sim / Não): ') 

if shutdown == 'Não': 
    exit()  # Não deliga o computador
elif shutdown == 'Sim': 
    os.system("shutdown /s /t 1") # Desliga o computador
else:
    print('Erro! Resposta incorreta. Tente novamente.')