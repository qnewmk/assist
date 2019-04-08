from os import system as sy
from time import sleep as sl
from huds import hud_mais

def pega_gastos():
    chave_interna = True
    chave_externa = True
    gastos = {}
    nome = ''
    valor = ''
    while chave_externa == True:
        try:
            hud_mais(gastos)
            chave_interna = True
            while chave_interna == True:
                sy('cls')
                print('''DIGITE SAIR A QUALQUER MOMENTO PARA TERMINAR A INSERÇÃO DE DADOS''')
                hud_mais(gastos)
                nome = str(input('Escreva o nome do que você quer acrescentar no sistema como gasto : ')).upper().strip()
                if nome == 'SAIR':
                    chave_externa = False
                    chave_interna = False
                elif nome == '':
                    sy('cls')
                    print('-'*40)
                    print('Valor inserido é invalido, favor tentar novamente.')
                    print('-'*40)
                    sl(2)
                    chave_interna = True
                else:
                    chave_interna = False 
            if chave_externa == False:
                break
            if chave_interna == False:
                chave_interna = True
            while chave_interna == True:
                sy('cls')
                print('''DIGITE SAIR A QUALQUER MOMENTO PARA TERMINAR A INSERÇÃO DE DADOS''')
                hud_mais(gastos)
                valor =input(f'''Escreva a quantia que gastará neste mês com {nome} : ''').upper()
                if valor == 'SAIR':
                    chave_externa = False
                    chave_interna = False
                elif valor == '':
                    sy('cls')
                    print('-'*40)
                    print('Valor inserido não encontrado, favor tentar novamente.')
                    print('-'*40)
                    sl(1)
                    chave_interna = True
                elif valor[0] not in '0123456789':
                    sy('cls')
                    print('-'*40)
                    print('Por favor digite um número ou digite SAIR para sair do modo inserção de dados')
                    print('-'*40)
                    sl(2)
                    chave_interna = True
                else:
                    chave_interna = False
                valor=float(valor)
            gastos[nome]=valor
            if chave_externa == False:
                break
        except:
            if nome == '' or valor == '' or nome == None or valor == None or nome == 'SAIR' or valor == 'SAIR':
                break
        if chave_externa == False:
            break
    return gastos


def pega_receitas():
    chave_interna = True
    chave_externa = True
    receitas = {}
    nome = ''
    valor = ''
    while chave_externa == True:
        try:
            hud_mais(receitas)
            chave_interna = True
            while chave_interna == True:
                sy('cls')
                print('''DIGITE SAIR A QUALQUER MOMENTO PARA TERMINAR A INSERÇÃO DE DADOS''')
                hud_mais(receitas)
                nome = str(input('Escreva o nome do que você quer acrescentar no sistema como receita : ')).upper().strip()
                if nome == 'SAIR':
                    chave_externa = False
                    chave_interna = False
                elif nome == '':
                    sy('cls')
                    print('-'*40)
                    print('Valor inserido é invalido, favor tentar novamente.')
                    print('-'*40)
                    sl(2)
                    chave_interna = True
                else:
                    chave_interna = False 
            if chave_externa == False:
                break
            if chave_interna == False:
                chave_interna = True
            while chave_interna == True:
                sy('cls')
                print('''DIGITE SAIR A QUALQUER MOMENTO PARA TERMINAR A INSERÇÃO DE DADOS''')
                hud_mais(receitas)
                valor =input(f'''Escreva a quantia que receberá neste mês com {nome} : ''').upper()
                if valor == 'SAIR':
                    chave_externa = False
                    chave_interna = False
                elif valor == '':
                    sy('cls')
                    print('-'*40)
                    print('Valor inserido não encontrado, favor tentar novamente.')
                    print('-'*40)
                    sl(1)
                    chave_interna = False
                elif valor[0] not in '0123456789':
                    sy('cls')
                    print('-'*40)
                    print('Por favor digite um número ou digite SAIR para sair do modo inserção de dados')
                    print('-'*40)
                    sl(2)
                    chave_interna = True
                else:
                    chave_interna = False
                valor=float(valor)
            receitas[nome]=valor
            if chave_externa == False:
                break
        except:
            if nome == '' or valor == '' or nome == None or valor == None or nome == 'SAIR' or valor == 'SAIR':
                break
        if chave_externa == False:
            break
    return receitas
