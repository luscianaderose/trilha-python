# Exercício 15: Verificação de Substring
# Solicite ao usuário que insira uma frase e, em seguida, uma palavra. 
# Verifique se a palavra está contida na frase e exiba o resultado da verificação.

frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra: ')
resposta = True if palavra in frase else False
print(f'A palavra está contida na frase? {resposta}')