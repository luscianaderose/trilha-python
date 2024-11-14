# 1. Perguntar ao usuário o nome de uma pessoa.
# 2. Exibir informações dessa pessoa: sobrenome e idade.
# Ana Soares 20
# Pedro Sento 45
# Maria Figueira 34
# José Santos 80
# Paula Silva 27

# nomes = ['Ana', 'Pedro', 'Maria', 'José', 'Paulo', 'Cláudia', 'Mário', 'Laura']
# sobrenomes = ['Soares', 'Sento', 'Figueira', 'Santos', 'Silva', 'Motta', 'Bernardes', 'Alves']
# idades = [20, 45, 34, 80, 27, 52, 14, 7]

pessoas = [
    ['Ana', 'Soares', 20],
    ['Pedro', 'Sento', 45],
    ['Maria', 'Figueira', 34]
]

# nomes = [pessoas[0][0], pessoas[1][0], pessoas[2][0]]
nomes = [pessoa[0] for pessoa in pessoas]
print(nomes)
quem = input('Digite um nome: ')
while quem not in nomes:
    print('Nome não encontrado.')
    quem = input('Digite um nome: ')
indice = nomes.index(quem)
print(f'Sobrenome: {pessoas[indice][1]}')
print(f'Idade: {pessoas[indice][2]}')

