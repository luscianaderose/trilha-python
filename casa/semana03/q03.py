# Exercício 03: Gerenciamento de Estoque de uma Loja de Alimentos
# Você está desenvolvendo um sistema de gerenciamento para uma loja de alimentos e 
# precisa controlar o estoque de produtos. Cada produto tem um
# identificador , um nome , uma quantidade disponível e um preço. 
# O sistema deve ser capaz de armazenar e exibir essas informações de forma organizada.

# Tarefas:
# 1. Inicie o sistema com pelo menos 5 produtos. 
# Cada produto deve conter as seguintes informações:
# Arroz: preço de R$ 7.49 por unidade, com 10 unidades disponíveis;
# Feijão: preço de R$ 9.69 por unidade, com 20 unidades disponíveis;
# Ovos: preço de R$ 0.70 por unidade, com 200 unidades disponíveis;
# Macarrão: preço de R$ 3.50 por unidade, com 50 unidades disponíveis;
# Açúcar: preço de R$ 2.30 por unidade, com 30 unidades disponíveis.

# 2. O sistema deve permitir as seguintes funcionalidades:
# Exibir a lista de produtos disponíveis, mostrando o nome de cada produto 
# e um identificador numérico (ex: 1, 2, 3, etc.)
# Exemplo de saída:
# Produtos disponíveis:
# 1 - Arroz: R$ 7.49 (10 unidades)
# 2 - Feijão: R$ 9.69 (20 unidades)
# 3 - Ovos: R$ 0.70 (200 unidades)
# 4 - Macarrão: R$ 3.50 (50 unidades)
# 5 - Açúcar: R$ 2.30 (30 unidades)

produtos = {
    1:{
        'nome':'arroz',
        'preço':7.49,
        'estoque':10,
    },
    2:{
        'nome':'feijão',
        'preço':9.69,
        'estoque':20,
    },
    3:{
        'nome':'ovo',
        'preço':0.70,
        'estoque':200,
    },
    4:{
        'nome':'macarrão',
        'preço':3.50,
        'estoque':50,
    },
    5:{
        'nome':'açúcar',
        'preço':2.30,
        'estoque':30
    }
}

for item in produtos.items():
    print(f'{item} - {item.value} R$ x (x unidades)')
