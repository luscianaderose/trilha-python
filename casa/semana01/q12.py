# Exercício 12: Concatenando Strings e Inteiros
# Crie uma variável do tipo string e outra do tipo inteiro. 
# Tente concatená-las diretamente e observe o erro gerado. 
# Depois, converta o inteiro para string e faça a concatenação corretamente. 
# Explique o que ocorreu durante esse processo.

string = '1'
inteiro = 2
#juntos = print(string + inteiro)
# TypeError: can only concatenate str (not "int") to str

juntos = print(string + str(inteiro))

# Na primeira vez não deu certo pq são types diferentes.
# O python juntou 1 e 2 como texto formando '12'.