# Exercício 01: Gerenciamento de Lista de Tarefas
# Você está desenvolvendo um sistema simples de gerenciamento de tarefas, no qual precisa gerenciar 
# três listas diferentes para armazenar as tarefas de acordo com seu status: pendentes, em andamento 
# e concluídas. O sistema deve permitir ao usuário realizar operações para visualizar as tarefas 
# em cada lista e controlar o andamento delas.

# Tarefas:
# 1. Estrutura de Dados:
# Você deve criar três listas para armazenar as tarefas:
# pendentes: lista de tarefas ainda não iniciadas.
# em andamento: lista de tarefas que estão sendo executadas.
# concluídas: lista de tarefas que foram finalizadas.

# 2. Menu de Opções:
# O programa deve exibir um menu interativo com as seguintes opções:
# 1. Listar Tarefas Pendentes: Exibe as tarefas que ainda não foram iniciadas.
# 2. Listar Tarefas em Andamento: Exibe as tarefas que estão em progresso.
# 3. Listar Tarefas Concluídas: Exibe as tarefas que foram finalizadas.
# 4. Sair: Finaliza o programa.

# 3. Comportamento do Sistema:
# Ao escolher uma opção de listar, o sistema deve mostrar as tarefas da lista correspondente.
# Ao escolher a opção "sair", o sistema deve ser encerrado.

# 4. Dados inciais:
# O sistema deve ser configurado com algumas tarefas iniciais já presentes em cada uma das listas 
# (pendentes, em andamento e concluídas).
# Lista de Tarefas Pendentes:
# Estudar para a prova
# Comprar alimentos
# Lista de Tarefas em Andamento:
# Preparar apresentação

# Exemplo de Saída:

# Menu de Opções:
# 1. Listar Tarefas Pendentes
# 2. Listar Tarefas em Andamento
# 3. Listar Tarefas Concluídas
# 4. Sair

# Escolha uma opção: 1
# Tarefas Pendentes:
# 1 - Estudar para a prova
# 2 - Comprar alimentos
# Escolha uma opção: 2
# Tarefas em Andamento:
# 1 - Preparar apresentação
# Escolha uma opção: 3
# Tarefas Concluídas:
# Nenhuma tarefa concluída
# Escolha uma opção: 4

pendentes = ['Estudar para a prova', 'Comprar alimentos']
em_andamento = ['Preparar apresentação']
concluidas = []

opcao = input('''
Lista de Tarefas
Menu de Opções:
1. Listar Tarefas Pendentes
2. Listar Tarefas em Andamento
3. Listar Tarefas Concluídas
4. Sair

Escolha uma opção: 
''')