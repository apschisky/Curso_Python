# Empacotamento e desempacotamento de dicionário
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

# a, b = pessoa
# print(a, b)
# a, b = pessoa.values()
# print(a, b)
# a, b = pessoa.items()
# print(a, b)

# for chave, valor in pessoa.items():
#     print(chave, valor)

# args e kwargs
# args (já vimos)
# kwargs - keywoed arguments (argumentos nomeados)

def mostro_argumentos_momeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_momeados(nome='Joana', qlq=123)
# mostro_argumentos_momeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_momeados(**configuracoes)

print