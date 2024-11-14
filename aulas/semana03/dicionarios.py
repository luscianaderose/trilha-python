# Dicionário de pessoas
pessoas = { 
    'Pedro':{'sobrenome':'Sento','idade':45},
    'Maria':{'sobrenome':'Figueira','idade':34},
    'Ana':{'sobrenome':'Soares','idade':20},
}

print('OPERAÇÕES DE LEITURA')
print('Dicionário pessoas: ', pessoas)
print(pessoas['Ana']) #não importa em qual posição esteja
print('só a idade da Ana: ', pessoas['Ana']['idade'])
print('Listar as chaves: ', pessoas.keys())
print('Listar os valores: ', pessoas.values())
print('Verificar se Ana está no dicionário: ', 'Ana' in pessoas)
# O padrão é verificar as chaves. Não precisa colocar pessoas.keys().
print('Existe 20 nas informações da Ana? ', 20 in pessoas['Ana'])
print('Existe 20 nas informações da Ana? ', 20 in pessoas['Ana'].values())

print('\nOPERAÇÕES DE ESCRITA')
# dicionario[nova_chave] = novo_valor
pessoas['Mario'] = {'sobrenome':'Figueira','idade':64}
print(pessoas)
print('alterar informação: ')
# dicionario[chave] = novo_valor
pessoas['Mario'] = {'sobrenome':'Figueira','idade':65}
print(pessoas)
pessoas['Mario']['idade'] = 66
print(pessoas)
# del dicionario[chave]
del pessoas['Mario']['idade']
print(pessoas)
del pessoas['Mario']
print(pessoas)
print(pessoas['Pedro'])
# print(pessoas['Mario']) # não existe, então dá erro
# dicionario.get(chave)
print(pessoas.get('Mario')) # retorna None
print(pessoas.get('Mario', 'Não existe.')) # para rertornar msg personalizada
print(pessoas.get('Pedro', 'Não existe.')) 

print('\nImprimindo cada chave com for:')
for chave in pessoas:
    print(chave)

print('\nImprimindo cada valor com for:')
for valor in pessoas.values():
    print(valor)

print('\nImprimindo chaves e valores com for:')
for chave, valor in pessoas.items():
    print(chave, valor)

print('\nOrganizando os itens:\n')
for chave, valor in pessoas.items():
    print('Nome: ', chave, '\nSobrenome:', valor['sobrenome'], '\nIdade:', valor['idade'], '\n')

print('\nOrganizando os itens com outro for:\n')
for chave, valor in pessoas.items():
    print('Nome: ', chave)
    for chave2, valor2 in valor.items():
        print(f'{chave2}: {valor2}')
    print()
