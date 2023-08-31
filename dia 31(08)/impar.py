def lista_impar(lista):
    return lista[::2]

def lista_reversa(lista):
    return lista[::-1]

def metade_da_lista(meio):
    meiuca = len(meio) // 2
    return meio[:meiuca]

def soma_lista(lista):
    total = 0
    for valor in lista:
        total = total + valor
    return total
#
def maiorvalor(lista):
    return max(lista,key=abs)