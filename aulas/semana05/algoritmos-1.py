# FizzBuzz
# Imprima os números de 1 a 100. 
# Para múltiplos de 3, imprima "Fizz", para múltiplos de 5, imprima "Buzz" 
# e para múltiplos de ambos (3 e 5), imprima "FizzBuzz".

# Algorítmo (passo a passo)
# 1. Lista com números de 1 a 101
# 2. Iterar a lista
# 3. Impirmir o número
# 4. Verificar se o resta da divisão do número por 3 dá 0
# 5. Se o resultado for verdadeiro, imprimir a palavra 'Fizz'
# 6. Verificar se o resto da divisão por 5 dá 0
# 7. Se o reusltado for verdadeiro, impirmir 'Buzz'
# 8. Verificar se o resto da divisão por 3 e 5 da 0
# 9. Se for verdadeiro, imprimir 'FizzBuzz'

for n in range(1, 101):
    print(n)
    if n % 3 == 0:
        print('Fizz')
    if n % 5 == 0:
        print('Buzz')
    # if n % 3 == 0 and n % 5 == 0:
    #     print('FizzBuzz')

# FORMATAR SAÍDA