# Exercício 04: Vários elif
# Você está desenvolvendo uma aplicação que informa o estado do tempo com base na temperatura em graus Celsius. 
# O programa deve mostrar uma mensagem dependendo da temperatura:
# 1. Se a temperatura for abaixo de 0°C, a mensagem deve ser "Frio extremo".
# 2. Se a temperatura estiver entre 0°C e 10°C, a mensagem será "Frio".
# 3. Se estiver entre 10°C e 20°C, a mensagem será "Ameno".
# 4. Se a temperatura estiver entre 20°C e 30°C, a mensagem será "Quente".
# 5. Se a temperatura for acima de 30°C, a mensagem será "Muito quente".
# Implemente um código que verifique as condições e imprima a mensagem correspondente
# Exemplo de saída:
# Digite a temperatura do dia (em °C): 30
# Muito quente

temp = int(input('Digite a temperatura do dia (em °C): '))

if temp < 0:
    print('Frio extremo')
elif 0 <= temp <= 10:
    print('Frio') 
elif 10 < temp <= 20:
    print('Ameno')
elif 20 < temp <= 30:
    print('Quente')
elif temp > 30:
    print('Calor extremo')