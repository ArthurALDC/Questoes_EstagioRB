#Primeira Questão 
def primeira_questao():
    indice = int(13)
    soma = 0
    k = 0
    while k < indice:
        k = k + 1
        soma = soma + k

    print(f"A soma final será: {soma}")

#Segunda Questão
#Anotações: por questões de memória não pude botar um limite muito alto de números para a sequência, perdão!
def segunda_questao():
    def Fibonacci(limite):
    #Os primeiros termos da sequência
        a,b = 0,1
    #Lista da sequência de números
        Fibonacci = [a,b]


    #O limite será algo como 1000000
        limite = int(1000000)
        while b <= limite:
            a, b = b, a + b
            Fibonacci.append(b)
        return Fibonacci

    #A função que vai verificar o se o número faz parte da sequência
    def verificacao(n, seq):
        if n in seq:
            return f"O número {n} pertence à sequência de Fibonacci."
        else:
            return f"O número {n} não pertence à sequência de Fibonacci."
    #Pede a entrada do número e calcular até um número maior que o informado
    numero_pedido = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    Fibonacci = Fibonacci(numero_pedido)

    #Verifica se vai pertencer na sequência 
    resultado = verificacao(numero_pedido, Fibonacci)
    print(resultado)

def menu():
    print("Selecione a questão:")
    print("1. Primeira Questão")
    print("2. Segunda Questão")
    opcao = input("Digite o número da questão: ")

    if opcao == '1':
        primeira_questao()
    if opcao == '2':
        segunda_questao()

menu()