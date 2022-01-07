# Definir função com múltiplos argumentos
def sum(*args):
    result = 0
    for i in args:
        result += i
    return result

# Apresentar o resultado da função ao usuário
print(sum(1, 2, 3, 4 , 5))
