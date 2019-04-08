from bd import ler_gastos,ler_receitas
def calc_gastos():
    gastos = ler_gastos()
    gastos = dict(gastos)
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
    receitas = ler_receitas()
    receitas = dict(receitas)
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
    calculo = {'gastos':gastos,'receitas':receitas,'fechamento':fechamento}
    return  calculo
