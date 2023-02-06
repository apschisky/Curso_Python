"""
Repetições
while (enquanto)
Executa uma ação qualque enquanto for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou')
