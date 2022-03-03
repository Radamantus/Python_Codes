# Importar bibliotecas necessárias
import random
import logging

form = "%(asctime)s :: %(levelname)s :: %(filename)s :: %(lineno)d :: %(message)s"
logging.basicConfig(filename = "guess_number.log", level = logging.DEBUG, format = form)

print("Seja muito bem-vindo(a) ao Guess Number do Radamantus!") # Apresenta ao usuário

choice_number = input("Digite o número teto do desafio: ") # Valor máximo a ser adivinhado pelo usuário

if choice_number.isdigit(): # Condicional para verificar se existe só dígitos dentra da string
    choice_number = int(choice_number) # Transformar string para inteiro
else:
    print("Erro: valor informado não é numérico. Favor execute novamente e informe um número!") # Apresenta ao usuário
    logging.critical("O usuário digitou algo não númerico que impediu a execução do programa.")
    logging.error("O usuário não forneceu dígitos.")

random_number = random.randint(0, choice_number) # Gerar um número aleatório entre 0 e o valor máximo definido pelo usuário
logging.info("Programa gerou um número aleatório.")

n_choices = 0 # Inicializar número de tentativas

while True: # Laço continua enquanto o usuário não advinha o número corretamente
    answer_user = input("Advinhe o número: ") # Chute do usuário

    if answer_user.isdigit(): # Laço para verificar se existe só dígitos dentra da string
        answer_user = int(answer_user) # Transformar string para inteiro
    else:
        print("Erro: valor informado não é numérico! Por favor informe um número!") # Apresenta ao usuário
        continue
    
    n_choices = n_choices + 1 # Incrementa número de tentativas em uma unidade
    if answer_user == random_number: # Condicional para verificar se usuário adivinhou ou não o número
        print("Acertou miserável!") # Apresenta ao usuário
        logging.info("Usuário adivinhou corretamente o número.")
        break
    elif answer_user > random_number: # Condicional para dar dica ao usuário
        print("Chutou alto, o número é menor que isso.") # Apresenta ao usuário
    else:
        print("Chutou baixo, o número é maior que isso.") # Apresenta ao usuário

print(f"Número de tentativas: {n_choices}.") # Apresenta ao usuário