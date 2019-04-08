from os import system as sy
from time import sleep as sl
from obter import pega_gastos, pega_receitas
from huds import hud_mais, hud_final
def main():
    '''
1 cadastrar gastos
2 cadastrar receitas
3 alterar gastos
4 alterar receitas
5 visualizar gastos
6 visualizar receitas
7 visualizar tudo
    '''
    chave_interna = True
    while chave_interna == True:
        sy('cls')
        print('-'*50)
        print(f'{"Selecione com número uma das opções a seguir":^40}')
        print('-'*50)
        opcoes={1:'CADASTRAR GASTOS',2:'CADASTRAR RECEITAS',3:'ALTERAR GASTOS',4:'ALTERAR RECEITAS',5:'VISUALIZAR GASTOS',6:'VISUALIZAR RECEITAS',7:'VISUALIZAR TUDO'}
        for opcao in opcoes:
            print(f'''{opcao:.<15}{opcoes[opcao]:<7}''')
        print('-'*50)
        opcao = input('DIGITE SUA OPÇÃO : ').upper()
        if opcao not in '1234567':
            sy('cls')
            print('-'*40)
            print('Por favor digite um número ou aperte ALT+F4 para fechar o sistema')
            print('-'*40)
            sl(2)
        else:
            chave_interna = False
            opcao = int(opcao)
    if opcao == 1:
        pega_gastos()
    elif opcao == 2:
        pega_receitas()
    elif opcao == 3:
        sy('cls')
        print('-'*60)
        print(f'{"AINDA EM DESENVOLVIMENTO VOLTE MAIS TARDE":^60}')
        print('-'*60)
        sl(3)
    elif opcao == 4:
        sy('cls')
        print('-'*60)
        print(f'{"AINDA EM DESENVOLVIMENTO VOLTE MAIS TARDE":^60}')
        print('-'*60)
        sl(3)
    elif opcao == 5:
        sy('cls')
        print('-'*60)
        print(f'{"AINDA EM DESENVOLVIMENTO VOLTE MAIS TARDE":^60}')
        print('-'*60)
        sl(3)
        
        #hud_mais(gastos)
    elif opcao == 6:
        sy('cls')
        print('-'*60)
        print(f'{"AINDA EM DESENVOLVIMENTO VOLTE MAIS TARDE":^60}')
        print('-'*60)
        sl(3) 
        #hud_mais(receitas)
    elif opcao == 7:
        sy('cls')
        print('-'*60)
        print(f'{"AINDA EM DESENVOLVIMENTO VOLTE MAIS TARDE":^60}')
        print('-'*60)
        sl(3)
        #hud_final(gastos,receitas,fechamento)
    else:
        sy('cls')
        print('-'*40)
        print('Valor inserido não encontrado, favor tentar novamente.')
        print('-'*40)
        sl(1)


while True:
    main()









        

    
