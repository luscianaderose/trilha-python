# Exercício 02: em construção
# Continuando o exercício anterior, no qual você desenvolveu um sistema para gerenciar tarefas em três listas (pendentes, em andamento e concluídas), agora você
# deve implementar uma nova funcionalidade: mover tarefas entre essas listas. O objetivo é permitir que o usuário altere o status das tarefas conforme o progresso
# delas, movendo-as de uma lista para outra.

# Tarefas:
# 1. Adicionar nova opção ao menu: Incluir uma nova opção para mover uma tarefa de uma lista para outra.
# 2. Comportamento de Mover Tarefa:
# Quando o usuário escolher "Mover Tarefa", o programa deve pedir:
# O nome da lista de origem (pendentes, em andamento ou concluídas) da qual a tarefa será movida.
# O nome da tarefa que será movida.
# A lista de destino (pendente, em andamento ou concluída) para onde a tarefa será movida.
# Após mover a tarefa, o sistema deve exibir as listas atualizadas, mostrando que a tarefa foi removida da lista de origem e adicionada à lista de
# destino.

# Exemplo de Saída:

# Menu de Opções:
# 1. Listar Tarefas Pendentes
# 2. Listar Tarefas em Andamento
# 3. Listar Tarefas Concluídas
# 4. Mover Tarefa
# 5. Sair
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
# Digite a lista com a terefa para mover: pendentes
# Digite o nome da tarefa que deseja mover: Estudar para a prova
# Escolha a lista de destino:
# 1 - Pendentes
# 2 - Em andamento
# 3 - Concluídas

# Escolha uma opção: 2
# Tarefa "Estudar para a prova" movida para "Em andamento".
# Menu de Opções:
# 1. Listar Tarefas Pendentes
# 2. Listar Tarefas em Andamento
# 3. Listar Tarefas Concluídas
# 4. Mover Tarefa
# 5. Sair

# Escolha uma opção: 2
# Tarefas em Andamento:
# 1 - Preparar apresentação
# 2 - Estudar para a prova

# Escolha uma opção: 3
# Tarefas Concluídas:
# Nenhuma tarefa concluída

# Escolha uma opção: 4
# Digite a lista com a tarefa para mover: pendentes
# Digite o nome da tarefa que deseja mover: Estudar para a prova
# Escolha a lista de destino:
# 1 - Pendentes
# 2 - Em andamento
# 3 - Concluídas

# Escolha uma opção: 2
# Tarefa "Estudar para a prova" movida para "Em andamento".
# Menu de Opções:
# 1. Listar Tarefas Pendentes
# 2. Listar Tarefas em Andamento
# 3. Listar Tarefas Concluídas
# 4. Mover Tarefa
# 5. Sair

# Escolha uma opção: 2
# Tarefas em Andamento:
# 1 - Preparar apresentação
# 2 - Estudar para a prova

# Escolha uma opção: 3
# Tarefas Concluídas:
# Nenhuma tarefa concluída


from colorama import Fore, Style


def linha():
    return Fore.BLUE + '-' * 20 + Style.RESET_ALL

def linha2():
    return Fore.BLUE + '*' * 20 + Style.RESET_ALL


pendentes = ['Estudar', 'Mercado']
em_andamento = ['Apresentação']
concluidas = []

# lista = ''
# if lista == 1:
#     lista = 'Pendentes'
# elif lista == 2:
#     lista = 'Em andamento'
# elif lista == 3:
#     lista = 'Concluídas'

while True:
    opcao = input(f'''
{linha()}
{Fore.CYAN}LISTAS DE TAREFAS{Style.RESET_ALL}
Menu de opções:
{Fore.RED}1.{Style.RESET_ALL} Listar Tarefas Pendentes
{Fore.YELLOW}2.{Style.RESET_ALL} Listar Tarefas em Andamento
{Fore.GREEN}3.{Style.RESET_ALL} Listar Tarefas Concluídas
{Fore.LIGHTRED_EX}4.{Style.RESET_ALL} Mover tarefa
{Fore.MAGENTA}5.{Style.RESET_ALL} Sair
{linha()}

Escolha uma opção: ''')

    if opcao == '1': # Listar Tarefas Pendentes
        print(f'{linha2()}{Fore.RED}\nTAREFAS PENDENTES:{Style.RESET_ALL}')
        if pendentes:
            for i, tarefa in enumerate(pendentes, start=1):
                print(f'{i} - {tarefa}')
        else:
            print(f'{Fore.CYAN}Parabéns! Nenhuma tarefa pendente!{Style.RESET_ALL}')

    elif opcao == '2': # Listar Tarefas em Andamento
        print(f'{linha2()}\n{Fore.YELLOW}TAREFAS EM ANDAMENTO:{Style.RESET_ALL}')
        if em_andamento:
            for i, tarefa in enumerate(em_andamento, start=1):
                print(f'{i} - {tarefa}')
        else:
            print(f'{Fore.CYAN}Nenhuma tarefa em andamento.{Style.RESET_ALL}')

    elif opcao == '3': # Listar Tarefas Concluídas
        print(f'{linha2()}\n{Fore.GREEN}TAREFAS CONCLUÍDAS:{Style.RESET_ALL}')
        if concluidas:
            for i, tarefa in enumerate(concluidas, start=1):
                print(f'{i} - {tarefa}')
        else:
            print(f'{Fore.CYAN}Nenhuma tarefa concluída.{Style.RESET_ALL}')

    elif opcao == '4': # MOVER TAREFA
        lista_mover_origem = int(input(f'''{linha2()}\n
Digite o número da lista com a tarefa para mover: 
1 - Pendentes
2 - Em andamento
3 - Concluídas 
'''))
        tarefa_nome = (input(f''' Digite a descrição da tarefa que deseja mover: '''))

        lista_mover_destino = int(input(f'''
Digite o número da lista de destino: 
1 - Pendentes
2 - Em andamento
3 - Concluídas
'''))
        
        # Determinar as listas de origem e destino
        if lista_mover_origem == 1:
            origem = pendentes
        elif lista_mover_origem == 2:
            origem = em_andamento
        elif lista_mover_origem == 3:
            origem = concluidas
        else: 
            print(f'{Fore.RED}Lista de origem inválida!{Style.RESET_ALL}')
            continue

        if lista_mover_destino == 1:
            destino = pendentes
        elif lista_mover_destino == 2:
            destino = em_andamento
        elif lista_mover_destino == 3:
            destino = concluidas
        else:
            print(f'{Fore.RED}Lista de destino inválida!{Style.RESET_ALL}')
            continue

        # Verificar se a tarefa existe na lista de origem
        if tarefa_nome in origem:
            origem.remove(tarefa_nome)
            destino.append(tarefa_nome)
        else:
            print(f'{Fore.RED}Tarefa não encontrada na lista de origem!{Style.RESET_ALL}')

        if destino == pendentes:
            lista = 'Pendentes'
        elif destino == em_andamento:
            lista = 'Em andamento'
        elif destino == concluidas:
            lista = 'Concluídas'
                
        print(f'{Fore.BLUE}Tarefa "{tarefa_nome}" movida para "Lista {lista}".{Style.RESET_ALL}')

    elif opcao == '5': # SAIR
        print(f'{linha()}\n{Fore.CYAN}Até logo! Volte sempre!{Style.RESET_ALL}')
        break

    else:
        print(f'{linha()}\n{Fore.CYAN}Opção inválida! Tente novamente.{Style.RESET_ALL}')

