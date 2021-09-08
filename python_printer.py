# Importar bibliotecas necessárias
import win32print
import win32api
import os

# Selecionar impressora a ser usada
lista_impressoras = win32print.EnumPrinters(2)

# Listar impressoras
for impressora in lista_impressoras:
    print(impressora)

# Impressora selecionada
impressora = lista_impressoras[4]
win32print.SetDefaultPrinter(impressora[2])

# Imprimir todos os arquivos de uma pasta do computdor
caminho = r'C:\Users\luism\Google Drive\Python Arquivos\Jupyter Exemplos\Imprimir'
lista_arquivos = os.listdir(caminho)
print(lista_arquivos)

# https://docs.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea

# Laço para imprimir cada arquivo encontrado na pasta
for arquivo in lista_arquivos:
    win32api.ShellExecute(0, "print", arquivo, None, caminho, 0)
print('Impressão Concluída')
