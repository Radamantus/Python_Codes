print('Calculadora Python') # Apresenta ao usuário

print('Operações Matemáticas Disponíveis') # Apresenta ao usuário

option = ['1-Adição', '2-Subtração', '3-Multiplicação', '4-Divisão'] # Lista de opções

# Laço para imprimir cada operação matemática disponível
for item in option:
    print(item)
    
selection = int(input('Entre com uma das opções (1/2/3/4): ')) # Entrada definada pelo usuário

# Laço se repete até que o usuário forneça uma opção válida
while (selection > 4) or (selection < 1):
    print('Opção inválida! Tente novamente.')
    selection = int(input('Entre com uma das opções (1/2/3/4): '))

n1 = float(input('Entre com o primeiro número: ')) # Primeiro valor fornecido pelo usuário
n2 = float(input('Entre com o segundo número: ')) # Segundo valor fornecido pelo usuário

# Definir função de adição
def somaFunc(n1, n2):
    resultado = n1 + n2
    return print(f'{n1} + {n2} = {resultado}')

# Definir função de subtração
def subFunc(n1, n2):
    resultado = n1 - n2
    return print(f'{n1} - {n2} = {resultado}')

# Definir função de multiplicação
def multFunc(n1, n2):
    resultado = n1 * n2
    return print(f'{n1} * {n2} = {resultado}')

# Definir função de divisão
def divFunc(n1, n2):
    resultado = n1 / n2
    return print(f'{n1} / {n2} = {resultado}')

# Condicional para selecionar a opção fornecida pelo usuário
if (selection == 1):
    print('Operação de adição selecionada.')
    somaFunc(n1, n2)
elif (selection == 2):
    print('Operação de subtração selecionada.')
    subFunc(n1, n2)
elif (selection == 3):
    print('Operação de multiplicação selecionada.')
    multFunc(n1, n2)
elif (selection == 4):
    print('Operação de divisão selecionada.')
    divFunc(n1, n2)

print('Cálculo finalizado.') # Fim da rotina