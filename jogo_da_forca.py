import random

forca = ["""
J O G O   D O   F O R C A - Edição Frutas

   +---+
   |   |
       |
       |
       |
       |
=========""", """
J O G O   D O   F O R C A - Edição Frutas

  +---+
  |   |
  O   |
      |
      |
      |
=========""", """
J O G O   D O   F O R C A - Edição Frutas

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""", """
J O G O   D O   F O R C A - Edição Frutas

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""", """
J O G O   D O   F O R C A - Edição Frutas

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""", """
J O G O   D O   F O R C A - Edição Frutas

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """
J O G O   D O   F O R C A - Edição Frutas

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""]

def obterPalavraAleatoria():
    palavras = ['maçã', 'banana', 'manga', 'morango', 'laranja', 'uva', 'abacaxi', 'damasco',
             'limão', 'coco', 'melancia', 'cereja', 'papaia', 'framboesa', 'pêssego', 'lichia', 'melão']

    palavra = random.choice(palavras)
    return palavra

def mostrarTabuleiro(forca, letrasErradas, letrasCorretas, palavraSecreta):
    print(forca[len(letrasErradas)])
    print()

    print('Letras Erradas:', end=' ')
    for letra in letrasErradas:
        print(letra, end=' ')
    print("\n")

    lacunas = '_' * len(palavraSecreta)

    for i in range(len(palavraSecreta)):  # substitui as lacunas pelas letras adivinhadas corretamente
        if palavraSecreta[i] in letrasCorretas:
            lacunas = lacunas[:i] + palavraSecreta[i] + lacunas[i+1:]

    for letra in lacunas:  # mostra a palavra secreta com espaços entre cada letra
        print(letra, end=' ')
    print("\n")

def obterPalpite(jaAdivinhadas):
    while True:
        palpite = input('Adivinhe uma letra: ')
        palpite = palpite.lower()
        if len(palpite) != 1:
            print('Por favor, insira uma única letra.')
        elif palpite in jaAdivinhadas:
            print('Você já adivinhou essa letra. Escolha novamente.')
        elif palpite not in 'abcdefghijklmnopqrstuvwxyz':
            print('Por favor, insira uma LETRA.')
        else:
            return palpite

def jogarNovamente():
    return input("\nVocê quer jogar novamente? ").lower().startswith('s')

letrasErradas = ''
letrasCorretas = ''
palavraSecreta = obterPalavraAleatoria()
jogoConcluido = False

while True:
    mostrarTabuleiro(forca, letrasErradas, letrasCorretas, palavraSecreta)

    palpite = obterPalpite(letrasErradas + letrasCorretas)

    if palpite in palavraSecreta:
        letrasCorretas = letrasCorretas + palpite

        todasLetrasEncontradas = True
        for i in range(len(palavraSecreta)):
            if palavraSecreta[i] not in letrasCorretas:
                todasLetrasEncontradas = False
                break
        if todasLetrasEncontradas:
            print('\nSim! A palavra secreta é "' +
                  palavraSecreta + '"! Você venceu!')
            jogoConcluido = True
    else:
        letrasErradas = letrasErradas + palpite

        if len(letrasErradas) == len(forca) - 1:
            mostrarTabuleiro(forca, letrasErradas,
                         letrasCorretas, palavraSecreta)
            print('Você esgotou todas as tentativas!\nApós ' + str(len(letrasErradas)) + ' tentativas erradas e ' +
                  str(len(letrasCorretas)) + ' tentativas corretas, a palavra era "' + palavraSecreta + '"')
            jogoConcluido = True

    if jogoConcluido:
        if jogarNovamente():
            letrasErradas = ''
            letrasCorretas = ''
            jogoConcluido = False
            palavraSecreta = obterPalavraAleatoria()
        else:
            break
