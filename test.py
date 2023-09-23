# Questão 01: Dada duas listas de strings de mesmo tamanho, faça o mapeamento para
# obter uma lista em que cada elemento seja a concatenação dos elementos de mesmo
#índice das duas listas. Retorna a lista resultante.
#definindo a função #(v1)
def concatenar(lista_1,lista_2):
#fazendo uma lista vazia para receber os valores
    lista_3 = []
#fazendo um for para percorrer a lista e usando o len para saber o tamanho da lista
    for item in range(len(lista_1)):
#fazendo o append para adicionar os valores na lista vazia
        lista_3.append(lista_1[item]+lista_2[item])
#retornando a lista vazia com os valores adicionados
    return lista_3

#primeira questao simplificada(v2)
def concatenadinhas(lista_1,lista_2):
    return[(lista_1[item]+lista_2[item])
           for item in range(len(lista_1))]
lista_1 = ["t","b","c","d"]
lista_2 = ["u","f","g","h"]
lista3 = concatenar(lista_1,lista_2)
print(lista3)


#avaliação do hidaka
# 1 = lista.ipynb
# 2 = list compress
# 3 = operadores
# 4 = função

#Questão 02: Dada uma lista de números inteiros, faça o mapeamento para obter uma
#lista de números primos. Cada elemento da lista deve ser igual ao menor número
#primo maior que o elemento corrente da lista.
def primo(lista):
    lista_primo = []
    for item in lista:
        for i in range(2,item):
            if item % i == 0:
                item += 1
        lista_primo.append(item)
    return lista_primo

lista = [1,2,3,4,5,6,7,8,9,10]
lista_primo = primo(lista)
print(lista_primo)


#questao 2 feita pelo hidaka
def eh_primo(valor):
    if valor <= 1:
        return False
    for divisor in range(2,valor):
        if valor % divisor == 0:
            return False
    return True 
def maior_primo_numero(valor):
    valor =+ 1
    while not eh_primo(valor):
        valor =+ 1
    return valor
def construir_lista_primo(valor):
    return[maior_primo_numero(item) for item in lista]
lista_primos = [9,-5,1,4,18]
lista_primaa = construir_lista_primo(lista_primos)
print(lista_primaa)

# Questão 03: Dada uma lista de string, faça um filtro para obter uma lista somente com
# os elementos cujo tamanho da string seja menor que 10. A lista resultante deve estar
# ordenada em ordem alfabética. Retorna a lista resultante.
def filtro_menor_10(lista):
    lista_filtro = []
    for item in lista:
        if len(item) < 10:
            lista_filtro.append(item)
    # lista_filtro.sort()
    return sorted(lista_filtro)
lista_tamanho = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
lista_filtro = filtro_menor_10(lista_tamanho)
print(lista_filtro)

#lista_simplificada(v2)
def filtro_simplificadinho_10(lista):
    return[(item) for item in lista if len(item) < 10]



# Questão 04: Dada uma lista onde cada elemento corresponde a uma outra lista, faça
# um filtro para obter uma lista onde cada lista interna seja homogênea de números
# inteiros. Retorna a lista resultante.
def filtro_lista_inteiros(lista):
    lista_filtro = []
    for item in lista:
        if all(isinstance(x,int) for x in item):
            lista_filtro.append(item)
    return lista_filtro
lista_com_outralista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
lista_filtro = filtro_lista_inteiros(lista_com_outralista)
print(lista_filtro)




# Questão 05: Dada uma lista de string e uma lista de números inteiros, faça um filtro
# para obter uma lista de string onde o tamanho do elemento é menor ou igual ao valor
# do número inteiro de índice correspondente. Retorna a lista resultante.
def filtro_tamanho(lista_string,lista_inteiros):
    lista_filtro = []
    for item in range(len(lista_string)):
        if len(lista_string[item]) <= lista_inteiros[item]:
            lista_filtro.append(lista_string[item])
    return lista_filtro 

# Questão 06: Dada uma lista onde cada elemento corresponde a uma lista de números
# inteiros, faça um filtro para obter uma lista de listas onde a soma dos elementos da
# lista de uma determinada posição é maior que a soma dos elementos da lista da
# próxima posição. Retorna a lista resultante.
def filtro_soma(lista):
    lista_filtro = []
    for item in range(len(lista)-1):
        if sum(lista[item]) > sum(lista[item+1]):
            lista_filtro.append(lista[item])
    return lista_filtro


# Questão 07: Dada três lista de números inteiros, faça uma redução para encontrar o
# menor número resultante da soma dos elementos de índices correspondentes. Retorne
# o valor encontrado.
def reducao(lista_1,lista_2,lista_3):
    lista_reducao = []
    for item in range(len(lista_1)):
        lista_reducao.append(lista_1[item]+lista_2[item]+lista_3[item])
    return min(lista_reducao)


