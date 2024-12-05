# Dicionário de pessoas
pessoas = { 
    'Pedro':{'sobrenome':'Sento','idade':45},
    'Maria':{'sobrenome':'Figueira','idade':34},
    'Ana':{'sobrenome':'Soares','idade':20},
}

print()
print()

print('A) OPERAÇÕES DE LEITURA')
print()

print('Dicionário pessoas: ', pessoas)
print()

print('A1. pessoas[Ana]:', pessoas['Ana']) #não importa em qual posição esteja
print()

print('A2. só a idade da Ana: ', pessoas['Ana']['idade'])
print()

print('A3. Listar as chaves: pessoas.keys() ->', pessoas.keys())
print()

print('A4. Listar os valores: pessoas.values() ->', pessoas.values())
print()

print('A5. Verificar se Ana está no dicionário: Ana in pessoas -> ', 'Ana' in pessoas)
# O padrão é verificar as chaves. Não precisa colocar pessoas.keys().
print()

print('A6. Existe 20 nas informações da Ana? ', 20 in pessoas['Ana'])
print()

print('A7. Existe 20 nas informações da Ana? ', 20 in pessoas['Ana'].values())
print()
print()


print('B) OPERAÇÕES DE ESCRITA')

# dicionario[nova_chave] = novo_valor
print('B1. Adiconando Mario')
pessoas['Mario'] = {'sobrenome':'Figueira','idade':64}
print(pessoas)
print()

# dicionario[chave] = novo_valor
print('''B2. Alterar informação 
      dicionario[chave] = novo_valor
      Mudei a idade de 64 pra 65: ''')

pessoas['Mario'] = {'sobrenome':'Figueira','idade':65}
print(pessoas)
print()

print('B3. Alterar informação - mudei a idade de 65 pra 66: ')
pessoas['Mario']['idade'] = 66
print(pessoas)
print()

print('B4. Deletar: dicionario[chave]') # del dicionario[chave]
del pessoas['Mario']['idade']
print()
print(pessoas)
print()

print('B. ')
del pessoas['Mario']
print()
print(pessoas)
print()

print('B. ')
print(pessoas['Pedro'])
print()

print('B. ')
# print(pessoas['Mario']) # não existe, então dá erro
# dicionario.get(chave)
print('B. Retorna None')
print(pessoas.get('Mario')) # retorna None
print()

print('B. Para rertornar msg personalizada')
print(pessoas.get('Mario', 'Não existe.')) # para rertornar msg personalizada
print()

print('B. ')
print(pessoas.get('Pedro', 'Não existe.')) 
print()
print()

print('B. Imprimindo cada chave com for:')
for chave in pessoas:
    print(chave)

print()
print('Imprimindo cada valor com for:')
for valor in pessoas.values():
    print(valor)

print()
print('Imprimindo chaves e valores com for:')
for chave, valor in pessoas.items():
    print(chave, valor)

print()
print()

print('Organizando os itens:')
print()

for chave, valor in pessoas.items():
    print('Nome: ', chave, '\nSobrenome:', valor['sobrenome'], '\nIdade:', valor['idade'], '\n')

print()
print()

print('Organizando os itens com outro for:')
print()

for chave, valor in pessoas.items():
    print('Nome: ', chave)
    for chave2, valor2 in valor.items():
        print(f'{chave2}: {valor2}')
    print()

print()