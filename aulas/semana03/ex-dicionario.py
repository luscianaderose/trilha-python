pessoas = { 
    'Pedro':{'sobrenome':'Sento','idade':45},
    'Maria':{'sobrenome':'Figueira','idade':34},
    'Ana':{'sobrenome':'Soares','idade':20},
    'José':{'sobrenome':'Santos','idade':76},
    'Paulo':{'sobrenome':'Silva','idade':32},
}

print('Pessoas: ', ', '.join(pessoas.keys()))
nomes = [pessoa.lower() for pessoa in pessoas]
quem = input('Quer mais informações sobre quem? ').lower()
while quem not in nomes:
    print('Nome não encontrado.')
    quem = input('Quer mais informações sobre quem? ').lower()
# for chave, valor in pessoas.items():
#     print('Nome', chave)
#     for chave2, valor2 in valor.items():
#         print(f'{chave2}:{valor2}')
# print(pessoas[quem]['sobrenome'])
quem = quem.capitalize()
print(f'Nome: {quem}')
for chave, valor in pessoas[quem].items():
    print(f'{chave.capitalize()}: {valor}')

