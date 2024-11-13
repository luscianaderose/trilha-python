# Exercício 08: Operadores Booleanos (AND)
# Crie um programa que determine se um aluno foi aprovado com base na realização de atividades. 
# O programa deve incluir uma variável chamada fez_atividade
# que indica se o aluno completou a atividade necessária para a aprovação. 
# A lógica é simples: se o aluno fez a atividade, 
# ele será considerado aprovado; caso contrário, será reprovado. 
# Utilize operadores booleanos para realizar essa verificação e exiba o resultado final.
# Exemplo de saída:
# O aluno fez a atividade: True
# O aluno foi aprovado: True

fez_atividade = input('O aluno fez a atividade? Digite "s" ou "n". ' )
fez_atividade = True if fez_atividade == "s" else False
situacao = 'Aprovado' if fez_atividade == True else 'Reprovado'

print(f'''
O aluno fez a atividade: {fez_atividade}
O aluno foi aprovado: {situacao}
''')