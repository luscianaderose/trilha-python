from typing import Union

def somar(numeros: list[int]) -> Union[int, float]:
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

def subtrair(numeros: list[int]) -> Union[int, float]:
    resultado = 0
    for numero in numeros:
        resultado -= numero
    return resultado

def multiplicar(numeros: list[int]) -> Union[int, float]:
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

def dividir(numeros: list[int]) -> Union[int, float]:
    resultado = numeros[0]
    for numero in numeros[1:]:
        resultado /= numero
    return resultado

def calcular(numeros: list[int], operacao: str) -> Union[int, float]:
    if operacao == 'somar':
        return somar(numeros)
    if operacao == 'subtrair':
        return subtrair(numeros)
    if operacao == 'multiplicar':
        return multiplicar(numeros)
    if operacao == 'dividir':
        return dividir(numeros)

lista = [1, 2, 3, 4, 5]

print('somar(lista): ', somar(lista))
print('subtrair(lista): ', subtrair(lista))
print('multiplicar(lista): ', multiplicar(lista))
print('dividir(lista): ', dividir(lista))
print('calcular(lista, somar): ', calcular(lista, 'somar'))
print('calcular(lista, subtrair): ', calcular(lista, 'subtrair'))
print('calcular(lista, multiplicar): ', calcular(lista, 'multiplicar'))
print('calcular(lista, dividir): ', calcular(lista, 'dividir'))

