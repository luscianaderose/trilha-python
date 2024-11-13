# Elabore um programa que peça ao usuário para inserir um número como uma string. 
# Converta essa string para um número inteiro e um número float,
# e exiba a string, os resultados das conversões e seus respectivos tipos.
# Exemplo de saída:
# Digite um número: 10
# Resultado:
# String: 10 str
# Inteiro: 10 int
# Float: 10 float

numero_string = input('Insira um número: ')
inteiro = int(numero_string)
float = float(numero_string)

print(f'''
String: {numero_string} {type(numero_string)}
Inteiro: {inteiro} {type(inteiro)}
Float: {float} {type(float)}
''')