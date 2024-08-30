# importando as funções
from divisao import divisao
from multiplicar import multiplicar
from resto_da_divisao import resto_divisao
from somar import somar
from subtrair import subtrair

def entrada():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: " ))
    return (num1,num2)

executar = True
# criar um looping para calculadora

while True:
    operacao =  input("Escolha a operação que você quer fazer: \n 1. subtrair \n 2. somar \n 3. divisão \n 4. multiplicar \n 5. resto da divisão \n 0. sair \n")
    if (operacao == '0'):
 #       executar = False
        print("Você está finalizando a calculadora")
        break
       
    if (operacao == '1'):
        n1, n2 = entrada()
        subtrair(n1,n2)
    elif (operacao == '2'):
        n1, n2 = entrada()
        somar(n1,n2)
    elif (operacao == '3'):
        n1, n2 = entrada()
        divisao(n1,n2)
    elif (operacao == '4'):
        n1, n2 = entrada()
        multiplicar(n1,n2)
    elif (operacao == '5'):
        n1, n2 = entrada()
        resto_divisao(n1,n2)
    else:
        print ("operacao invalida")
