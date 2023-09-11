"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('digite um numero: '))
num2 = float(input('digite mais um numero: '))

if num1 > num2:
    print('o numero {} é maior que o numero {}'.format (num1, num2))
if num2 > num1:
    print('o numero {} é maior que o numero {}'.format (num2, num1))
if num2 == num1:
    print('os numeros sao iguais')
else:
    print('numeros não informados ou incorretos')

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num1 = float(input('digite um numero: '))

if num1 >= 0:
    print('o numero {} é positivo'.format(num1))
if num1 < 0:
    print('o numero {} é negativo'.format(num1))
else:
    print('detectamos um erro, tente novamente')

    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

def sexo(resposta):
    if resposta == '2':
        return "Engraçado, mas agora responda corretamente"
    elif resposta == 'M':
        return "Masculino"
    elif resposta == 'F':
        return "Feminino"
    else:
        return "Valor Inválido!"

def main():
    resposta = input("qual é o seu sexo? Digite M-Masculino ou F-Feminino: ").upper()
    mensagem = sexo(resposta)
    print(mensagem)

if __name__ == "__main__":
    main()

    
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('digite uma letra: ')

# Convertemos a letra para minúscula usando o método lower() para facilitar a comparação.
if letra.lower() in ['a', 'e', 'i', 'o', 'u']:
    print('a letra {} é uma vogal'.format(letra))
else:
    print('a letra {} é uma consoante'.format(letra))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

num1 = float(input('digite uma das notas: '))
num2 = float(input('digite a outra nota: '))

media = (num1 + num2)/2

if media >= 7:
    print('o aluno foi aprovado com uma nota de {}'.format (media))
else:
    print('o aluno n foi aprovado com a nota {}'.format(media))

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Faça um Programa que leia três números e mostre o maior deles.

num1 = float(input('digite um numero:'))
num2 = float(input('digite o segundo numero:'))
num3 = float(input('digite o terceio numero:'))

maior = num1 

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

print('o maior numero é o {}'.format(maior))
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float(input('digite o primeiro numero:'))
num2 = float(input('digite o segundo numero:'))
num3 = float(input('digite o terceiro numero:'))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print('o menor numero é o {}'.format(menor))
print('o maior numero é o {}'.format(maior))
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('digite o valor do primeiro produto:'))
p2 = float(input('digite o valor do segundo produto:'))
p3 = float(input('digite o valor do terceiro produto:'))

menor = p1

if p2 < menor:
    menor = p2
if p3 < menor:
    menor = p3

print('o menor valor é {}'.format(menor))
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = float(input('digite um valor: '))
num2 = float(input('digite um valor: '))
num3 = float(input(''))
