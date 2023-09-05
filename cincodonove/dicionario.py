
#dicionario
cadastros = {"nome":"mingau","email":"mingau@gmail.com","saida":"58"}
print(cadastros)
print(cadastros["nome"])
print(cadastros["email"])
print(cadastros["saida"])
pass
#dicionario dentro de uma lista
cadastros = [{"nome":"mingau","email":"mingau@gmail.com","saldo":"58"}]
print(cadastros[0]["nome"])
pass
#dois dicionarios dentro de uma lista
cadastros = [{"nome":"mingau","email":"mingau@gmail.com","saldo":58},{"nome":"roger","email":"roger@gmail.com","saldo":10.24}]
print(cadastros[0]["nome"])


#construindo uma nova função
#calcula saldo médio
def calcular_saldo_médio(cadastros):
    saldo_médio = 0
    for elemento in cadastros:
        saldo_médio += saldo_médio + elemento["saldo"]
    return saldo_médio / len(cadastros)

saldo = calcular_saldo_médio(cadastros)
print(saldo)

#função que filtra a lista que tem Gmail
def filtrar_por_email(cadastros):
    for elemento in cadastros.copy():
        if "gmail" in elemento["email"]:
            cadastros.remove(elemento)
    return cadastros

filtro = filtrar_por_email(cadastros)
print(filtro)

#filtro de lista dinamica
def filtrar_por_emaiLl(cadastros,provedor):
    lista_filtrada = []
    for elemento in cadastros.copy():
        if provedor not in elemento["email"]:
            lista_filtrada.append(elemento)
    return lista_filtrada()

#filtra a lista por saldo
def filtrar_por_saldo(cadastros, saldo, parametro):
    lista_filtrada = []
    for elemento in cadastros.copy():
        if parametro.upper == "maior" and elemento["saldo"]  > saldo:
            lista_filtrada.append(elemento)
    # for elemento in cadastros:
    #     if elemento >= 1000 in elemento["saldo"]:
    # return lista_por_saldo 
