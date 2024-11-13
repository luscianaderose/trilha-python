# Exercício 01
# Imagine que você está criando um aplicativo para coletar feedback dos usuários. Peça ao usuário para digitar uma frase sobre sua experiência. Após a entrada, faça o seguinte:
# Exiba a entrada original e seu tipo.
# Exiba a quantidade de caracteres da mensagem.
# Converta a frase toda para letras maiúsculas e minúsculas, exibindo os resultados.
# Remova quaisquer espaços em branco no início e no fim da frase.
# Conte quantas vezes a palavra "bom" e "ruim" aparecem na mensagem exiba os resultados.

feedback = input('Qual é seu feedback? ')
print(f'O feedback foi: "{feedback}".\nO tipo é: {type(feedback)}.')
print(f'A quantidade de caracteres é: {len(feedback)}.')
print(f'Feedback em maiúsculo: {feedback.upper()}.')
print(f'Feedback em minúsculo: {feedback.lower()}.')
print(f'Removendo espaços em branco: "{feedback.strip()}".')
print(f'Número de palavras "bom": {feedback.count('bom')}.')
print(f'Número de palavras "ruim": {feedback.count('ruim')}.')