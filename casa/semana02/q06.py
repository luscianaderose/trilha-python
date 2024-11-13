# Exercício 06: Verificando Múltiplas Condições (Uso de and / or )

# Você está criando um programa que verifica se uma pessoa pode ser aprovada para um empréstimo bancário. 
# Para que o empréstimo seja aprovado, a pessoa deve atender a uma das seguintes condições:
# 1. Ter uma renda mínima de R$3000 e um histórico de crédito "bom".
# 2. Caso tenha uma renda inferior a R$3000, ela deve ter um histórico de crédito "excelente".
# Implemente um programa que verifique essas condições e imprima "Empréstimo aprovado" ou "Empréstimo negado".

# Exemplo de saída 01:
# Informe sua renda mínima: 1000.00
# Informe seu histórico de crédito:
# 1 - Excelente
# 2 - Bom
# 3 - Médio
# 4 - Ruim
# 1
# Empréstimo aprovado

# Exemplo de saída 02:
# Informe sua renda mínima: 1000.00
# Informe seu histórico de crédito:
# 1 - Excelente
# 2 - Bom
# 3 - Médio
# 4 - Ruim
# 2
# Empréstimo negado

renda = int(input('Informe sua renda mínima: R$ '))
hc = int(input('''Informe seu histórico de crédito:
Informe seu histórico de crédito:
1 - Excelente
2 - Bom
3 - Médio
4 - Ruim
'''))

if renda >= 3000 and hc <= 2:
    print('Empréstimo aprovado')
elif renda < 3000 and hc == 1:
    print('Empréstimo aprovado')
else:
    print('Empréstimo negado')
