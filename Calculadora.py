import time, math

while True:
#Opções para tipo de matemática utilizada!

    print('\033[35mFUNÇÕES\033[m')
    print('\033[33m[ 1 ]\033[m Aritméticas básicas')
    print('\033[33m[ 2 ]\033[m Trigonométricas')
    print('\033[33m[ 3 ]\033[m Logarítmicas/Exponenciais')

    funcao= int(input('Qual função você deseja:'))
    print('=='*20)
    while funcao != 1 and funcao !=  2 and funcao !=  3:
        print('\033[31mDIGITE A OPÇÃO CERTA\033[m')
        time.sleep(1)
        funcao = int(input('Qual função você deseja:'))

#ARITMÉICAS BÁSICAS
    while True:
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
    #SOMA
            elif opition == 1:
                primeira_parcela= float(input('Primeira parcela:'))
                segunda_parcela= float(input('Segunda parcela:'))
                print(f'{primeira_parcela} + {segunda_parcela} = {primeira_parcela+segunda_parcela:.1f}')
    #SUBTRAÇÃO
            elif opition == 2:
                minuendo= float(input('Minuendo:'))
                subtraendo= float(input('Subtraendo:'))
                print(f'{minuendo} - {subtraendo} = {minuendo-subtraendo:.1f}')

    #MULTIPLICAÇÃO
            elif opition == 3:
                multiplicando= float(input('Multiplicando:'))
                multiplicador= float(input('Multiplicador:'))
                print(f'{multiplicando} x {multiplicador} = {multiplicando*multiplicador:.1f}')

    #DIVISÃO
            elif opition == 4:
                dividendo= float(input('Dividendo:'))
                divisor= float(input('Divisor:'))
                print(f'{dividendo} / {divisor} = {dividendo/divisor:.1f}')

    #FATORIAL
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

    #RAIZ_QUADRADA
            elif opition == 6:
                radicando= float(input('Radicando:'))
                print(f'√{radicando} = {math.sqrt(radicando):.1f}')

#Visualizar se o usuário quer continuar!
            continuar= str(input('Deseja continuar na função ARITMÉTICAS BÁSICAS [S/N]:')).strip().upper()[0]
            if continuar == 'N':
                print('\033[34mVOLTANDO..\033[m')
                time.sleep(0.6)
                break
            time.sleep(0.6)
            print(' ')
            print('=='*20)

#TRIGONOMÉTRICAS:
        if funcao==2:

            print('\033[35mTRIGONOMÉTRICAS:\033[m')
            print('\033[33m[ 1 ]\033[m SENO')
            print('\033[33m[ 2 ]\033[m COSSENO')
            print('\033[33m[ 3 ]\033[m TANGENTE')
            print('\033[33m[ 4 ]\033[m ARCSEN')
            print('\033[33m[ 5 ]\033[m ARCCOS')
            print('\033[33m[ 6 ]\033[m ARCTAN')
            opcao_trigonometria= int(input('Opção:'))

            while opcao_trigonometria != 1 and opcao_trigonometria  != 2 and opcao_trigonometria != 3 and opcao_trigonometria != 4 and opcao_trigonometria != 5 and opcao_trigonometria !=6:
                print('\033[31mDIGITE A OPÇÃO CERTA\033[m')
                time.sleep(1)
                opcao_trigonometria = int(input('Opção:'))

