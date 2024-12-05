# Exercício 06: Gerenciamento de Estoque de uma Loja de Alimentos - Atualizar um Produto
# Continuando o exercício anterior, onde você implementou a funcionalidade de remover produtos do estoque, agora o sistema deve permitir que o usuário atualize as
# informações de um produto já existente no estoque.
# Tarefas:
# 1. Atualizar Produto:
# O sistema deve permitir que o usuário atualize as informações de um produto. O usuário deverá escolher um produto pelo seu identificador e fornecer as
# novas informações para o produto:
# Novo nome (opcional, caso o nome precise ser alterado).
# Novo preço (opcional, caso o preço precise ser alterado).
# Nova quantidade (opcional, caso a quantidade precise ser alterada).
# 2. Exibição da Lista de Produtos Após Atualização:
# Após atualizar as informações do produto, o sistema deve exibir a lista atualizada de produtos, com as mudanças feitas.
# Exemplo de Saída:
# Produtos disponíveis:
# 1 - Arroz: R$ 7.49 (10 unidades)
# 2 - Feijão: R$ 9.69 (20 unidades)
# 3 - Ovos: R$ 0.70 (200 unidades)
# 4 - Macarrão: R$ 3.50 (50 unidades)
# 5 - Açúcar: R$ 2.30 (30 unidades)
# Digite o identificador do produto que deseja atualizar: 2
# Digite o novo nome (ou pressione Enter para manter o nome atual): Feijão Preto
# Digite o novo preço (ou pressione Enter para manter o preço atual): 10.99
# Digite a nova quantidade (ou pressione Enter para manter a quantidade atual): 25
# Produto atualizado com sucesso.
# Produtos disponíveis:
# 1 - Arroz: R$ 7.49 (10 unidades)
# 2 - Feijão Preto: R$ 10.99 (25 unidades)
# 3 - Ovos: R$ 0.70 (200 unidades)
# 4 - Macarrão: R$ 3.50 (50 unidades)
# 5 - Açúcar: R$ 2.30 (30 unidades)

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

def exibir_estoque():
    print('\nESTOQUE')
    for indice, (nome, detalhes) in enumerate(produtos.items(), start=1):
        print(f'{indice} - {nome.capitalize()}: R$ {detalhes["preço"]:.2f} ({detalhes["quantidade"]} unidades)')

exibir_estoque()

remover = int(input('\nDigite o identificador do produto que deseja remover: ')) - 1
produto_removido = list(produtos.keys())[remover] # PEGANDO O NOME DO PRODUTO RELATIVO AO IDENTIFICADOR
produtos.pop(produto_removido)
print(f'Produto {produto_removido.capitalize()} removido do estoque.')

exibir_estoque()