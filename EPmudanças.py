from random import randint
from time import sleep
def dado_mesa(fichas): #função que define o valor da soma dos dados
    dado_mesa = randint(1,6)+ randint(1,6)
    print('Os dados deram {0}'.format(dado_mesa))
    return dado_mesa
def pass_line_bet(dado_mesa, Valor_PL):#função da aposta pass line
    lucro = 0
    if dado_rodada == 7 or dado_rodada == 11:
        lucro = 2*Valor_PL
        print('Você ganhou {0} fichas'.format(Valor_PL))
    elif dado_rodada == 2 or dado_rodada == 3 or dado_rodada == 12:
        print('Você perdeu {0} fichas'.format(Valor_PL))
    else:
        print('Etapa: Poit')
        sleep(1)
        dado_point = dado_rodada
        lucro = point(dado_point, Valor_PL)
    return lucro
def point(dado_point, Valor_P): #função da aposta point
    lucro = 0
    ciclo_point = True
    while ciclo_point:
        dado_rodada_point = dado_mesa(fichas)
        if dado_point == dado_rodada_point:
            lucro = 2*Valor_PL
            print('Você ganhou {0} fichas'.format(Valor_PL))
            ciclo_point = False
        elif dado_rodada_point == 7:
            print('Você perdeu {0} fichas'.format(Valor_PL))
            ciclo_point = False
    return lucro
def field(dado_rodada, Valor_F): #função da aposta fields
    lucro = 0
    if dado_rodada >=5 and dado_rodada <= 8:
        print('Você ganhou {0} fichas'.format(Valor_F))
    elif dado_rodada == 2:
        lucro = 3*Valor_F
        print('Você ganhou {0} fichas'.format(Valor_F))
    elif dado_rodada == 12:
        lucro = 4*Valor_F
        print('Você ganhou {0} fichas'.format(Valor_F))
    else:
        lucro = 2*Valor_F
        print('Você ganhou {0} fichas'.format(Valor_F))
    return lucro
def any_craps(dado_rodada, Valor_A): #função da aposta any craps
    lucro = 0
    if dado_rodada == 2 or dado_rodada==3 or dado_rodada==12:
        lucro = 7*Valor_A
    return lucro
def twelve(dado_rodada, Valor_T): #função da aposta twelve
    lucro = 0
    if dado_rodada == 12:
        lucro = 12*Valor_T        
    return lucro
fichas = 100
lucro_total = 0
Valor_PL = 0
Valor_F = 0
Valor_A = 0
Valor_T = 0
PL = False
F = False
A = False
T = False
sair_do_programa = 'nao'
x = 'sim'
while sair_do_programa == 'nao':
    if PL or F or A or T:
        dado_rodada = dado_mesa(fichas)
        sleep(1)
    if PL == True:
        lucro_total += pass_line_bet(dado_rodada, Valor_PL)
        sleep(1)
    if F == True:
        lucro_total += field(dado_rodada, Valor_F)
        sleep(1)
    if A == True:
        lucro_total += any_craps(dado_rodada, Valor_A)
        sleep(1)
    if T == True:
        lucro_total += twelve(dado_rodada, Valor_T)
        sleep(1)
    fichas += lucro_total
    print('Você tem {} fichas'.format(fichas))
    lucro = 0
    PL = False
    F = False
    A = False
    T = False
    Valor_PL = 0
    Valor_F = 0
    Valor_A = 0
    Valor_T = 0
    if fichas == 0:
        print('Suas fichas acabaram ')
        break
    if x =='nao':
        sair_do_programa = input('Deseja sair do programa? (sim/nao) ')
    x = 'sim'
    while x!='nao':
        if sair_do_programa == 'sim':
            break
        print('Você tem {} fichas'.format(fichas))
        if x == 'sim':
            print('Pass Line Bet, Field, Any Craps, Twelvez (PL/F/A/T)')
            x = input('Qual aposta deseja fazer ? ')
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
            print('Essa não é uma aposta valida')
            sair_do_programa = 'sim'
            break
        x = input('Deseja fazer outra aposta ? (sim/nao) ')
print('cabo')
