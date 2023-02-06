"""
FAça uma lista de compras com listas

O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""


#----------------------------------------------------------------------------------------

#-------------------------------- MINHA SOLUÇÃO -------------------------------------------


lista_compras = []
inicio = True
inserir = ''
apagar = ''
while inicio == True:
    opcoes_permitidas = 'IiAaLlSs'
    opcao = input('O que você deseja fazer? [I]nserir item, [A]pagar um item, [L]istar todos os itens ou [S]air:  ')
    if opcao in opcoes_permitidas:
        if opcao == 'I' or opcao == 'i':
            inserir = input('Escreva um produto para a lista: ')
            lista_compras.append(inserir)
            continue
        elif opcao == 'A' or opcao == 'a':
            for indice, nome in enumerate(lista_compras, start=1):
                print(indice, nome)
            apagar_str = input('Digite o número do ítem a ser apagado: ')

            try:
                apagar = int(apagar_str)
                apagar -= 1
                apagar == int() and (apagar + 1 > len(lista_compras))
                del lista_compras[apagar]
            except ValueError:
                print('Por favor digite um número inteiro!')
            except IndexError:
                print('Produto inexistente')
            except Exception:
                print('Erro desconhecido')
            
            

        elif opcao == 'L' or opcao == 'l':
            for indice, nome in enumerate(lista_compras, start=1):
                print(indice, nome)


        elif opcao == 'S' or opcao == 's':
            break
    else:
        print('Digite uma opção válida!')

    
#-----------------------------------------------------------------------------------------

#------------------ SOLUÇÃO PROFESSOR ----------------------------------------------

# import os

# lista = []

# while True:
#     print('Selecione uma opção')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')

#     if opcao == 'i':
#         os.system('cls')
#         valor = input('Valor: ')
#         lista.append(valor)
#     elif opcao == 'a':
#         indice_str = input(
#             'Escolha o índice para apagar: '
#         )

#         try:
#             indice = int(indice_str)
#             del lista[indice]
#         except ValueError:
#             print('Por favor digite número int.')
#         except IndexError:
#             print('Índice não existe na lista')
#         except Exception:
#             print('Erro desconhecido')
#     elif opcao == 'l':
#         os.system('cls')

#         if len(lista) == 0:
#             print('Nada para listar')

#         for i, valor in enumerate(lista):
#             print(i, valor)
#     else:
#         print('Por favor, escolha i, a ou l.')