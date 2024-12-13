import random
from colorama import Fore, Style

palavras = ['cachorro', 'gato', 'cavalo', 'coelho', 'leão', 'tigre', 'girafa', 'elefante', 'jacaré', 
            'lobo', 'urso', 'foca', 'tubarão', 'baleia', 'golfinho', 'zebra', 'macaco', 'rinoceronte', 
            'hipopótamo', 'camelo', 'cadeira', 'mesa', 'sofá', 'televisão', 'telefone', 'computador', 
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

def escolher_palavra():
    return random.choice(palavras)

def linha(simbolo='*', repeticoes=60):
    return simbolo * repeticoes + '\n'

# def imprimir_palpite_feedback(palavra, msg=''):
#     return msg + 'A palavra é: ' + palavra.upper()

def imprimir(msg='', cor=None, reset=Style.RESET_ALL):
    if not cor:
        print(msg)
    else:
        print(cor + msg + reset)

def jogo_da_forca(max_tentativas=5):
    palavra_secreta = escolher_palavra()
    acertos = set()
    imprimir(f'{linha()} # BEM-VINDO AO JOGO DA FORCA! #')
    imprimir(f'\nAdivinhe a palavra: {exibir_palavra(palavra_secreta, acertos)}')
    while max_tentativas > 0:
        imprimir(f'\nVocê tem {max_tentativas} tentativas.')
        palpite = input('Digite uma letra: ').lower()
        if palpite in palavra_secreta:
            acertos.add(palpite)
            imprimir(f'')
        else:
            max_tentativas -= 1
            imprimir(f'\nQue pena! Você errou! A palavra é {exibir_palavra(palavra_secreta, acertos)}.')

        if '_' not in exibir_palavra(palavra_secreta, acertos):
            imprimir(f'Parabéns! Você acertou a palavra: {palavra_secreta.upper()}!\n' + linha())
            break
    else: 
        imprimir(f'Que pena, você perdeu o jogo! A palavra era: {palavra_secreta.upper()}!')

jogo_da_forca()

# colocar uma dica pra cada palavra