# Exercício 13: Cálculo de Média
# Crie três variáveis do tipo float para representar as notas de um aluno. 
# Calcule a média dessas notas e exiba o resultado formatado com duas casas decimais.
# Exemplo de saída para as notas 1.53 e 8.62:
# A média do aluno foi: 5.07

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
media = (nota1 + nota2 + nota3) / 3
print(f'A média é {media:.2f}')