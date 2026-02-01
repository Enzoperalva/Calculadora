import time, math

while True:
    print('\033[35mCALCULADORA\033[m')
    print('\033[33m[ 1 ]\033[m SOMA')
    print('\033[33m[ 2 ]\033[m SUBTRAÇÃO')
    print('\033[33m[ 3 ]\033[m MULTIPLICAÇÃO')
    print('\033[33m[ 4 ]\033[m DIVISÃO')
    print('\033[33m[ 5 ]\033[m FATORAÇÃO')
    print('\033[33m[ 6 ]\033[m RAIZ QUADRADA')

    opition= int(input('Opção:'))

    if opition != 1 and opition != 2 and opition != 3 and opition != 4 and opition != 5 and opition != 6:
        print('\033[31mOPÇÃO INVÁLIDA!\033[m')
        print('Ecolha somente 1, 2, 3, 4, 5 ou 6.')
        time.sleep(1)
    elif opition ==1:
        print('')