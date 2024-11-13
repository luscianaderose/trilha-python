# Estruturas de Controle - Desafios

# Desafio 01: Desenvolvimento de um Sistema de Saque para o Caixa Eletrônico

# Você foi designado para desenvolver um sistema de transações para um caixa eletrônico que será utilizado 
# pelos clientes do PicPay. O sistema deverá permitir que os clientes realizem saques de forma prática 
# e eficiente, levando em consideração os seguintes requisitos:

# Requisitos:

# 1. Entrada do Usuário:
# O sistema deve perguntar ao usuário o valor do saque desejado. Esse valor deve ser informado em reais 
# e deve respeitar as seguintes restrições:
# O valor mínimo para saque é de R$ 10,00.
# O valor máximo para saque é de R$ 600,00.

# 2. Notas Disponíveis:
# O caixa eletrônico possui apenas as seguintes notas disponíveis:
# R$ 100,00
# R$ 50,00
# R$ 10,00
# R$ 5,00
# R$ 2,00

# 3. Distribuição das Notas:
# Após o usuário informar o valor do saque, o sistema deve calcular e informar quantas notas de cada valor 
# serão entregues para completar o total solicitado.
# O programa deve ser capaz de dividir o valor total de maneira eficiente, sempre priorizando as notas 
# de maior valor.

# 4. Limitação:
# Não é necessário se preocupar com o número de notas disponíveis na máquina, apenas com a 
# distribuição do valor solicitado.

# Exemplo de saída 01:
# Digite o valor do saque: 5.00
# Operação inválida: o valor mínimo de saque é de R$10.00

# Exemplo de saída 02:
# Digite o valor do saque: 379.00
# Operação bem sucedida.
# Extrato do saque:
# 3 notas de R$ 100.00
# 1 notas de R$ 50.00
# 2 notas de R$ 10.00
# 1 notas de R$ 5.00
# 2 notas de R$ 2.00

# Exemplo de saída 03:
# Digite o valor do saque: 601.00
# Operação bem inválida: o valor máximo do saque é de R$ 600.00

print('CAIXA ELETRÔNICO DO PICPAY')
saque = int(input('Digite o valor do saque (apenas entre R$ 10 e R$ 600): R$ '))

if saque < 10:
    print('\nOperação inválida: o valor mínimo de saque é de R$ 10.00 ')
elif saque > 600:
    print('\nOperação inválida: o valor máximo de saque é de R$ 600.00')
else:
    print('\nOperação válida.')
    notas_100 = saque // 100
    saque -= notas_100 * 100

    notas_50 = saque  // 50
    saque -= notas_50 * 50

    notas_10 = saque // 10
    saque -= notas_10 * 10

    notas_5 = saque // 5
    saque -= notas_5 * 5

    notas_2 = saque // 2
    saque -= notas_2 * 2
    
    notas_1 = saque // 1

    print(f'''\nExtrato do saque:
- {notas_100} notas de 100
- {notas_50} notas de 50
- {notas_10} notas de 10
- {notas_5} notas de 5
- {notas_2} notas de 2
- {notas_1} notas de 1
''')