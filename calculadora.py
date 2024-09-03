# importando as funções
from divisao import divisao
from multiplicar import multiplicar
from resto_da_divisao import resto_divisao
from somar import somar
from subtrair import subtrair

def entrada():
    while True:
        try:
            num1 = float(input("\nDigite o primeiro número: "))
            num2 = float(input("\nDigite o segundo número: " ))
            return (num1,num2)
            break
        except:
            print("Você não digitou um número.")
        
executar = True
# criar um looping para calculadora

while True:
    operacao =  input("\nEscolha a operação que você deseja executar:\n" 
                          "1. Subtração \n"
                          "2. Soma \n" 
                          "3. Divisão \n"
                          "4. Multiplicação \n" 
                          "5. Resto da divisão \n"
                          "0. sair \n")

    if (operacao == '0'):
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
        print ("\nDigite uma opção válida")
