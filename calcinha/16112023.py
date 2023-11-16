def load_data_base():
    with open('datatran2020.csv', 'r', encoding= 'utf-8') as f:
        dados = [linha.split(',') for linha in f]
        colunas = dados[0]
        bd = dict()
        for id, coluna in enumerate(colunas):
            bd[coluna] = [item[id] for item in dados [1:]] 
    return bd

"""1- Quais os valores distintos existente na coluna fase dia?"""
def questao_01():
    bd = load_data_base()
    coluna = bd ['fase_dia']
    valores = set(coluna)
    print(valores)

"""2- Qual a frequência de acidentes por fase do dia?"""
def questao_02():
    bd = load_data_base()
    valores = bd ['fase_dia']
    colunas = set(valores)
    freq_fase_dia = dict()
    for coluna in colunas:
        freq_fase_dia[coluna] = sum([1 for item in valores if item == coluna])
    print(freq_fase_dia)

"""3- Qual a frequência de acidentes por UF?"""
def questao_03():
    bd = load_data_base()
    valores = bd ['uf']
    colunas = set(valores)
    freq_por_uf = dict()
    for coluna in colunas:
        freq_por_uf[coluna] = sum([1 for item in valores if item == coluna])
    print(freq_por_uf)

"""4- Quantas mortes houveram no estado do Pará?"""
def questao_04():
    bd = load_data_base()
    ufs = bd['uf']
    mortes = bd['mortos']
    total = sum([int(valor) for uf, valor in zip(ufs, mortes) if uf == 'PA'])
    print(total)
questao_04()


