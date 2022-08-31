def calc_idade():
    id = False
    while (id == False):
        try:
            nome = str(input("Digite seu nome completo: "))
            ano = int(input("Informe o seu ano de nascimento: "))
            if 1922 <= ano < 2022:
                idade = 2022 - ano
                print(f'Nome: {nome}, {idade} anos.')
                id = True
            else:
                print('Ano inválido!\n')

        except:
            print('Erro! Ano de nascimento inválido!')


calc_idade()
