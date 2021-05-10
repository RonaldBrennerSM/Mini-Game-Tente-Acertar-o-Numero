def linha(tam=30):
    return '\033[35m-\033[m' * 30


def cabeçalho(txt):
    print(linha())
    print(txt.center(30))
    print(linha())


def menu(lista):
    cabeçalho('GAME: CHUTE UM NÚMERO')
    print('Deseja jogar?'.center(30))
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    resposta = leiaInt('\033[7;40mDigite uma das opções:\033[m ')
    return resposta


def leiaInt(NI):
    try:
        n = int(input(NI))
    except:
        print('\n\033[1;31mERRO: pro favor, digite um número inteiro\033[m\n')
    else:
        return n
    n2 = leiaInt('Digite um número: ')
    return n2