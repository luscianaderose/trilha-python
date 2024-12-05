import time

def busca_linear(lista, alvo):
    contador = 0
    for n in lista:
        if n == alvo:
            break
        contador += 1
    return contador

tempo_inicial = time.time()
lista = range(1,20000001)
alvo = 20000001
busca = busca_linear(lista, alvo)
tempo_final = time.time()
tempo_total = tempo_final - tempo_inicial
print(f'O alvo {alvo} está na posição {busca} executado em {tempo_total}.')
print(tempo_inicial, tempo_final)
print(f'{tempo_total:.20f}')
# Com alvo 3000 deu     0.00097537040710449219
# Com alvo 1000001 deu  0.12222576141357421875
# Com alvo 20000001 deu 1.68889641761779785156