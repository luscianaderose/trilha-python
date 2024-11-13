# Exercício 11: Comparação de Tipos
# Crie uma variável do tipo string e outra do tipo inteiro, ambas representando o mesmo número. 
# Compare as variáveis usando == e != , exiba os resultados 
# e explique o comportamento observado na comparação.

variavel_string = input('Digite um número: ')
variavel_inteiro = int(variavel_string)
print('variavel_string: ', variavel_string)
print('variavel_inteiro: ', variavel_inteiro)
print('variável string é igual à variável inteiro? ', variavel_string == variavel_inteiro)
print('variável string é diferente da variável inteiro? ', variavel_string != variavel_inteiro)

# As variáveis são diferentes porque são types diferentes.