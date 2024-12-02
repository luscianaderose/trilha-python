# Fatorial de um Número
# Calcule o fatorial de um número informado pelo usuário. 
# (Exemplo: 5! = 5 × 4 × 3 × 2 × 1)

# 1. Coletar um número positivo fornecido pelo usuário.
# 2. Criar uma lista de 1 ao número fornecido.
# 3. Guardar resultado igual a 1.
# 4. Iterar os números.
# 5. Atualizar o resultado com o valor de resultado multiplicado pelo número.
# 6. Imprimir o resultado.

numero = int(input('Digite um número positivo para que eu calcule o fatorial: '))

resultado = 1
for n in range(1, numero + 1):
    # print('resultado:', resultado, 'n:', n)
    resultado *= n

print(f'{numero}! = {resultado}')

