# MAnipulando chaves e valoresem dicionários

# pessoa = {
#     'nome': 'Anderson',
#     'sobrenome': 'Pschisky',
#     'idade': 38,
#     'altura': 1.75,
#     'endereços': [
#         {'rua': 'tal e tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 555},
#     ],
# 
# }

pessoa = {}

chave = 'nome'


pessoa[chave] = 'Anderson'
pessoa['sobrenome'] = 'Pschisky'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

print(pessoa['sobrenome'])