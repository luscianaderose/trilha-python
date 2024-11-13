# Exercício 07: Sequência de Gastos Diários
# Você está criando um programa para ajudar uma pessoa a gerenciar seus gastos diários. 
# O programa deve funcionar da seguinte maneira:
# 1. O programa deve pedir ao usuário para informar a quantidade total de gastos que ele teve no dia.
# 2. Em seguida, o programa deve solicitar o valor de cada um desses gastos, um por vez.
# 3. Ao final, o programa deve calcular e exibir o valor total de todos os gastos daquele dia.
# O programa deve ser capaz de somar todos os valores inseridos e mostrar o total ao usuário.
# Dica: Para pedir ao usuário o valor de cada gasto repetidamente, utilize um laço for para percorrer 
# a quantidade de gastos informada pelo usuário.
# Exemplo de saída:
# Quantos gastos você teve hoje? 3
# Informe o valor do gasto 1: 15.50
# Informe o valor do gasto 2: 30.00
# Informe o valor do gasto 3: 45.75
# O valor total dos gastos de hoje é: R$ 91.25

gastos = int(input('Quantos gastos você teve hoje? '))
gasto = ''
total = 0
for g in range(1, gastos + 1):
    gasto = int(input(f'Informe o valor do gasto {g}: R$ '))
    total += gasto
print(f'O valor total dos gastos de hoje é: R$ {total}.')
