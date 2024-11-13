# Exercício 08: Caixa de supermercado
# Você está criando um sistema para o caixa de um supermercado. O programa deve simular o processo 
# de escaneamento dos itens de um cliente. O funcionamento deve ser o seguinte:
# 1. O programa deve pedir ao usuário que digite o número de um item sempre que ele escanear um produto. 
# Esse número pode ser qualquer valor, representando o código do produto.
# 2. O programa continuará pedindo números até que o usuário digite a palavra "fim". 
# Quando o usuário digitar "fim", o programa deve parar de pedir mais números.
# 3. Quando o cliente terminar de registrar todos os itens e digitar "fim", o programa deve contar 
# quantos itens foram escaneados e exibir essa quantidade.
# O programa deve contar o número de itens escaneados e mostrar o total de produtos registrados.
# Dica: Use um laço while para continuar pedindo números até que o usuário digite "fim".
# Exemplo de saída:
# Digite o número do item: 12345
# Digite o número do item: 67890
# Digite o número do item: 11223
# Digite o número do item: fim
# Total de itens escaneados: 3

n = ''
#contador = 0
contador = -1
while n != 'fim':
    n = input('Digite o número do item: ').lower()
    contador += 1
    #if n == 'fim':    >>>> não precisa
        #break
print(f'Total de itens escaneados: {contador}')

