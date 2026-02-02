import time, math

while True:
#Opções para tipo de matemática utilizada!
    print('\033[35mFUNÇÕES\033[m')
    print('\033[33m[ 1 ]\033[m Aritméticas básicas')
    print('\033[33m[ 2 ]\033[m Trigonométricas')
    print('\033[33m[ 3 ]\033[m Logarítmicas/Exponenciais')

    funcao= int(input('Qual função você deseja:'))
    while funcao != 1 and funcao !=  2 and funcao !=  3:
        print('\033[31mDIGITE A OPÇÃO CERTA\033[m')
        time.sleep(1)
        funcao = int(input('Qual função você deseja:'))
    print(' ')
    print('==' * 20)
#ARITMÉICAS BÁSICAS
    if funcao==1:
        print('\033[35mARITMÉTICAS BÁSICAS:\033[m')
        print('\033[33m[ 1 ]\033[m SOMA')
        print('\033[33m[ 2 ]\033[m SUBTRAÇÃO')
        print('\033[33m[ 3 ]\033[m MULTIPLICAÇÃO')
        print('\033[33m[ 4 ]\033[m DIVISÃO')
        print('\033[33m[ 5 ]\033[m FATORAÇÃO')
        print('\033[33m[ 6 ]\033[m RAIZ QUADRADA')

        opition= int(input('Opção:'))
        while opition != 1 and opition != 2 and opition != 3 and opition != 4 and opition != 5 and opition != 6:
            print('\033[31mDIGITE A OPÇÃO CERTA\033[m')
            time.sleep(1)
            opition = int(input('Opção:'))

#Condições para validar as escolhas sobre aritmética basica!
        if opition != 1 and opition != 2 and opition != 3 and opition != 4 and opition != 5 and opition != 6:
            print('\033[31mOPÇÃO INVÁLIDA!\033[m')
            print('Ecolha somente 1, 2, 3, 4, 5 ou 6.')
            time.sleep(1)
        elif opition == 1:
            primeira_parcela= float(input('Primeira parcela:'))
            segunda_parcela= float(input('Segunda parcela:'))
            print(f'{primeira_parcela} + {segunda_parcela} = {primeira_parcela+segunda_parcela:.1f}')
        elif opition == 2:
            minuendo= float(input('Minuendo:'))
            subtraendo= float(input('Subtraendo:'))
            print(f'{minuendo} - {subtraendo} = {minuendo-subtraendo:.1f}')
        elif opition == 3:
            multiplicando= float(input('Multiplicando:'))
            multiplicador= float(input('Multiplicador:'))
            print(f'{multiplicando} x {multiplicador} = {multiplicando*multiplicador:.1f}')
        elif opition == 4:
            dividendo= float(input('Dividendo:'))
            divisor= float(input('Divisor:'))
            print(f'{dividendo} / {divisor} = {dividendo/divisor:.1f}')
        elif opition == 5:
            fator= int(input('Fator:'))
            c=fator
            f=1
            while c>0:
                print(f'{c}', end='')
                print(' x ' if c > 1 else ' = ', end='')
                f*=c
                c-=1
            print(f'{f}')
        elif opition == 6:
            radicando= float(input('Radicando:'))
            print(f'√{radicando} = {math.sqrt(radicando):.1f}')

#Visualizar se o usuário quer continuar!
        continuar= str(input('Deseja continuar [S/N]')).strip().upper()[0]
        if continuar == 'N':
            print('\033[34mObrigado por usar minha calculadora<3\033[m')
            break
        time.sleep(1)
        print(' ')
        print('=='*20)

#TRIGONOMÉTRICAS:
    if funcao == 2:
        print('\033[35mTRIGONOMÉTRICAS:\033[m')
        print('\033[33m[ 1 ]\033[m SENO')
        print('\033[33m[ 2 ]\033[m COSSENO')
        print('\033[33m[ 3 ]\033[m TANGENTE')
        print('\033[33m[ 4 ]\033[m ARCSIN')
        print('\033[33m[ 5 ]\033[m ARCCOS')
        print('\033[33m[ 6 ]\033[m ARCTAN')
        opcao_trigonometria= int(input('Opção:'))
        while opcao_trigonometria != 1 and opcao_trigonometria  != 2 and opcao_trigonometria != 3 and opcao_trigonometria != 4 and opcao_trigonometria != 5 and opcao_trigonometria !=6:
            print('\033[31mDIGITE A OPÇÃO CERTA\033[m')
            time.sleep(1)
            opcao_trigonometria = int(input('Opção:'))
        
#LOGARÍTMICAS/EXPONENCIAIS
    if funcao == 3:
        print('\033[35mLOGARÍTMICAS/EXPONENCIAIS:\033[m')
        print('\033[33m[ 1 ]\033[m LOGARITIMO NATURAL')
        print('\033[33m[ 2 ]\033[m LOGARITIMO BASE')
        print('\033[33m[ 3 ]\033[m EXPONENCIAL')
        print('\033[33m[ 4 ]\033[m POTÊNCIA DE 10')
        opcao_logarimo= int(input('Opção:'))
        while opcao_logarimo != 1 and opcao_logarimo  != 2 and opcao_logarimo != 3 and opcao_logarimo != 4:
            print('\033[31mDIGITE A OPÇÃO CERTA\033[m')
            time.sleep(1)
            opcao_logarimo = int(input('Opção:'))