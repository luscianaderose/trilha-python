# Exercício 01: uso de if
# Você está ajudando a gerenciar a entrada de pessoas em um bar noturno. 
# O programa deve perguntar ao usuário sua idade. Se a idade for igual ou maior que 18 anos,
# o programa deve imprimir a mensagem "Entrada liberada". Caso contrário, 
# deve imprimir "Entrada negada".
# Exemplo de saída:
# Digite sua idade: 18
# Entrada liberada

idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Entrada liberada.')
else:
    print('Entrada proibida.')