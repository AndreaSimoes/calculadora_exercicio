#importação das funções
from somar import somar
from subtrair import subtrair
from multiplicar import multiplicar
from dividir import dividir
from resto import resto
from historico import historico

#para armazenar o historico das operações
historico_operacao=[]

print("Bem vindo a calculadora da Proz")

executar = True

#enquanto não escolher a opçaão 0, continua o processamento
while (executar == True):
  try:
    operacao = int(input(" 1: Somar \n 2: Subtrair \n 3: Multiplicar \n 4: Dividir \n 5: Resto da divisão \n 0: Sair \n Escolha a operação: "))
    if (operacao < 0) or (operacao > 5):
        print ("Essa opção é invalida")
    elif (operacao == 0):
        executar = False                  #vai finalizar o processamento
    else:
        hist = historico(operacao)          #vai chamar a função para colocar o descritivo da operação 
        historico_operacao.append(hist)     #monta lista de operações
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        if (operacao == 1):
            somar(num1,num2)
        elif (operacao == 2):
            subtrair(num1,num2)
        elif (operacao == 3):
            multiplicar(num1,num2)
        elif (operacao == 4):
            dividir(num1,num2)
        else:
            resto(num1,num2)
  except:
      print ("A opção digitada não é numerica")

print ("O seu histórico é: " + str(historico_operacao))
print ("Obrigado por usar a calculadora")
