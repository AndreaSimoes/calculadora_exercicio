# importando as funções
from divisao import divisao
from multiplicar import multiplicar
from resto_da_divisao import resto_divisao
from somar import somar
from subtrair import subtrair

executar = True
# criar um looping para calculadora

while executar == True:
    operacao =  input("Escolha a operação que você quer fazer: \n 1. subtrair \n 2. somar \n 3. divisão \n 4. multiplicar \n 5. resto da divisão \n 0. sair \n")
    executar = False
