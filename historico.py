def historico(operacao):
    if (operacao == 1):
        hist = '1 - somar'
        return hist
    elif (operacao == 2):
        hist = '2 - subtrair'
        return hist
    elif (operacao == 3):
        hist = '3 - multiplicar'
        return hist
    elif (operacao == 4):
        hist = '4 - dividir'
        return hist
    else:
        hist = '5 - resto'
        return hist