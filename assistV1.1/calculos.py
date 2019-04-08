from huds import hud_final

def calc_gastos():
    gastos = pega_gastos()
    total = 0
    '''
    item contem a chave de gastos;
    dados[item] contem o valor da chave de gastos;
    '''
    for item in gastos:
        total += gastos[item]
    gastos['TOTAL'] = total
    return gastos


def calc_receitas():
    receitas = pega_receitas()
    total = 0
    '''
    item contem a chave de receitas;
    receitas[item] contem o valor da chave de receitas;
    '''
    for item in receitas:
        total += receitas[item]
    receitas['TOTAL'] = total
    return receitas


def calc_final():
    gastos = calc_gastos()
    receitas =  calc_receitas()
    fechamento = receitas["TOTAL"]-gastos["TOTAL"]
    hud_final(gastos,receitas,fechamento)

