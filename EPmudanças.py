from random import randint
from time import sleep
def dado_mesa(fichas): #função que define o valor da soma dos dados
    dado_mesa = randint(1,6)+ randint(1,6)
    print('Os dados deram {0}'.format(dado_mesa))
    return dado_mesa
def pass_line_bet(dado_mesa, Valor_PL):#função da aposta pass line
    if dado_rodada == 7 or dado_rodada == 11:
        lucro = Valor_PL
        print('Você ganhou {0} fichas'.format(Valor_PL))
    elif dado_rodada == 2 or dado_rodada == 3 or dado_rodada == 12:
        lucro = -Valor_PL
        print('Você perdeu {0} fichas'.format(Valor_PL))
    else:
        print('Etapa: Poit')
        sleep(1)
        Valor_P = Valor_PL
        Valor_PL = 0
        dado_point = dado_rodada
        lucro = point(dado_point, Valor_PL)
    return lucro
def point(dado_point, Valor_P): #função da aposta point
    ciclo_point = True
    while ciclo_point:
        dado_rodada_point = dado_mesa(fichas)
        if dado_point == dado_rodada_point:
            lucro = Valor_PL
            print('Você ganhou {0} fichas'.format(Valor_P))
            print('Você tem {0} fichas'.format(fichas))
            ciclo_point = False
        elif dado_rodada_point == 7:
            lucro = -Valor_PL
            print('Você perdeu {0} fichas'.format(Valor_PL))
            print('Você tem {0} fichas'.format(fichas))
            ciclo_point = False
    return lucro
def field(dado_rodada, Valor_F): #função da aposta fields
    if dado_rodada >=5 and dado_rodada <= 8:
        lucro = -Valor_F
    elif dado_rodada == 2:
        lucro = 2*Valor_F
    elif dado_rodada == 12:
        lucro = 3*Valor_F
    else:
        lucro = Valor_F
    return lucro
def any_craps(dado_rodada, Valor_A): #função da aposta any craps
    if dado_rodada == 2 or dado_rodada==3 or dado_rodada==12:
        lucro = 7*Valor_A
    else:
        lucro = -Valor_A
    return lucro
def twelve(dado_rodada, Valor_T): #função da aposta twelve
    if dado_rodada == 12:
        lucro = -12*Valor_T
    else:
        lucro = Valor_T
    return lucro
fichas = 100
lucro = 0
Valor_PL = 0
Valor_P = 0
Valor_F = 0
Valor_A = 0
Valor_T = 0
PL = False
F = False
A = False
T = False
continuar_apostando = 'sim'
x = 'sim'
while continuar_apostando == 'nao':
    if PL or F or A or T:
        print('Você tem {} fichas'.format(fichas))
        dado_rodada = dado_mesa(fichas)
        sleep(1)
    if PL == True:
        lucro += pass_line_bet(dado_rodada, Valor_PL)
        sleep(1)
    if F == True:
        lucro += field(dado_rodada, Valor_F)
        sleep(1)
    if A == True:
        lucro += any_craps(dado_rodada, Valor_A)
        sleep(1)
    if T == True:
        lucro += twelve(dado_rodada, Valor_T)
        sleep(1)
    fichas += lucro
    lucro = 0
    PL = False
    F = False
    A = False
    T = False
    x = 'sim'
    while x!='nao':
        print('Você tem {} fichas'.format(fichas))
        if x == 'sim':
            print('Pass Line Bet, Field, Any Craps, Twelvez, Não (PL/F/A/T)')
            x = input('Qual aposta deseja fazer outra aposta ? ')
        if x == 'PL':
            PL = True
            print('Você tem {} fichas'.format(fichas))
            Valor_PL += int(input('Quanto deseja apostar? '))
            fichas -= Valor_PL
        elif x == 'F':
            F = True
            print('Você tem {} fichas'.format(fichas))
            Valor_F += int(input('Quanto deseja apostar? '))
            fichas -= Valor_F
        elif x == 'A':
            A = True
            print('Você tem {} fichas'.format(fichas))
            Valor_A += int(input('Quanto deseja apostar? '))
            fichas -= Valor_A
        elif x == 'T':
            T = True
            print('Você tem {} fichas'.format(fichas))
            Valor_T += int(input('Quanto deseja apostar? '))
            fichas -= Valor_T
        elif x == 'sim':
            print('Pass Line Bet, Field, Any Craps, Twelvez, Não (PL/F/A/T/nao)')
            x = input('Deseja fazer outra aposta ? ')
        else:
            break
        x = input('Deseja continuar apostando? (sim/nao) ')
print('cabo')
