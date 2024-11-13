# Exercício 10: Substituição de Palavras em String
# Crie um programa que peça ao usuário para inserir uma frase e, em seguida, 
# solicite que ele informe uma palavra que deseja substituir e a nova
# palavra que deve ser usada no lugar.
# Exemplo de saída:
# Digite uma frase: Programadores são o cérebro e os computadores, o músculo.
# Digite a palavra a ser substituída: músculo
# Digite a nova palavra: motor
# Frase original: Programadores são o cérebro e os computadores, o músculo.
# Frase modificada: Programadores são o cérebro e os computadores, o motor.

frase_original = input('Digite uma frase: ')
palavra1 = input('Qual a palavra que quer alterar? ')
palavra2 = input('Qual a nova palavra que quer colocar no lugar? ')
frase_modificada = frase_original.replace(palavra1, palavra2)
print('A nova frase é: ', frase_modificada)