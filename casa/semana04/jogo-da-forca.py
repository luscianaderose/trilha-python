# criar lista de palavras - ok
# sortear uma palavra - ok
# transformar a palavra em tracinhos - ok
# guardar número de tentativas - ok
# contabilizar as tentaivas erradas - ok
# guardar valores das tentativas certas - ok
# perguntar ao usuario qual é o palpite - ok
# verificar se a tentativa é certa
# revelar onde a letra está na palavra
# reduzir uma tentativa caso esteja errado
# quando acabam as tentaivas ou quando o jogar acerta, dizer se perdeu ou ganhou

import random

palavras = ['cachorro', 'gato', 'cavalo', 'coelho', 'leão', 'tigre', 'girafa', 'elefante', 'jacaré', 
            'lobo', 'urso', 'foca', 'tubarão', 'baleia', 'golfinho', 'zebra', 'macaco', 'rinoceronte', 
            'hipopótamo', 'camelo', 'adeira', 'mesa', 'sofá', 'televisão', 'telefone', 'computador', 
            'relógio', 'abajur', 'caderno', 'caneta', 'lápis', 'mochila', 'armário', 'gaveta', 'tapete', 
            'cobertor','garrafa', 'panela', 'vassoura', 'espelho', 'vermelho', 'azul', 'amarelo', 
            'verde', 'laranja', 'roxo', 'rosa', 'preto', 'branco', 'cinza', 'marrom', 'bege', 'arroz', 
            'feijão', 'pão', 'macarrão', 'pizza', 'bolo', 'torta','salada', 'sopa', 'carne', 'peixe', 
            'frango', 'queijo', 'leite', 'manteiga', 'mel', 'chocolate', 'biscoito','batata', 'cenoura', 
            'morango', 'banana', 'maçã', 'brasil', 'argentina', 'chile', 'peru', 'méxico', 'canadá', 
            'estadosunidos', 'inglaterra', 'frança', 'alemanha', 'itália', 'espanha', 'portugal', 'japão', 
            'china','austrália', 'rússia', 'índia', 'áfrica', 'egito', 'médico', 'professor', 'engenheiro', 
            'advogado', 'arquiteto','bombeiro', 'policial', 'dentista', 'músico', 'escritor', 'jornalista', 
            'ator', 'cozinheiro', 'motorista','agricultor', 'piloto', 'enfermeiro', 'psicólogo', 'veterinário', 
            'pintor', 'carro', 'moto', 'biciclheta']


def exibir_palavra(palavra_secreta, acertos):
    palavra_tracinho = [letra if letra in acertos else '_' for letra in palavra_secreta]
    return ' '.join(palavra_tracinho)

palavra_secreta = random.choice(palavras)
max_tentativas = 5
acertos = set()

print('*' * 30, '\nBem-vindo ao jogo da forca!\n')
print(f'Adivinhe a palavra: {exibir_palavra(palavra_secreta, acertos)}')

while max_tentativas > 0:
    print(f'\nVocê tem {max_tentativas} tentativas.')
    palpite = input('Digite uma letra: ').lower()
    if palpite in palavra_secreta:
        acertos.add(palpite)
        print(f'\nBoa! A palavra agora é {exibir_palavra(palavra_secreta, acertos)}.')
    else:
        max_tentativas -= 1
        print(f'\nQue pena! Você errou! A palavra é {exibir_palavra(palavra_secreta, acertos)}.')

    if '_' not in exibir_palavra(palavra_secreta, acertos):
        print(f'Parabéns! Você acertou a palavra: {palavra_secreta.upper()}!\n' + '*' * 30)
        break
else: 
    print(f'Que pena, você perdeu o jogo! A palavra era: {palavra_secreta.upper()}!')




