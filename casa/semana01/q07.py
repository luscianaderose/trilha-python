# Exercício 07: Variáveis Booleanas
# Crie duas variáveis booleanas: uma chamada maioridade, 
# que indica se o usuário é maior de idade, 
# e outra chamada tem_ingresso, que indica se ele possui ingresso. 
# Exiba as seguintes informações:
# O usuário tem maioridade: True
# O Usuário possui o ingresso: True

maioridade = input('O usuário maior de idade? Digite "s" ou "n". ')
maioridade = True if maioridade == 's' else False
tem_ingresso = input('O usuário tem ingresso? Digite "s" ou "n".  ')
tem_ingresso = True if tem_ingresso == 's' else False

print(f'''
O usuário tem maioridade: {maioridade}
O Usuário possui o ingresso: {tem_ingresso}
''')