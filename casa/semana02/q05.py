# Exercício 05: condições com operadores
# Você está criando um sistema de descontos para clientes. O programa deve calcular o desconto baseado 
# no valor da compra e no status do cliente:
# 1. Se o cliente for VIP e a compra for igual ou acima de R$1000, ele receberá 15% de desconto.
# 2. Se o cliente não for VIP, mas a compra for igual ou acima de R$1000, o desconto será 10%.
# 3. Se a compra for abaixo de R$1000, o desconto será 5% para todos os clientes, independentemente 
# de serem VIP ou não.
# Implemente esse código que calcule o valor do desconto.

# Exemplo de saída 01:
# Informe o valor da compra (em R$): 1000.00
# Informe se o cliente é VIP: não
# O valor do desconto é R$ 100.00

# Exemplo de saída 02:
# Informe o valor da compra (em R$): 1000.00
# Informe se o cliente é VIP: sim
# O valor do desconto é R$ 150.00

# Exemplo de saída 03:
# Informe o valor da compra (em R$): 900.00
# Informe se o cliente é VIP: não
# O valor do desconto é R$ 50.00

valor = int(input('Informe o valor da compra (em R$): '))
vip = input('Informe se o cliente é VIP [s/n]: ').lower()
vip = True if vip == 's' else False

if valor >= 1000 and vip: 
    print(f'O valor do desconto é de 15% = R$ {(valor * 0.15)}')
elif valor >= 1000:
    print(f'O valor do desconto é de 10% = R$ {(valor * 0.1)}')
elif valor < 1000:
    print(f'O valor do desconto é de 5% = R$ {(valor * 0.05)}')
