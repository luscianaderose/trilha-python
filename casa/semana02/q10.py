# Exercício 10: Tabuada
# Crie um programa que mostre a tabuada de um número fornecido pelo usuário. 
# O programa deve exibir o número multiplicado de 1 a 10.
# Dica: Use um laço for para gerar a tabuada de um número.
# Exemplo de saída:
# Digite um número para ver a tabuada: 3
# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12
# 3 x 5 = 15
# 3 x 6 = 18
# 3 x 7 = 21
# 3 x 8 = 24
# 3 x 9 = 27
# 3 x 10 = 30

n = int(input('Digite um número para ver a tabuada: '))
for x in range(1, 11):
    print(f'{n} x {x} = {n * x}')
