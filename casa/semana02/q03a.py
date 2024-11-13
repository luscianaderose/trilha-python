# Exercício 03: Diferença entre if Conjuntos e elif
# Você está criando um sistema de notas para uma escola. O programa deve avaliar a nota de um aluno 
# e imprimir a seguinte mensagem:
# 1. Se a nota for acima de 9, o aluno receberá "Aprovado com Mérito".
# 2. Se a nota for maior ou igual a 7, o aluno será "Aprovado".
# 3. Se a nota for menor que 7, o aluno será "Reprovado".

# Sua tarefa é implementar dois programas para realizar essa avaliação de formas diferentes:

# 1. No arquivo q3a.py , crie o programa utilizando apenas if s conjuntos (sem usar elif ). 
# Ou seja, use várias verificações if para cada condição, sem interromper as verificações com elif.

# 2. No arquivo q3b.py, implemente o programa utilizando a estrutura if e elif. Isso significa 
# que você deve usar elif para encadear as verificações de forma que, uma vez que uma condição seja satisfeita, 
# as demais não sejam avaliadas.

# Objetivo: Compare os dois códigos e observe se há diferenças no comportamento. Caso haja, 
# descreva qual é a diferença e explique o motivo.
# Dica: Lembre-se de que, no código com if conjuntos, todas as condições serão verificadas, 
# enquanto no código com elif, a verificação de condições para após a primeira condição verdadeira 
# ser encontrada.

# Exemplo de saída q3a.py :
# Digite a nota do aluno: 10
# Aprovado com Mérito
# Aprovado

# Exemplo de saída q3b.py :
# Digite a nota do aluno: 10
# Aprovado com Mérito

nota = int(input('Digite a nota: '))

if nota > 9:
    print('Aprovado com mérito')

if nota >= 7:
    print('Aprovado')

if nota < 7:
    print('Reprovado')
