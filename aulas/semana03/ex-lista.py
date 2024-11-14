# 1. Perguntar ao usuário o nome de uma pessoa.
# 2. Exibir informações dessa pessoa: sobrenome e idade.
# Ana Soares 20
# Pedro Sento 45
# Maria Figueira 34
# José Santos 80
# Paula Silva 27

nomes = ['Ana', 'Pedro', 'Maria', 'José', 'Paulo', 'Cláudia', 'Mário', 'Laura']
sobrenomes = ['Soares', 'Sento', 'Figueira', 'Santos', 'Silva', 'Motta', 'Bernardes', 'Alves']
idades = [20, 45, 34, 80, 27, 52, 14, 7]

print(nomes)
quem = input('Digite o primeiro nome: ')
while quem not in nomes:
    print('Pessoa não encontrada.')
    quem = input('Digite o primeiro nome: ')
indice = nomes.index(quem)
print(f'Sobrenome: {sobrenomes[indice]}')
print(f'Idade: {idades[indice]}')
