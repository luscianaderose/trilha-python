import time

def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        elif lista[meio] > alvo:
            direita = meio - 1


tempo_inicial = time.time()
lista = range(1,20000001)
alvo = 20000000
busca = busca_binaria(lista, alvo)
tempo_final = time.time()
tempo_total = tempo_final - tempo_inicial
print(f'''
Alvo: {alvo}
Posição: {busca}
Tempo inicial: {tempo_inicial} 
Tempo final: {tempo_final}
Tempo total: {tempo_total:.20f}''')

## ALGORÍTMO LINEAR
# Com alvo 3000 deu     0.00097537040710449219
# Com alvo 1000001 deu  0.12222576141357421875
# Com alvo 20000001 deu 1.68889641761779785156
## ALGORÍTMO BINÁRIO
# Com alvo 20000000 deu 0.00001025199890136719