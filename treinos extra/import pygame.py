import random

# Gerar um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

tentativas = 0
max_tentativas = 10

print("Bem-vindo ao Jogo de Adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while tentativas < max_tentativas:
    try:
        # Solicitar uma tentativa ao jogador
        tentativa = int(input("Tentativa {}: ".format(tentativas + 1)))

        # Verificar se a tentativa está correta
        if tentativa == numero_secreto:
            print("Parabéns! Você adivinhou o número secreto ({}).".format(numero_secreto))
            break
        elif tentativa < numero_secreto:
            print("Tente um número maior.")
        else:
            print("Tente um número menor.")

        tentativas += 1
    except ValueError:
        print("Por favor, insira um número válido.")

if tentativas == max_tentativas:
    print("Você esgotou suas tentativas. O número secreto era {}.".format(numero_secreto))