# Questão 08: Dada uma lista de string, faça uma redução para determinar o tamanho da
# maior string. Retorne o valor encontrado e o índice correspondente na lista. Se mais de
# uma string possuir o maior tamanho, retorne o menor índice.
def reducao_tamanho(lista):
    lista_reducao = []
    for item in lista:
        lista_reducao.append(len(item))
    return max(lista_reducao),lista_reducao.index(max(lista_reducao))


# Questão 09: Dada uma lista de números reais, faça uma redução que implique na soma
# dos elementos. O elemento da posição i só pode ser somado se ele for maior que o
# elemento da posição i+1. Retorne o valor encontrado.
def reducao_soma(lista):
    lista_reducao = []
    for item in range(len(lista)-1):
        if lista[item] > lista[item+1]:
            lista_reducao.append(lista[item])
    return sum(lista_reducao)


# Questão 10: Dada uma lista de string, faça uma redução que resulte em uma string
# concatenando todos os elementos separados por vírgula e espaço em branco. Retorne
# o valor encontrado.
def reducao_concatenar(lista):
    lista_reducao = ""
    for item in lista:
        lista_reducao += item + ", "
    return lista_reducao[:-2]


# Questão 11: Dada uma lista de números inteiros, faça uma redução para retornar o
# índice do maior primo da lista. Caso não exista, retorne -1.
def reducao_primo(lista):
    lista_reducao = []
    for item in lista:
        for i in range(2,item):
            if item % i == 0:
                item += 1
        lista_reducao.append(item)
    return lista_reducao.index(max(lista_reducao))


# Questão 12: Dada uma lista de números reais, faça uma redução para calcular o desvio
# padrão. Retorne o valor encontrado.
def reducao_desvio(lista):
    media = sum(lista)/len(lista)
    lista_reducao = []
    for item in lista:
        lista_reducao.append((item-media)**2)
    return (sum(lista_reducao)/len(lista_reducao))**(1/2)


# Questão 13: Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
# função que faça uma busca linear do elemento e retorne quantas comparações foram
# necessárias, bem como true ou false para informar se a busca foi realizada com sucesso
# ou não.
def busca_linear(lista,numero):
    for item in lista:
        if item == numero:
            return True,lista.index(item)
    return False,lista.index(item)


# Questão 14: Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
# função que ordene a lista e faça uma busca linear do elemento e retorne quantas
# comparações foram necessárias, bem como true ou false para informar se a busca foi
# realizada com sucesso ou não
def busca_linear_ordenada(lista,numero):
    lista.sort()
    for item in lista:
        if item == numero:
            return True,lista.index(item)
    return False,lista.index(item)


# Questão 15: Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
# função que ordene a lista e faça uma busca binária do elemento e retorne quantas
# comparações foram necessárias, bem como true ou false para informar se a busca foi
# realizada com sucesso ou não
def busca_binaria(lista,numero):
    lista.sort()
    inicio = 0
    fim = len(lista)-1
    while inicio <= fim:
        meio = (inicio+fim)//2
        if numero == lista[meio]:
            return True,lista.index(numero)
        elif numero < lista[meio]:
            fim = meio-1
        else:
            inicio = meio+1
    return False,lista.index(numero)



# lista = [9,-5,1,4,18]
# #questao 2 feita pelo hidaka
# def eh_primo(valor):
#     if valor <= 1:
#         return False
#     for divisor in range(2,valor):
#         if valor % divisor == 0:
#             return False
#     return True 
# def maior_primo_numero(valor):
#     valor =+ 1
#     while not eh_primo(valor):
#         valor =+ 1
#     return valor
# def construir_lista_primo(valor):
#     return[maior_primo_numero(item) for item in lista]


# lista_primaa = construir_lista_primo(lista)
# print(lista_primaa)

# def filtro_menor_10(lista):
#     lista_filtro = []
#     for item in lista:
#         if len(item) < 10:
#             lista_filtro.append(item)
#     # lista_filtro.sort()
#     return sorted(lista_filtro)
# lista_tamanho = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
# lista_filtro = filtro_menor_10(lista_tamanho)
# print(lista_filtro)


# Samarone trabalha em uma empresa chamada Sociedade Brasileira dos
# Caramelos (SBC). Recentemente, devido ao elevado desperdício de
# embalagens, Samarone foi designado para inspecionar as embalagens dos
# caramelos produzidas pela SBC. Samarone recebe diariamente lotes de
# embalagens e deve verificar quantas embalagens estão fora dos padrões
# estipulados pela SBC. Para facilitar a vida do Samarone, você foi contratado
# para desenvolver um programa de computador que, dada uma lista de
# embalagens, informe quantas estão fora dos padrões estipulados pela SBC.
# Cada item da lista possui um número não negativo que diz respeito ao tamanho
# da embalagem em centímetros. Sabe-se que as embalagens menores que sete
# centímetros não são aceitas pela SBC.

def verificação(lista):
    embalagens_fora_do_padrão = 0
    for embalagens in lista:
        if embalagens < 7:
            return embalagens_fora_do_padrão + 1

entrada = [1,2,3,4,5,6,7,8,20,1,2,3]
entrada_filtrada = verificação(entrada)
print(entrada_filtrada)