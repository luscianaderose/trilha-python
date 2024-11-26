from typing import Union

def somar(n1: Union[int, float], n2: Union[int, float]) -> Union[int, float]:
    return n1 + n2

def subtrair(n1: Union[int, float], n2: Union[int, float]) -> Union[int, float]:
    return n1 - n2

def multiplicar(n1: Union[int, float], n2: Union[int, float]) -> Union[int, float]:
    return n1 * n2

def dividir(n1: Union[int, float], n2: Union[int, float], divisao_inteira: bool = True) -> Union[int, float]:
    if n2 == 0:
        print('Erro: não é possível dividir um número por 0.')
        return
    if divisao_inteira:
        return n1 // n2
    return n1 / n2

def calcular(n1: Union[int, float], n2: Union[int, float], operacao: str) -> Union[int, float]:
    if operacao not in ['somar', 'subtrair', 'multiplicar', 'dividir']:
        print(f'Erro: operação {operacao} inválida.')
        return
    if operacao == 'somar':
        return somar(n1, n2)
    if operacao == 'subtrair':
        return subtrair(n1, n2)
    if operacao == 'multiplicar':
        return multiplicar(n1, n2)
    if operacao == 'dividir':
        return dividir(n1, n2)
    
print('somar:', calcular(10, 3, 'somar'))
print('subtrair:', calcular(10, 3, 'subtrair'))
print('multiplicar:', calcular(10, 3, 'multiplicar'))
print('dividir:', calcular(10, 3, 'dividir'))
print('modulo:', calcular(10, 3, 'modulo'))
