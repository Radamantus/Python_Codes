# Algoritmo para exemplificar o uso do comando with

# Sem with
arquivo = open('with_arquivo.txt', 'w')
arquivo.write('Oi, tudo bem?')
arquivo.close()


# Com with
with open('with_arquivo.txt', 'w') as arquivo:
    arquivo.write("Qual o papo de hoje? \n\nO mesmo de sempre.")

with open('with_arquivo.txt', 'r') as arquivo:
    print(arquivo.read())
