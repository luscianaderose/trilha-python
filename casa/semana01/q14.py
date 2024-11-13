# Exercício 14: Manipulação de String
# Crie um programa que realize as seguintes operações com uma frase fornecida pelo usuário:
# 1. Peça ao usuário para inserir uma frase.
# 2. Conte quantas palavras a frase contém e exiba o resultado.
# 3. Inverta a ordem dos caracteres da frase e exiba a frase invertida.
# 4. Exiba a frase com a primeira letra de cada palavra em maiúscula.
# 5. Exiba a primeira palavra da frase.
# Exemplo de saída:
# Digite uma frase: Python é uma linguagem poderosa.
# A frase contém 5 palavras.
# Frase invertida: .asoredop gnauqnilag amu e nohtyP
# Frase capitalizada: Python É Uma Linguagem Poderosa.
# Primeira palavra da frase: Python

frase = input('1. Digite uma frase: ')
print(f'2. A frase contém {len(frase.split())} palavras.')
print('3. Frase invertida: ', frase[::-1])
print('4. Frase capitalizada: ', frase.title())
print('5. Primeira palavra da frase: ', frase.split(' ')[0])
