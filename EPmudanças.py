from random import randint

def dado_mesa(fichas): #função que define o valor da soma dos dados
    dado_mesa = randint(1,6)+ randint(1,6)
    print('Os dados deram {0}'.format(dado_mesa))
    return dado_mesa
def pass_line_bet(dado_mesa, Valor_PL):#função da aposta pass line
    if dado_mesa == 7 or dado_mesa == 11:
        lucro = Valor_PL
        print('Você ganhou {0} fichas'.format(Valor_PL))
    elif dado_mesa == 2 or dado_mesa == 3 or dado_mesa == 12:
        lucro = -Valor_PL
        print('Você perdeu {0} fichas'.format(Valor_PL))
    else:
        print('Etapa: Poit')
        Valor_PL = Valor_P
        Valor_PL = 0
        point(dado_mesa, Valor_PL)
    return lucro
def point(dado_mesa, Valor_P): #função da aposta point
    ciclo_point = True
    point = dado_mesa
    while ciclo_point:
        dado_mesa = dado_mesa(fichas)
        if point == dado_mesa:
            lucro = Valor_PL
            print('Você ganhou {0} fichas'.format(Valor_P))
            ciclo_point = False
        elif dado_mesa == 7:
            lucro = -Valor_PL
            print('Você perdeu {0} fichas'.format(Valor_PL))
            ciclo_point = False
    return lucro
def field(dado_mesa, Valor_F): #função da aposta fields
    if dado_mesa >=5 and dado_mesa <= 8:
        lucro = -Valor_F
    elif dado_mesa == 2:
        lucro = 2*Valor_F
    elif dado_mesa == 12:
        lucro = 3*Valor_F
    else:
        lucro = Valor_F
    return lucro
def any_craps(dado_mesa, Valor_A): #função da aposta any craps
    if dado_mesa == 2 or dado_mesa==3 or dado_mesa==12:
        lucro = 7*Valor_A
    else:
        lucro = -Valor_A
    return lucro
def twelve(dado_mesa, Valor_T): #função da aposta twelve
    if dado_mesa == 12:
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
print('Pass Line Bet, Field, Any Craps, Twelvez (PL/F/A/T)')
x = input('Qual aposta tipo de aposta deseja fazer? ')
while fichas != 0 or continuar_apostando == 'nao':
    if PL == True:
        lucro += pass_line_bet(dado_mesa, Valor_PL)
    if F == True:
        lucro += field(dado_mesa, Valor_F)
    if A == True:
        lucro += any_craps(dado_mesa, Valor_A)
    if T == True:
        lucro += twelve(dado_mesa, Valor_T)
    
    while x!='nao':
        if x == 'PL':
            PL = True
            Valor_PL += int(input('Quanto deseja apostar? '))
        elif x == 'F':
            F = True
            Valor_F += int(input('Quanto deseja apostar? '))
        elif x == 'A':
            A = True
            Valor_A += int(input('Quanto deseja apostar? '))
        elif x == 'T':
            T = True
            Valor_T += int(input('Quanto deseja apostar? '))
        else:
            break
        print('Pass Line Bet, Field, Any Craps, Twelvez, Não (PL/F/A/T/nao)')
        x = input('Deseja fazer outra aposta ? ')

print('cabo')
