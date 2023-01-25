frase = input('Escreva uma frase: ')

i = 0
qtd_let = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    letra_apareceu = frase.count(letra_atual)

    if qtd_let < letra_apareceu:
        qtd_let = letra_apareceu
        letra_apareceu_mais = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_apareceu_mais}", apareceu '
    f'{qtd_let}x.'

)

# frase = input('Escreva uma frase: ')

# i = 0
# qtd_apareceu_mais_vezes = 0
# letra_apareceu_mais_vezes = ''

# while i < len(frase):
#     letra_atual = frase[i]

#     if letra_atual == ' ':
#         i += 1
#         continue

#     qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

#     if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
#         qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
#         letra_apareceu_mais_vezes = letra_atual

#     i += 1

# print(
#     'A letra que apareceu mais vezes foi '
#     f'"{letra_apareceu_mais_vezes}" que apareceu '
#     f'{qtd_apareceu_mais_vezes}x'
# )