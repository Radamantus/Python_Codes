# Importar bibliotecas necessárias
import os

# caminho = r'C:\Users\luism\Google Drive\Python Arquivos\Jupyter Exemplos'

# Listar arquivos presentes na pasta Mover
lista_arquivos = os.listdir('Mover')

# laço para mover corretamente os arquivos do tipo XLSX
for arquivo in lista_arquivos:
    if '.xlsx' in arquivo:
        if 'Jan' in arquivo:
            # jogar pra pasta de janeiro
            os.rename(f'Mover/{arquivo}', f'Mover/Jan/{arquivo}')
        if 'Fev' in arquivo:
            # jogar pra pasta de fevereiro
            os.rename(f'Mover/{arquivo}', f'Mover/Fev/{arquivo}')
        if 'Mar' in arquivo:
            # jogar pra pasta de março
            os.rename(f'Mover/{arquivo}', f'Mover/Mar/{arquivo}')