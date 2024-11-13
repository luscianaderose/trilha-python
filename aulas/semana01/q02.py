nome = input('Nome completo: ')
idade = int(input('Idade: '))
novidade = input('Gostaria de receber novidades e promoções por e-mail? Responda "sim" ou "não". ').lower()
novidade = True if novidade == 'sim' else False
agendamento = input('Deseja algum serviço extra? Digite\n1-Corte\n2-Coloração\n3-Penteado\n')
print(f'Nome: {nome.title()} / Tipo: {type(nome)}')
print(f'Idade: {idade} / Tipo: {type(idade)}')
print(f'O usuário {nome.split(' ')[0]} deseja receber novidades por email: {novidade}.')
