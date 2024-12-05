import time

def busca_linear(lista, alvo):
    contador = 0
    for n in lista:
        if n == alvo:
            break
        contador += 1
    return contador

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

lista = range(1,20000001)
alvo = 20000000

tempo_inicial = time.time()
busca = busca_binaria(lista, alvo)
tempo_final = time.time()
tempo_total = tempo_final - tempo_inicial
print(f'''
BUSCA BINÁRIA
Alvo: {alvo}
Posição: {busca}
Tempo inicial: {tempo_inicial} 
Tempo final: {tempo_final}
Tempo total: {tempo_total:.20f}''')

tempo_inicial = time.time()
busca = busca_linear(lista, alvo)
tempo_final = time.time()
tempo_total = tempo_final - tempo_inicial
print(f'''
BUSCA LINEAR
Alvo: {alvo}
Posição: {busca}
Tempo inicial: {tempo_inicial} 
Tempo final: {tempo_final}
Tempo total: {tempo_total:.20f}''')

