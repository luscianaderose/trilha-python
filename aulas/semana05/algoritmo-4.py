# Soma de Pares
# Dado um vetor de números inteiros, crie um algoritmo que calcule a soma dos números que são pares.
# vetor = lista

# 1. Pedir um número 
# 2. Criar uma lista do número 1 até o número escolhido
# 3. Guardar um resultado com valor inicial igual a 0
# 4. Iterar a lista
# 5. Verificar se cada número é par
# 6. Se for verdadeiro, somar valor do número da vez atulizando o resultado
# 7. Imprimir o resultado

numero = int(input('Digite um número: '))
resultado = 0

for n in range(1, numero + 1):
    # print('Numero: ', n)
    if n % 2 == 0:
        resultado += n
        # print('Soma: ', resultado)

print(f'O resultado da soma dos pares de {numero} é {resultado}.')
