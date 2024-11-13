verdadeiro = True
falso = False

print(type(verdadeiro), type(falso))

print('Operações AND')
# A operação AND é igual a verdadeiro apenas quando todos os itens das operações forem verdadeiras.
print(verdadeiro and falso)
print(verdadeiro and verdadeiro and falso)
print(falso and falso)
print(verdadeiro and verdadeiro)

print('Operações OR')
# A operação OR só é falsa quando todos os ítens são falsos.
print(verdadeiro or falso)
print(falso or verdadeiro or falso)
print(falso or falso)
print(verdadeiro or verdadeiro)

print('Operações NOT')
# A operação NOT inverte o valor do componente.
print(not verdadeiro)
print(not falso)

print('Operador >')
print(2 > 5)

print('Operador <')
print(2 < 5)

print('Operador ==') #se usar só um = é como se criasse uma variavel ou fizesse uma atribuição.
print(2 == 5)
print(2 < 2)
print(2 <= 2) # é como fazer o de baixo
print(2 < 2 or 2 == 2)
print(2 >= 2 )

print('Conversões')
# int -> bool: Qualquer número diferente de zero é True, mesmo positivo ou negativo. Pode variar de linguagem pra linguagem.
print(bool(1))
print(bool(-1))
print(bool(0))
print(bool(0.5))
print(bool(None)) # None é falso!



