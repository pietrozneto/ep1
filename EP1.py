import random

def dado_mesa(fichas):
    dado_mesa = randint(1,6)+ randint(1,6)
    print('Os dados deram {0}'.format(dado_mesa))
    return dado_mesa
def pass_line_bet(dado_mesa, Valor_PL):
    if dado_mesa == 7 or dado_mesa == 11:
        lucro = Valor_PL
        print('Você ganhou {0} fichas'.format(Valor_PL))
        print('Você tem {0} fichas'.format(fichas))
    elif dado_mesa == 2 or dado_mesa == 3 or dado_mesa == 12:
        lucro = -Valor_PL
        print('Você perdeu {0} fichas'.format(Valor_PL))
        print('Você tem {0} fichas'.format(fichas))
    else:
        print('Etapa: Poit')
    return lucro
def point(dado_mesa, Valor_P):
    ciclo_point = True
    point = dado_mesa
    while ciclo_point:
        dado_mesa = dado_mesa(fichas)
        if point == dado_mesa:
            lucro = Valor_PL
            print('Você ganhou {0} fichas'.format(Valor_P))
            print('Você tem {0} fichas'.format(fichas))
            ciclo_point = False
        elif dado_mesa == 7:
            lucro = -Valor_PL
            print('Você perdeu {0} fichas'.format(Valor_PL))
            print('Você tem {0} fichas'.format(fichas))
            ciclo_point = False
    return lucro