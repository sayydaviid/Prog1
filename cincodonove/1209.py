
#dicionario
cadastros = {"nome":"mingau","email":"mingau@gmail.com","saida":"58"}
print(cadastros)
print(cadastros["nome"])
print(cadastros["email"])
print(cadastros["saida"])
#dicionario dentro de uma lista
cadastros = [{"nome":"mingau","email":"mingau@gmail.com","saldo":"58"}]
print(cadastros[0]["nome"])

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

   
 #filtrando a lista pelo tipo de arquivo que eu quero
def filtrar_por_tipo(lista, tipo):
    lista_vazia = []
    for item in lista:
        if type(item) == tipo:
            lista_vazia.append(item)
    return lista_vazia


lista = ['a','b','c',1,2,3]
lista_vazia = filtrar_por_tipo(lista, int)
print(lista_vazia)



#dois dicionarios dentro de uma lista
cadastrosos = [{"nome":"mingau","email":"mingau@gmail.com","saldo":58},{"nome":"roger","email":"roger@gmail.com","saldo":10.24}]

def extrair_nomes(cadastrosos):
    lista_com_nomes = []
    for nomes in cadastrosos:
        lista_com_nomes.append(nomes["nome"])
    return lista_com_nomes




#dois dicionarios dentro de uma lista
cadastrosos = [{"nome":"mingau","email":"mingau@gmail.com","saldo":58},{"nome":"roger","email":"roger@gmail.com","saldo":10.24}]

lista_com_nomes = extrair_nomes(cadastrosos)
print(lista_com_nomes)

def formatar_nomes(cadastrosos):
    """ 
    mapeia uma lista de string para uma lista de string em capslock
    argumentos: lista de string
    retorno: lista de string em capslock

    """
    lista_formatada = []
    for item in cadastrosos:
        lista_formatada.append(item.upper())
    return lista_formatada
lista_nomes = formatar_nomes(lista_com_nomes)
print(lista_nomes)

def formatar_nomes(cadastrosos):
    """ 
    mapeia uma lista de string para uma lista de string em capslock
    argumentos: lista de string
    retorno: lista de string em capslock

    """
    lista_formatada = []
    for item in cadastrosos:
        lista_formatada.append(item.lower())
    return lista_formatada
lista_nomes = formatar_nomes(lista_com_nomes)
print(lista_nomes)


# def formatar_nomes(cadastrosos,formatacao):
#     if formatacao == 'CAIXA_ALTA':
#         return formatar_caixa_alta(cadastrosos)
#     elif formatacao == 'caixa_baixa':

#     for item in cadastrosos:
#         lista_formatada = 



def calcular_tamanho_nomes(cadastrosos):
    lista_formatadax = []
    for item in cadastrosos:
        lista_formatadax.append(len(item))
    return lista_formatadax
lista_tamanho = calcular_tamanho_nomes(lista_com_nomes)
print(lista_tamanho)

# def (cadastrosos):
#     for item in cadastrosos:

#         len(item)