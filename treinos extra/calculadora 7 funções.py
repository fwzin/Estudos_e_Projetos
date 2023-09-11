import math

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero!"

def potencia(x, y):
    return x ** y

def raiz_quadrada(x):
    return math.sqrt(x)

def valor_absoluto(x):
    return abs(x)

print("Selecione a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Potência")
print("6. Raiz Quadrada")
print("7. Valor Absoluto")

opcao = input("Digite a opção (1/2/3/4/5/6/7): ")

num1 = float(input("Digite o primeiro número: "))

if opcao != '6' and opcao != '7':
    num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print(num1, "+", num2, "=", adicao(num1, num2))
elif opcao == '2':
    print(num1, "-", num2, "=", subtracao(num1, num2))
elif opcao == '3':
    print(num1, "*", num2, "=", multiplicacao(num1, num2))
elif opcao == '4':
    print(num1, "/", num2, "=", divisao(num1, num2))
elif opcao == '5':
    print(num1, "elevado a", num2, "=", potencia(num1, num2))
elif opcao == '6':
    print("A raiz quadrada de", num1, "é", raiz_quadrada(num1))
elif opcao == '7':
    print("O valor absoluto de", num1, "é", valor_absoluto(num1))
else:
    print("Opção inválida!")
