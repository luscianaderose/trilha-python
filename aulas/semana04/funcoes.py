from typing import Union # Union é união de vários tipos

# DECLARAR FUNÇÃO 
print('Função 1')
def nome_funcao(parametro1, parametro2, parametro3):
    print() # Toda função tem um retorno, mesmo que não seja "return". Se não colocar nada, aparece None.
print(nome_funcao(1,2,3)) # aparece None

print('\nFunção 2')
def nome_funcao2(parametro1, parametro2, parametro3):
    return f'{parametro1}, {parametro2}, {parametro3}'
print(nome_funcao2(1,2,3))

print('\nFunção 3 - Anotações de tipos')
def soma(numero1: int, numero2: int) -> int: # É uma boa prática colocar o tipo depois do parâmetro e depois dos parênteses é o tipo do retorno, só pra se lembrar. Não dá erro se não usar esse tipo.
    return numero1 + numero2
print(soma('1', '2')) # Dá 12. Não dá erro, o python não reclama se vc não usar o tipo indicado pq era só uma informação, um lembrete.
print(soma(1, 2)) # Dá 3.

print('\nFunção 4')
def soma2(numero1: int, numero2: int) -> int:
    if type(numero1) != int or type(numero2) != int:
        print('Números com tipos inválidos.')
        return # Sempre que tiver um return, a função não continua mais.
    return numero1 + numero2 # Deu None pq o return ficou vazio.
print(soma2('1', '2')) 

print('\nFunção 5')
def soma3(numero1: Union[int, float], numero2: Union[int, float]) -> Union[int, float]:
    tipo_numero1 = type(numero1)
    tipo_numero2 = type(numero2)
    # if (tipo_numero1 != int or tipo_numero2 != int) and (tipo_numero1 != float or tipo_numero2 != float):
    if (tipo_numero1 != int and tipo_numero1 != float) or (tipo_numero2 != int and tipo_numero2 != float):
        print('Números com tipos inválidos.')
        return
    return numero1 + numero2 
print('1)', soma3('1', '2'))
print('1b)', soma3(1, '2'))
print('2)', soma3(1, 2))
print('3)', soma3(1.1, 2.1))
print('4)', soma3(1, 2.1))

print('\nFunção 6')
def divisao(
        numero1: Union[int, float], 
        numero2: Union[int, float], 
        divisao_inteira: bool
    ) -> Union[int, float]:
    if divisao_inteira:
        return numero1 // numero2
    return numero1 / numero2
print(divisao(10, 3, True))
print(divisao(10, 3, False))
# print(divisao(10, 3)) Deu erro pq faltou um parâmetro.

print('\nFunção 7')
def divisao2(
        numero1: Union[int, float], 
        numero2: Union[int, float], 
        divisao_inteira: bool = True
    ) -> Union[int, float]:
    if divisao_inteira:
        return numero1 // numero2
    return numero1 / numero2
print('a)', divisao2(10, 3, True))
print('b)', divisao2(10, 3, False))
print('c)', divisao2(10, 3)) 