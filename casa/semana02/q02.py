# Exercício 02: uso do if aninhado
# Você trabalha em um site de vendas e precisa calcular o desconto de um produto com base no valor da compra. 
# O programa deve funcionar assim:
# Se o valor da compra for maior que R$500, o desconto será de 10%.
# Se o valor for menor ou igual a R$500, mas maior que R$100, o desconto será de 5%.
# Se o valor for menor ou igual a R$100, não haverá desconto.
# Implemente um código que faça esse cálculo e exiba o valor do desconto.

# Exemplo de saída 01:
# Digite o valor da Compra (R$): 80
# O valor do desconto é R$ 0,00

# Exemplo de saída 02:
# Digite o valor da Compra (R$): 500
# O valor do desconto é R$ 25,00

# Exemplo de saída 03:
# Digite o valor da Compra (R$): 600
# O valor do desconto é R$ 60,00

valor = int(input('Digite o valor da Compra (R$): '))
if valor > 500:
    print(f'O valor do desconto é de 10%, R$ {valor * 0.1}, e o valor final é R$ {valor - (valor * 0.1)}.')
elif valor <= 100:
    print('Este valor não recebe desconto.')
elif valor <= 500:
    print(f'O valor do desconto é 5%, R$ {valor * 0.05}, e o valor final é R$ {valor - (valor * 0.05)}.')

