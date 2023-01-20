# ---------------------------------------------------------------
# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.

# num_str = input('Digite um número inteiro: ')
# numero_par_impar = None
# if num_str.isdigit():
#     numero_par_impar = int(num_str) %2
#     if numero_par_impar == 0:
#         print('O número digitado é par')
#     else:
#         print('O número digitado é ímpar')
# else:
#     print('Isso não é um número inteiro')

# ----------------------------------------------------------------

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input('Qual é a hora atual? ')
# hora_atual = 0
# if hora.isdigit():
#     hora_atual = int(hora)

#     if hora_atual >= 0 and hora_atual <= 11:
#         print(f'Bom dia! São {hora_atual} horas!')
#     elif hora_atual >= 12 and hora_atual <= 17:
#         print(f'Boa tarde! São {hora_atual} horas!')
#     elif hora_atual >= 18 and hora_atual <= 23:
#         print(f'Boa noite! São {hora_atual} horas!')
#     else:
#         print('Escolha uma hora de "0" à "23"')
# else:
#     print('Não conheço essa hora')


# SOLUÇÃO DO PROFESSOR

# entrada = input('Digite a hora em números inteiros: ')

# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Bom tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Bom noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas números inteiros')

# -------------------------------------------------------------------------------

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Escreva o seu primeiro nome: ')
letras_nome = len(nome)
if letras_nome <= 4 and letras_nome > 0:
    print(f'Seu nome é curto, só tem {letras_nome} letras!')
elif letras_nome >= 5 and letras_nome <= 6:
    print(f'Seu nome é normal, tem {letras_nome} letras!')
elif letras_nome > 6:
    print(f'Seu nome é muito grande, tem {letras_nome} letras')
else:
    print('Digite pelo menos uma letra')


# SOLUÇÃO DO PROFESSOR

# nome = input('Digite seu nome: ')
# tamanho_nome = len(nome)

# if tamanho_nome > 1:
#     if tamanho_nome <= 4:
#         print('Seu nome é curto')
#     elif tamanho_nome >= 5 and tamanho_nome <= 6:
#         print('Seu nome é normal')
#     else:
#         print('Seu nome é muito grande')
# else:
#     print('Digite mais de uma letra.')