# Condições para validar as escolhas sobre TRIGONOMÉTRICAS!

    #SENO
            if opcao_trigonometria == 1:
                grau_radiano= str(input('Resultado em GRAU ou RADIANO [G/R]:')).upper().strip()[0]
                if grau_radiano == 'R':
                    numero= float(input('Ângulo em radianos:'))
                    print(f'Seno de {numero} = {math.sin(numero):.1f}')
                elif grau_radiano == 'G':
                    numero = float(input('Ângulo em graus:'))
                    print(f'Seno de {numero} = {math.sin(math.radians(numero)):.1f}')

    #COSSENO
            if opcao_trigonometria == 2:
                grau_radiano= str(input('Resultado em GRAU ou RADIANO [G/R]:')).strip().upper()[0]
                if grau_radiano == 'R':
                    numero= float(input('Ângulo em radianos:'))
                    print(f'Cosseno de {numero} = {math.cos(numero):.1f}')
                elif grau_radiano == 'G':
                    numero= float(input('Ângulo em graus:'))
                    print(f'Cosseno de {numero} = {math.cos(math.radians(numero)):.1f}')

    #TANGENTE
            if opcao_trigonometria == 3:
                grau_radiano = str(input('Resultado em GRAU ou RADIANO [G/R]:')).strip().upper()[0]
                if grau_radiano == 'R':
                    numero= float(input('Ângulo em radianos:'))
                    print(f'Tangente de {numero} = {math.tan(numero):.1f}')
                elif grau_radiano == 'G':
                    numero= float(input('Ângulo em graus:'))
                    print(f'Tangente de {numero} = {math.tan(math.radians(numero)):.1f}')

    #ARCSEN
            if opcao_trigonometria == 4:
                grau_radiano = str(input('Resultado em GRAU ou RADIANO [G/R]:')).strip().upper()[0]
                if grau_radiano == 'R':
                    numero= float(input('Ângulo em radianos:'))
                    print(f'Arcoseno de {numero} = {math.asin(numero):.1f}')
                if grau_radiano == 'G':
                    numero= float(input('Ângulo em graus'))
                    print(f'Arcoseno de {numero} = {math.asin(math.radians(numero)):.1f}')

    #ARCCOS
            if opcao_trigonometria == 5:
                grau_radiano = str(input('Resultado em GRAU ou RADIANO [G/R]:')).strip().upper()[0]
                if grau_radiano == 'R':
                    numero= float(input('Ângulo em radianos:'))
                    print(f'Arcocosseno de {numero} = {math.acos(numero):.1f}')
                if grau_radiano == 'G':
                    numero= float(input('Ângulo em graus:'))
                    print(f'Arcosseno de {numero} = {math.acos(math.radians(numero)):.1f}')

    #ARCTAN
            if opcao_trigonometria == 6:
                grau_radiano= str(input('Resultado em GRAU ou RADIANO [G/R]:')).strip().upper()[0]
                if grau_radiano == 'R':
                    numero= float(input('Ângulo em radianos:'))
                    print(f'Arcotangente de {numero} = {math.atan(numero):.1f}')
                if grau_radiano == 'G':
                    numero= float(input('Ângulo em graus:'))
                    print(f'Arcotangente de {numero} = {math.atan(math.radians(numero)):.1f}')

#VER SE O USUÁRIO QUER COTINUAR NA FUNÇÃO TRIGONOMÉTRICA
            continuar = str(input('Deseja continuar na função TRIGONOMÉTRICA [S/N]')).strip().upper()[0]
            if continuar == 'N':
                print('\033[34mVOLTANDO..\033[m')
                time.sleep(0.6)
                break
            time.sleep(0.6)
            print(' ')
            print('==' * 20)

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

# Condições para validar as escolhas sobre LOGARITMICA...!
            if opcao_logarimo != 1 and opcao_logarimo != 2 and opcao_logarimo != 3 and opcao_logarimo != 4:
                print('\033[31mOPÇÃO INVÁLIDA!\033[m')
                print('Ecolha somente 1, 2, 3 ou 4.')
                time.sleep(1)

        #LOGARITIMO NATURAL
            elif opcao_logarimo == 1:
                logaritmo = float(input('Logartimo:'))
                print(f'Log de {logaritmo} = {math.log1p(logaritmo):.1f}')

        #LOGARITIMO BASE
            elif opcao_logarimo == 2:
                base = float(input('Base:'))
                x = float(input('logaritmando:'))
                print(f'{x} na base de{base} = {math.log(x, base):.1f}')

        #EXPONENCIAL
            elif opcao_logarimo == 3:
                base = float(input('Base:'))
                expoente = float(input('Expoente:'))
                print(f'{base**expoente:.1f}')

        #POTÊNCIA DE 10
            elif opcao_logarimo == 4:
                base = float(input('Base:'))
                print(f'Base de {base} elevado a 10 = {math.pow(base, 10):.1f}')

            #VER SE O USUÁRIO QUER COTINUAR NA FUNÇÃO LOGARITMICA..
            continuar = str(input('Deseja continuar na função LOGARÍTMICA [S/N]')).strip().upper()[0]
            if continuar == 'N':
                print('\033[34mVOLTANDO..\033[m')
                time.sleep(0.6)
                break
            time.sleep(0.6)
            print(' ')
            print('==' * 20)

#VERIFICAR SE O USUÁRIO QUER CONTINUAR USANDO A CALCULADORA POR COMPLETO
    continuar = str(input('Deseja continuar com a CALCULADORA [S/N]:')).upper().strip()[0]
    if continuar == 'N':
        print('=='*20)
        print(' ')
        print('\033[33mOBRIGADO POR USAR MINHA CALCULADORA<3\033[m')
        print(' ')
        print('==' * 20)
        break