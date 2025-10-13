import random

def gerar_senha():
    return

def iniciar_gerador():
    while True:
        try:
            comprimento = int(input('Digite o comprimento da senha (mínimo 4): '))
            if comprimento < 4:
                print('O comprimento mínimo é 4. Tente novamente')
                continue
        except ValueError:
            print('\nERRO: Por favor, digite apenas um número inteiro para o comprimento.')

if __name__ == '__main__':
    iniciar_gerador()
