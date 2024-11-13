# Estruturas de Controle - Desafios
# Desafio 02: Cálculo da Sequência de Fibonacci
# A sequência de Fibonacci é amplamente utilizada em diversos contextos do dia a dia, como no crescimento populacional de animais, no design de padrões estéticos
# e até mesmo na análise de mercados financeiros. Ela é uma sequência de números onde cada número é a soma dos dois números anteriores. A sequência começa
# com 0 e 1, e, a partir daí, cada número seguinte é a soma dos dois anteriores. Matematicamente, ela é definida como:
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2), para n > 1
# Ou seja, a sequência começa assim:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# Por exemplo:
# O 0º número da sequência é 0.
# O 1º número da sequência é 1.
# O 2º número da sequência é 1 (0 + 1).
# O 3º número da sequência é 2 (1 + 1).
# O 4º número da sequência é 3 (1 + 2), e assim por diante.
# Sabendo isso, neste desafio, você foi designado para implementar um programa que calcule os primeiros n números da sequência de Fibonacci. O número n será
# fornecido pelo usuário.
# Exemplo de saída:
# Digite um número: 30
# A sequencia de fibonaci para o número 30 é: 0, 1, 1, 2, 3, 5, 8, 13, 21

# # qtd = int(input('Digite a quantidade de itens da lista: '))
# qtd = 10
# lista = []
# num_atual = 0
# num_anterior = 0
# for item in range(qtd):
#     if num_atual == 0:
#         lista.append(num_atual)
#         num_atual = 1
#     else:
#         lista.append(num_atual)
#         print(num_atual, num_anterior)
#         num_proximo = num_atual + num_anterior
#         print(num_proximo)
#         num_atual = num_proximo
#         num_anterior = num_atual
#         # print(num_anterior, num_atual, num_proximo)
# print(lista)


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