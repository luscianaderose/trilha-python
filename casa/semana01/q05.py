# Exercício 05: Operações Aritméticas com Variáveis
# Declare duas variáveis numéricas, a e b , atribuindo valores a elas.
# Realize as operações de soma, subtração, multiplicação e divisão (inteira e
# decimal) entre a e b , exibindo cada resultado.
# Exemplo de saída em que a é igual a 5 e b, 3:
# Soma: 8
# Subitração: 2
# Multiplicação: 15
# Divisão Inteiro: 1
# Divisão Decimal: 1,67

a = 10
b = 3

print(f'''
Soma: {a} + {b} = {a + b}
Subtração: {a} - {b} = {a - b}
Multiplicação: {a} x {b} = {a * b}
Divisão Inteiro: {a} / {b} = {(a / b):.2f} 
Divisão Decimal: {a} // {b} = {a // b}
''')