""" Calculadora com while """
valor1 = None
valor2 = None
operador = None
resultado = True
numeros_validos = None
while resultado is True:
    try:
        valor1 = float(input('Digite um número: '))
        valor2 = float(input('Digite outro número: '))
        operador = input('Digite o a operação que deseja "+-*/": ')
        numeros_validos = True
    
    except Exception:
        numeros_validos = None

    if numeros_validos is None:
        print('O número digitado é inválido! Por favor, digite um numero válido.')
        continue

    operadores_permitidos = '+-*/'

    if operador not in operadores_permitidos:
        print('Operador inválido! Digite um operador válido. (+), (-), (*) ou (/)')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '+':
        resultado = valor1 + valor2
        print(f'A soma de {valor1} + {valor2} é igual a {resultado}.')
    elif operador == '-':
        resultado = valor1 - valor2
        print(f'A subtração de {valor1} - {valor2} é igual a {resultado}.')
    elif operador == '*':
        resultado = valor1 * valor2
        print(f'A multiplicação de {valor1} * {valor2} é igual a {resultado}.')
    elif operador == '/':
        resultado = valor1 / valor2
        print(f'A divisão de {valor1} / {valor2} é igual a {resultado}.')


    sair = input('Deseja sair? Para sair tecle "s". Para continuar pressione qualquer trecla: ').lower().startswith('s')
    
    if sair is True:
        break
    else:
        continue
