frase = 'O Python é uma linguagem de programação multiparadigma.' \
    'Python foi criado por Guido van Rossum.'

i = 0
qtd_let = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    letra_apareceu = frase.count(letra_atual)

    if qtd_let < letra_apareceu:
        qtd_let = letra_apareceu
        letra_apareceu_mais = letra_atual

i += 1

print('A letra que apareceu mais vezes')