import random
from time import sleep
from lib.interface import *


while True:
    c = 0
    resposta = menu(['\033[1;32mSIM\033[m', '\033[1;31mNÃO\033[m'])
    n1 = random.randint(1, 100)
    if resposta == 1:
        print('\n\033[1;36mCOMEÇOU!!! Eu escolhi um número entre 0 e 100. Caso queira desistir digite [-1] :)\033[m\n')
        n2 = leiaInt('Digite um número: ')
        print('')
        while True:
            if n2 == -1:
                print(f'\n\033[1;31mFIM DE JOGO!\033[m Você desistiu com \033[1;31m{c}\033[m tentativas\n')
                break
            elif n2 == n1:
                c +=1
                print(f'\n\033[1;31mP\033[1;32mA\033[1;33mR\033[1;34mA\033[1;35mB\033[1;36mÉ\033[1;31mN\033[1;32mS\033[m VOCÊ \033[1;32mACERTOU!\033[m com {c} tentativas\n'
                      f'Eu estava pensando mesmo no número \033[1;31m{n1}\033[m!\n')
                break
            elif n2 > n1:
                print(f'É um número MENOR que {n2}')
            else:
                print(f'É um número MAIOR que {n2}')
            c += 1
            n2 = leiaInt('Digite um número se deseja continuar (-1 para parar): ')
            print('')
    elif resposta == 2:
        print('\nPrograma se encerrando...\n')
        sleep(1)
        cabeçalho('PROGRAMA ENCERRADO')
        break
    else:
        print('\n\033[1;31mERRO: Digite uma opção válida\033[m\n')