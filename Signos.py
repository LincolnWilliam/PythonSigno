dia = int(input('informe dia de nascimento: '))
mes = int(input('informe o codigo do mês de nascimento: \n'
                '1-Janeiro '
                '2-Fevereiro '
                '3-Março '
                '4-Abril '
                '5-Maio '
                '6-Junho '
                '7-Julho '
                '8-Agosto '
                '9-Setembro '
                '10-Outubro '
                '11-Novembro '
                '12-Dezembro: '))

if (dia >= 21 and mes == 3) or (dia <= 20 and mes == 4):
    print('seu signo é Áries')

elif (dia >= 21 and mes == 4) or (dia <= 20 and mes == 5):
    print('seu signo é Touro')

elif (dia >= 21 and mes == 5) or (dia <= 20 and mes == 6):
    print('seu signo é Gêmeos')

elif (dia >= 21 and mes == 6) or (dia <=22 and mes == 7):
    print('seu signo é Câncer')

elif (dia >= 23 and mes == 7) or (dia <= 22 and mes == 8):
    print('seu signo é Leão')

elif (dia >= 23 and mes == 8) or (dia <= 22 and mes == 9):
    print('Seu signo é Virgem')

elif (dia >= 23 and mes == 9) or (dia <= 22 and mes == 10):
    print('seu signo é Libra')

elif (dia >= 23 and mes == 10) or (dia <= 21 and mes == 11):
    print('seu signo é Escorpião')

elif (dia >= 22 and mes == 11 ) or (dia <= 21 and mes == 12):
    print('seu signo é Sagitário')

elif (dia >= 22 and mes == 12 ) or (dia <=20 and mes == 1):
    print('seu signo é Capricórnio')

elif (dia >= 21 and mes == 1) or (dia <= 18 and mes == 2):
    print('seu signo é Aquário')

elif (dia >= 19 and mes == 2) or (dia <= 20 and mes == 3):
    print('seu signo é Peixes ')










