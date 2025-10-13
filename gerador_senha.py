import random

def gerar_senha(comprimento, usar_letras, usar_numeros, usar_simbolos):
    
    # Definição dos grupos de caracteres 
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()-_+=[]{}|;:,.<>?'
    return

def iniciar_gerador():
    print('---- GERADOR DE SENHAS ----')

    while True:
        try:
            comprimento = int(input('Digite o comprimento da senha (mínimo 4): '))
            if comprimento < 4:
                print('O comprimento mínimo é 4. Tente novamente')
                continue
            
            print('\nSelecione os tipos de caracteres: ')
            usar_letras = input("Quer incluir letras na senha? (Sim ou não)").lower() == 'sim' 
            usar_numeros = input("Quer incluir números na senha? (Sim ou não)").lower() == 'sim' 
            usar_simbolos = input("Quer incluir simbolos na senha? (Sim ou não)").lower() == 'sim' 


        except ValueError:
            print('\nERRO: Por favor, digite apenas um número inteiro para o comprimento.')

if __name__ == '__main__':
    iniciar_gerador()
