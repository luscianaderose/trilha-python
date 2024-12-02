# Verificar Palíndromo
# Verifique se uma palavra ou frase é um palíndromo 
# (que pode ser lido da mesma forma de trás para frente). 
# Ignore espaços e diferenças de maiúsculas/minúsculas.
# Socorram-me, subi no ônibus em Marrocos
# Socorramme subi no onibus em Marrocos

# 1. Coletar palavra ou frase
# 2. Juntar tudo tirando os espaços
# 3. Colocar tudo em minúsculo
# 4. Guardar palavra ao contrário
# 5. Comparar a palavra original com a a palavra ao contrário
# 6. Se for verdadeiro, imprimo 'palíndromo'.
# 7. Se não for, imprimir 'Não é um palíndromo'.

original = input('Digite uma palavra ou frase: ')
original_formatado = original.lower().replace(' ', '')
inverso = original_formatado[::-1]

# print(original_formatado)
# print(inverso)

if original_formatado == inverso:
    print(f'O texto {original} é um palíndromo!')
else:
    print(f'O texto {original} não é um palíndromo!')


