# Exercício 04: Gerenciamento de Estoque de uma Loja de Alimentos - Adicionar Novos Produtos

# Continuando o exercício anterior, onde você criou um sistema para gerenciar o estoque 
# de uma loja de alimentos, agora você deve implementar a funcionalidade
# para adicionar novos produtos ao estoque de forma dinâmica. O sistema deve permitir 
# que o usuário insira novos produtos e o adicione à lista de produtos
# disponíveis.

# Tarefas:

# 1. Adicionar Novos Produtos:
# O sistema deve permitir que o usuário adicione novos produtos ao estoque, inserindo 
# as seguintes informações:

## -Nome do Produto
## -Preço por Unidade
## -Quantidade Disponível
# O novo produto deve ser registrado no sistema com um identificador único 
# (numérico e sequencial), e o sistema deve exibir a lista de produtos
# atualizada com o novo item.

# 2. Exibição da Lista de Produtos:
# Após adicionar o novo produto, o sistema deve exibir a lista completa de produtos 
# disponíveis, incluindo o novo item, de forma organizada e com o
# identificador de cada produto.

# Exemplo de Saída:

# Adicione um novo produto:
# Nome: Óleo
# Preço (R$): 4.50
# Quantidade Disponível: 25
# Óleo cadastrado no estoque.

# Produtos disponíveis:
# 1 - Arroz: R$ 7.49 (10 unidades)
# 2 - Feijão: R$ 9.69 (20 unidades)
# 3 - Ovos: R$ 0.70 (200 unidades)
# 4 - Macarrão: R$ 3.50 (50 unidades)
# 5 - Açúcar: R$ 2.30 (30 unidades)
# 6 - Óleo: R$ 4.50 (25 unidades)

produtos = {
    1:{
        'nome':'arroz',
        'preço':7.49,
        'quantidade':10,
    },
    2:{
        'nome':'feijão',
        'preço':9.69,
        'quantidade':20,
    },
    3:{
        'nome':'ovo',
        'preço':0.70,
        'quantidade':200,
    },
    4:{
        'nome':'macarrão',
        'preço':3.50,
        'quantidade':50,
    },
    5:{
        'nome':'açúcar',
        'preço':2.30,
        'quantidade':30
    }
}

# 1 - Arroz: R$ 7.49 (10 unidades)
print('ESTOQUE')
for id, info in produtos.items():
    print(f'{id} - {info["nome"].capitalize()}: R$ {info["preço"]:.2f} ({info["quantidade"]} unidades)')

# Adicione um novo produto:
# Nome: Óleo
# Preço (R$): 4.50
# Quantidade Disponível: 25
# Óleo cadastrado no estoque.

print('\nAdicione um novo produto:')
nome = input('Nome: ').capitalize()
preco = float(input('Preço: R$ '))
quantidade = int(input('Quantidade: '))
novo_id = max(produtos.keys()) + 1
produtos[novo_id] = {'nome':nome, 'preço':preco, 'quantidade':quantidade}
print(f'{nome} cadastrado no estoque.\n')

print('ESTOQUE ATUALIZADO')
for id, info in produtos.items():
    print(f'{id} - {info["nome"].capitalize()}: R$ {info["preço"]:.2f} ({info["quantidade"]} unidades)')

