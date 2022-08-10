from codecs import BufferedIncrementalEncoder


def votacao(candidato):  # fução para votação com a variavel candidato como argumento
    global candidato_X, candidato_Y, candidato_Z, branco
 
    if candidato.isalpha():  # checa se candidato contem apenas letras
        if candidato == 'Sair' or candidato == 'sair' or candidato == 'SAIR':
            print('\nFIM DA VOTAÇÃO!')
            print_resultados()

    elif candidato.isnumeric():  # checa se candidato e um caracter numerico
        if candidato == '889' or candidato == '847' or candidato == '515' or candidato == '0':
            if candidato == '889':
                candidato_Y += 1
            elif candidato == '847':
                candidato_X += 1
            elif candidato == '515':
                candidato_Z += 1
            elif candidato == '0':
                branco += 1
        else:  # se o valor digitado nao e valido, há entrada de novo candidato e a funcao repete
            candidato= str(input('Digite um numero válido para o candidato: '))
            votacao(candidato)


def print_resultados():  # printa resultados e encerra programa
    global candidato_X, candidato_Y, candidato_Z, branco

    print('\nQUANTIDADE DE VOTOS:\n')
    print('CANDIDATO Y - Quantidade de votos: ' + str(candidato_Y))
    print('CANDIDATO X - Quantidade de votos: ' + str(candidato_X))
    print('CANDIDATO Z - Quantidade de votos: ' + str(candidato_Z))
    print('VOTOS NULOS - Quantidade de votos: ' + str(branco))

    exit()  # encerra prog


#main 
candidato_X = 0
candidato_Y = 0
candidato_Z = 0
branco = 0

while True:  # laço ocorre indefinidamente ate "sair"
    candidato = str(input('ELEIÇÃO ESPECIAL\nDigite o número do seu candidato ou digite "sair" para sair da votação: '))
    votacao(candidato)