import time

# ALGORÍTMO DE BUSCA LINEAR
# Linear porque vai de um a um.
# Cria uma lista de números de 1 a 10. Imprima a posição do número 5.
# lista = [1,2,3,4,5,6,7,8,9,10]
# print(lista.index(5))

tempo_inicial = time.time()
lista2 = [2,8,3,5,9,6,8]
contador = 0
for n in lista2:
    if n == 5:
        break
    contador += 1
    
tempo_final = time.time()
tempo_total = tempo_final - tempo_inicial
print(f'A posição de 5 é {contador} executado em {tempo_total}.')

