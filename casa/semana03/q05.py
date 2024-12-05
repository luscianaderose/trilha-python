# Exercício 05: Gerenciamento de Estoque de uma Loja de Alimentos - Remover um Item

# Continuando o exercício anterior, onde você criou um sistema para gerenciar o estoque de uma loja 
# de alimentos e implementou a funcionalidade de adicionar novos
# produtos, agora o sistema deve permitir que o usuário remova um produto do estoque.

# Tarefas:

# 1. Remover Produto:
# O sistema deve permitir que o usuário remova um produto do estoque. 
# Para isso, será necessário que o usuário forneça o identificador do produto a ser
# removido. O produto será removido da lista de produtos disponíveis.

# 2. Exibição da Lista de Produtos Após Remoção:
# Após remover o produto, o sistema deve exibir a lista atualizada de produtos, 
# de forma organizada e com o identificador de cada produto.

# Exemplo de Saída:
# Produtos disponíveis:
# 1 - Arroz: R$ 7.49 (10 unidades)
# 2 - Feijão: R$ 9.69 (20 unidades)
# 3 - Ovos: R$ 0.70 (200 unidades)
# 4 - Macarrão: R$ 3.50 (50 unidades)
# 5 - Açúcar: R$ 2.30 (30 unidades)

# Digite o identificador do produto que deseja remover: 3
# Produto Ovos removido do estoque.
# Produtos disponíveis:
# 1 - Arroz: R$ 7.49 (10 unidades)
# 2 - Feijão: R$ 9.69 (20 unidades)
# 3 - Macarrão: R$ 3.50 (50 unidades)
# 4 - Açúcar: R$ 2.30 (30 unidades)

produtos = {
    'arroz':{
        'preço':7.49,
        'quantidade':10,
    },
    'feijão':{
        'preço':9.69,
        'quantidade':20,
    },
    'ovo':{
        'preço':0.70,
        'quantidade':200,
    },
    'macarrão':{
        'preço':3.50,
        'quantidade':50,
    },
    'açúcar':{
        'preço':2.30,
        'quantidade':30
    }
}

# exibir_estoque()
# for indice, info in produtos.items():
#     print(f'{indice} - {produtos.keys().capitalize()}: R$ {info["preço"]:.2f} ({info["quantidade"]} unidades)')

# remover = int(input('\nDigite o identificador do produto que deseja remover: '))
# produto_removido = produtos.pop(remover)
# print(f'Produto {produto_removido["nome"].capitalize()} removido do estoque.')
# exibir_estoque()


# print(produtos.keys())

# for indice, nome in enumerate(produtos.keys()):
#     print(f'{indice} - {nome.capitalize()}')

def exibir_estoque():
    print('\nESTOQUE')
    for indice, (nome, detalhes) in enumerate(produtos.items(), start=1):
        print(f'{indice} - {nome.capitalize()}: R$ {detalhes["preço"]:.2f} ({detalhes["quantidade"]} unidades)')

exibir_estoque()

remover = int(input('\nDigite o identificador do produto que deseja remover: ')) - 1
produto_removido = list(produtos.keys())[remover] # PEGANDO O NOME DO PRODUTO RELATIVO AO IDENTIFICADOR
# print('list(produtos.keys())', list(produtos.keys()))
# print('list(produtos.keys()[remover])', list(produtos.keys()[remover]))
produtos.pop(produto_removido)
print(f'Produto {produto_removido.capitalize()} removido do estoque.')

exibir_estoque()

