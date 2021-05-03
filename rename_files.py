# Algoritmo para renomear todos os arquivos (independentemente da extensão) dentro de uma pasta no windows
import os
import re

newname = input('Entre com o nome para qual os arquivos serão renomeados: ')
# folder = 'C:/Users/luism/Documents/MATLAB/'
folder = r'/Users/luism/Documents/MATLAB/'
i = 1

for filename in os.listdir(folder):
    file_name, file_extension = os.path.splitext(filename)
    os.rename(os.path.join(folder, filename), os.path.join(folder, newname + str(i) + file_extension))
    i += 1

print('Todos os arquivos na pasta selecionada forma renomeados com sucesso.')

# Algoritmo para renomear somente arquivos com determinada extensão dentro de uma pasta no windows
import os
import re

newname = input('Entre com o nome para qual os arquivos serão renomeados: ')
extension = input('Entre com a extensão dos arquivos a serem renomeados: ') #  Exemplo: pdf, jpg, exe, png, mp3, mp4, xlsx, xlsm
# folder = 'C:/Users/luism/Documents/MATLAB/'
folder = r'/Users/luism/Documents/MATLAB/'
i = 1

for filename in os.listdir(folder):
    file_name, file_extension = os.path.splitext(filename)
    if re.search(f'\.{extension}$', filename):
        os.rename(os.path.join(folder, filename), os.path.join(folder, newname + str(i) + file_extension))
    else:
        pass
    i = i + 1

print(f'Todos os arquivos com extensão .{extension} na pasta selecionada forma renomeados com sucesso.')
