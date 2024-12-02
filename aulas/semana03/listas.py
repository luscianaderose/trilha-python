lista = ['a','b','c','d','e']

print('OPERAÇÕES DE LEITURA DE UMA LISTA')
print('1 lista: ', lista)
print('2 primeira posição', lista[0])
print('3 Do primeiro ao terceiro:', lista[0:2])
print('4 Último:', lista[-1])
print('5 Penúltimo:', lista[-2])
print('6 ...:', lista[-3])
print('7 a existe na lista? ', 'a' in lista)
print('8 z existe na lista? ', 'z' in lista)
print('9 Quantos itens tem na lista? ', len(lista))
print('10 Quantos letras "a" exitem na lista? ', lista.count('a'))
print('11 Qual é a posição da letra "d"? ', lista.index('d'))

print('\nOPERAÇÕES DE ESCRITA DE UMA LISTA')
lista[0] = 'teste'
print('12 trocar o 1o elemento: ', lista[0])
lista.append('f')
print('13 adicionando um elementos: ', lista)
# lista.append('g', 'h', 'i') => não pode
# print('9 adicionando muitos elemento: ', lista)
lista.extend(['g', 'h', 'i'])
print('14 adicionando muitos elementos: ', lista)
lista.pop(0)
print('15 deletar o primeiro: ', lista)
lista.pop()
print('16 remover o último: ', lista)
lista.append('teste')
lista.append('teste')
print('17 acrescentou valores iguais', lista)
lista.remove('teste')
print('18 removendo teste da lista', lista) # removeu só uma vez
lista = [1, 2, 3, 4]
print('19 atualizando a lista: ', lista)
print('20 exibir cada elemento: ')
for item in lista:
    print(item)
print('21 exibir cada elemento com operação matemática com lista de números: ')
for item in lista:
    print(item * 3)

lista2 = []
print('22 exibir lista com números multiplicados por 3: ')
for item in lista:
    novo_item = item * 3
    lista2.append(novo_item)
print(lista2)

lista3 = [item for item in lista] # a palavra item antes do for é o que realmente vai aparecer na lista nova
print('23 lista3: ', lista3)

lista4 = [item * 2 for item in lista] # a palavra item antes do for pode ser multiplicada por um número qdo item for número
print('24) lista4: ', lista4)

lista5 = range(0, 100)
print('\n25) lista5 mostra objeto range: ', lista5)
lista6 = [item for item in range(1,101)]
print('\n26) lista6', lista6)
lista7 = [item + 1 for item in range(1,101)]
print('\n27) lista7', lista7)

print('\n28 SEQUÊNCIA DE FIBONACCI')
# Quantidade de itens da sequência de Fibonacci
qtd = 10
lista = []

# Valores iniciais para Fibonacci
num_atual = 0
num_anterior = 0

for item in range(qtd):
    if item == 0:
        lista.append(0)  # Primeiro número da sequência é sempre 0
    elif item == 1:
        lista.append(1)  # Segundo número da sequência é sempre 1
        num_anterior = 0
        num_atual = 1
    else:
        num_proximo = num_atual + num_anterior
        lista.append(num_proximo)
        num_anterior = num_atual
        num_atual = num_proximo

print(f"A sequência de Fibonacci com {qtd} números é: {lista}")

print(f'O 5o número de Fibonacci é: {lista[4]}')
print(f'O número 1 está em qual posição? Na posição {lista.index(1)}.')
print(f'Quantas vezes aparece o número 1? {lista.count(1)} vezes.')
print('str(lista)', str(lista))
print('type(str(lista)):', type(str(lista))) # ficou com [] e com vírgulas
lista = ['1', '2', '3', '4']
print('join com espaço:', ' '.join(lista))
print('join com traço:','-'.join(lista))
print('join com enter:', '\n'.join(lista))

print('Desafio: gerar a mesma lista de Fibonacci mas transformados em string para exibir com join.')