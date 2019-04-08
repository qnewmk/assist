from os import system as sy


def hud_final(gastos,receitas,fechamento):
    sy('cls')
    print('-'*40)
    print(f'{"LISTAGEM DE VALORES DE GASTOS":^40}')
    print('-'*40)
    print(f'{"NOME":.<30}{"VALOR"}')
    print('-'*40)
    for item in gastos:
        print(f'''{item:.<30}R${gastos[item]:<7}''')
    print('-'*40)
    print(f'{"LISTAGEM DE VALORES DE RECEITAS":^40}')
    print('-'*40)
    print(f'{"NOME":.<30}{"VALOR"}')
    print('-'*40)
    for item in receitas:
        print(f'''{item:.<30}R${receitas[item]:<7}''')
    print('-'*40)
    print(f'Vai te sobrar : R${fechamento}')
    print('-'*40)
    print('''

Se o numero acima der positivo, significa que suas finanças mediante ao que nos foi passado está no verde.
Caso o número seja negativo, rode o programa novamente para ter certeza de que esrevera
todos os numeros corretamente e se escreveu e ainda assim o numero acima estiver negativo...
suas finanças estão no vermelho infelizmente.''')


def hud_mais(dados):
    total = 0
    print('-'*40)
    print(f'{"LISTAGEM DE VALORES":^40}')
    print('-'*40)
    print(f'{"NOME":.<30}{"VALOR"}')
    print('-'*40)
    for item in dados:
        print(f'''{item:.<30}R${dados[item]:<7}''')
        total+=dados[item]
    print('-'*40)
    print(f'TOTAL ATÉ O MOMENTO : R${total}')
    print('-'*40)
