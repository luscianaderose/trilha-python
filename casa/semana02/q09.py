# Exercício 09: Contagem de Vogais em uma Frase
# Crie um programa que leia uma frase e conte quantas vogais (a, e, i, o, u) existem nela. 
# O programa deve percorrer cada caractere da frase e, se o caractere for uma
# vogal, ele deve incrementar um contador.
# Dica: Use um laço for para percorrer os caracteres da frase e contar as vogais.

# Exemplo de saída:
# Digite uma frase: Olá, como vai você?
# Número de vogais: 8

frase = input('Digite uma frase: ')
c = 0
for l in frase:
    #if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
    if l in 'aeiou':
        c += 1

print(f'A frase tem {c} vogais.')