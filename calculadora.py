# importando as funções
from divisao import divisao
from multiplicar import multiplicar
from resto_da_divisao import resto_divisao
from somar import somar
from subtrair import subtrair
from historico import historico

#função que pede um número e testa para ver se ele é um número mesmo. 
def entrada(mensagem):
    while True:
        try:
            a = float(input(mensagem))
            return a
        except:
            print("Você não digitou um número.")
   
        

#para armazenar o historico das operações
historico_operacao=[]

while True:
    try:  
        operacao =  int(input("\nEscolha a operação que você deseja executar:\n" 
                            "1. Subtração \n"
                            "2. Soma \n" 
                            "3. Divisão \n"
                            "4. Multiplicação \n" 
                            "5. Resto da divisão \n"
                            "6. Histórico da calculadora\n"
                            "0. sair \n"))
        
        #checar se o número está entre 0 e 5 
        if (operacao < 0) or (operacao > 6):
            print ("Essa opção é invalida")

        #finaliza o código 
        elif (operacao == 0):
            print ("Obrigado por usar a calculadora")
            break   

        #mostra o histórico de uso da calculadora e checa se a array está vazio.
        elif (operacao == 6):
            if len(historico_operacao) == 0:
                print("Você ainda não executou nenhuma operação!")
            else:
                print ("O seu histórico é: " + str(historico_operacao)) 
        
        #quando o número digitado foi 1,2,3,4 ou 5 o código irá realizar as seguintes ações:
        else:

            hist = historico(operacao)          #chamar a função para colocar o descritivo da operação 
            historico_operacao.append(hist)     #montar lista com o histórico de operações
        
        #pedir o input dos usuários para a realização das operações com a função de entrada
            n1 = entrada("Digite o primeiro número:") 
            n2 = entrada("Digite o segundo número: ")

        #realizar as operações
            if (operacao == 1):
                subtrair(n1,n2)
            elif (operacao == 2):
                somar(n1,n2)
            elif (operacao == 3):
                divisao(n1,n2)
            elif (operacao == 4):
                multiplicar(n1,n2)
            elif (operacao == 5):
                resto_divisao(n1,n2)
    except:
        print("Digite uma opção válida.")
