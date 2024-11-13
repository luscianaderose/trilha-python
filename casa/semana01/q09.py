# Exercício 09: Concatenando Strings
# Crie duas variáveis do tipo string: primeiro_nome e sobrenome. 
# Concatene essas duas strings em uma nova variável chamada nome_completo e
# exiba o resultado final.
# Exemplo de saída:
# Nome completo: João Luiz

primeiro_nome = input('Qual é seu primeio nome? ')
sobrenome = input('Qual é seu sobrenome? ')
nome_completo = primeiro_nome + ' ' + sobrenome
print(f'Nome completo: {nome_completo}.')