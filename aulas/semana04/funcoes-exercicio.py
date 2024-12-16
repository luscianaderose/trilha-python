def func(x):
    resultado = 1
    for i in range(1, x + 1):
        print(f'{resultado}*{i}')
        resultado *= i
    return resultado

print(func(5))