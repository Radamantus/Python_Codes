# Algoritmo para consultar o histórico de ações na bolsa de valores
import numpy as np
import pandas as pd
from pandas_datareader import data as web
import matplotlib.pyplot as plt

dias = np.linspace(0, 364, 364)

# Histórico de cotação da ação VALE3
df = web.DataReader('BTC-USD', data_source = 'yahoo', start = '04-30-2020', end = '04-30-2021')
# display(df) #  Apresenta tabela para o usuário

fig, ax = plt.subplots(figsize = (10, 5))
ax.plot(dias, df['Adj Close'], label = 'Bitcoin')
ax.set(xlabel = 'Tempo (dias)', ylabel = 'Bitcoin em dólar americano', title = 'Cotação do Bitcoin') #  Configurações do gráfico
# ax.grid()
ax.grid(True, linestyle = '-.')
ax.tick_params(labelcolor = 'r', labelsize = 'large', width = 3)

fig.savefig('stock_price.png')
ax.legend() # Plota a legenda da figura
plt.show() #  Plota a figura para o usuário

data_inicial = "04/30/2020"
data_final = "04/30/2021"

empresas_df = pd.read_excel('empresas.xlsx') # Carrega os dados contidos na tabela excel
# display(empresas_df)

for empresa in empresas_df['Empresas']: #  Laço para todas as ações
    print(f"{empresa}:")
    df = web.DataReader(f'{empresa}.SA', data_source = 'yahoo', start = data_inicial, end = data_final)
    # display(df) #  Apresenta tabela para o usuário
    df['Adj Close'].plot(figsize = (10, 5))
    plt.show() #  Plota a figura para o usuário