import random

def gerar_senha(comprimento, usar_letras, usar_numeros, usar_simbolos):
    
    # Definição dos grupos de caracteres 
    letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeros = '0123456789'
    simbolos = '!@#$%^&*()-_+=[]{}|;:,.<>?'

    pool_caracteres = ''
    if usar_letras:
        pool_caracteres += letras
    
    if usar_numeros:
        pool_caracteres += numeros
    
    if usar_simbolos:
        pool_caracteres += simbolos

    if not pool_caracteres:
        return 'Erro: escolha pelo menos um tipo de caractere'

    senha_final= ''
    for _ in range(comprimento):
        caractere_aleatorio = random.choice(pool_caracteres)
        senha_final += caractere_aleatorio

    return senha_final

def iniciar_gerador():
    print('---- GERADOR DE SENHAS ----')

    while True:
        try:
            comprimento = int(input('Digite o comprimento da senha (mínimo 4): '))
            if comprimento < 4:
                print('O comprimento mínimo é 4. Tente novamente')
                continue
            
            print('\nSelecione os tipos de caracteres: ')
            usar_letras = input("Quer incluir letras na senha? (Sim ou não) ").lower() == 'sim' 
            usar_numeros = input("Quer incluir números na senha? (Sim ou não) ").lower() == 'sim' 
            usar_simbolos = input("Quer incluir simbolos na senha? (Sim ou não) ").lower() == 'sim' 

            senha_final = gerar_senha(comprimento, usar_letras, usar_numeros, usar_simbolos)

            print('\nSua senha gerada é:')
            print(f'{senha_final}')

            if not senha_final.startswith('Erro'):
                break
        except ValueError:
            print('\nERRO: Por favor, digite apenas um número inteiro para o comprimento.')

if __name__ == '__main__':
    iniciar_gerador()
