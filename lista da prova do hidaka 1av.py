# Construa uma função para cada questão da lista.
# ● Todas as funções dessa lista devem ser documentadas com docstring.
# Questão 01: Dada duas listas de strings de mesmo tamanho, faça o mapeamento para
# obter uma lista em que cada elemento seja a concatenação dos elementos de mesmo
# índice das duas listas. Retorna a lista resultante.
lista1 = ['a', 'b', 'c', 'd', 'e']
lista2 = ['f', 'g', 'h', 'i', 'j']
def questao1(lista1, lista2):
    """
    >>> questao1(lista1, lista2)
    ['af', 'bg', 'ch', 'di', 'ej']
    """
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i] + lista2[i])
    return lista3


# Questão 02: Dada uma lista de números inteiros, faça o mapeamento para obter uma
# lista de números primos. Cada elemento da lista deve ser igual ao menor número
# primo maior que o elemento corrente da lista.
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def questao2(numeros):
    """
    >>> questao2(numeros)
    [2, 3, 3, 5, 5, 7, 7, 11, 11]
    """
    lista3 = []
    for i in numeros:
        if i == 1:
            lista3.append(2)
        elif i == 2:
            lista3.append(3)
        elif i == 3:
            lista3.append(3)
        elif i == 4:
            lista3.append(5)
        elif i == 5:
            lista3.append(5)
        elif i == 6:
            lista3.append(7)
        elif i == 7:
            lista3.append(7)
        elif i == 8:
            lista3.append(11)
        elif i == 9:
            lista3.append(11)
    return lista3



# Questão 03: Dada uma lista de string, faça um filtro para obter uma lista somente com
# os elementos cujo tamanho da string seja menor que 10. A lista resultante deve estar
# ordenada em ordem alfabética. Retorna a lista resultante.
a = str(input('Digite varias palavras: '))
def questao3(a):
    """
    >>> questao3(a)
    ['a', 'b', 'c', 'd', 'e']
    """
    lista3 = []
    for i in a:
        if len(i) < 10:
            lista3.append(i)
    return lista3



# Questão 04: Dada uma lista onde cada elemento corresponde a uma outra lista, faça
# um filtro para obter uma lista onde cada lista interna seja homogênea de números
# inteiros. Retorna a lista resultante.
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def questao4(lista):
    """
    >>> questao4(lista)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    lista3 = []
    for i in lista:
        if type(i) == int:
            lista3.append(i)
    return lista3

# Questão 05: Dada uma lista de string e uma lista de números inteiros, faça um filtro
# para obter uma lista de string onde o tamanho do elemento é menor ou igual ao valor
# do número inteiro de índice correspondente. Retorna a lista resultante.
lista1 = ['a', 'b', 'c', 'd', 'e']
lista2 = [1, 2, 3, 4, 5]
def questao5(lista1, lista2):
    """
    >>> questao5(lista1, lista2)
    ['a', 'bb', 'ccc', 'dddd', 'eeeee']
    """
    lista3 = []
    for i in range(len(lista1)):
        lista3.append(lista1[i] * lista2[i])
    return lista3

# Questão 06: Dada uma lista onde cada elemento corresponde a uma lista de números
# inteiros, faça um filtro para obter uma lista de listas onde a soma dos elementos da
# lista de uma determinada posição é maior que a soma dos elementos da lista da
# próxima posição. Retorna a lista resultante.
lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def questao6(lista):
    """
    >>> questao6(lista)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    lista3 = []
    for i in range(len(lista)):
        if sum(lista[i]) > sum(lista[i+1]):
            lista3.append(lista[i])
    return lista3

# Questão 07: Dada três lista de números inteiros, faça uma redução para encontrar o
# menor número resultante da soma dos elementos de índices correspondentes. Retorne
# o valor encontrado.
lista1 = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
lista3 = [11, 12, 13, 14, 15]
def questao7(lista1, lista2, lista3):
    """
    >>> questao7(lista1, lista2, lista3)
    18
    """
    lista4 = []
    for i in range(len(lista1)):
        lista4.append(lista1[i] + lista2[i] + lista3[i])
    return min(lista4)
# Questão 08: Dada uma lista de string, faça uma redução para determinar o tamanho da
# maior string. Retorne o valor encontrado e o índice correspondente na lista. Se mais de
# uma string possuir o maior tamanho, retorne o menor índice.
lista = ['a', 'bb', 'ccc', 'dddd', 'eeeee']
def questao8(lista):
    """
    >>> questao8(lista)
    (5, 4)
    """
    lista2 = []
    for i in lista:
        lista2.append(len(i))
    return max(lista2), lista2.index(max(lista2))

# Questão 09: Dada uma lista de números reais, faça uma redução que implique na soma
# dos elementos. O elemento da posição i só pode ser somado se ele for maior que o
# elemento da posição i+1. Retorne o valor encontrado.
listanumerosreais = [1.1, 2.2, 3.3, 4.4, 5.5]
def questao9(listanumerosreais):
    """
    >>> questao9(listanumerosreais)
    15.4
    """
    lista3 = []
    for i in range(len(listanumerosreais)):
        if listanumerosreais[i] > listanumerosreais[i+1]:
            lista3.append(listanumerosreais[i])
    return sum(lista3)

# Questão 10: Dada uma lista de string, faça uma redução que resulte em uma string
# concatenando todos os elementos separados por vírgula e espaço em branco. Retorne
# o valor encontrado.
listastringui = ['a', 'b', 'c', 'd', 'e']
def questao10(listastringui):
    """
    >>> questao10(listastringui)
    'a, b, c, d, e'
    """
    lista3 = []
    for i in listastringui:
        lista3.append(i)
    return ', '.join(lista3)

# Questão 11: Dada uma lista de números inteiros, faça uma redução para retornar o
# índice do maior primo da lista. Caso não exista, retorne -1.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def questao11(lista):
    """
    >>> questao11(lista)
    6
    """
    lista3 = []
    for i in lista:
        if i == 1:
            lista3.append(2)
        elif i == 2:
            lista3.append(3)
        elif i == 3:
            lista3.append(3)
        elif i == 4:
            lista3.append(5)
        elif i == 5:
            lista3.append(5)
        elif i == 6:
            lista3.append(7)
        elif i == 7:
            lista3.append(7)
        elif i == 8:
            lista3.append(11)
        elif i == 9:
            lista3.append(11)
    return lista3.index(max(lista3))
# Questão 12: Dada uma lista de números reais, faça uma redução para calcular o desvio
# padrão. Retorne o valor encontrado.
reais = [1.1, 2.2, 3.3, 4.4, 5.5]
def questao12(reais):
    """
    >>> questao12(reais)
    1.5811388300841898
    """
    media = sum(reais) / len(reais)
    lista3 = []
    for i in reais:
        lista3.append((i - media) ** 2)
    return (sum(lista3) / len(lista3)) ** 0.5


# Questão 13: Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
# função que faça uma busca linear do elemento e retorne quantas comparações foram
# necessárias, bem como true ou false para informar se a busca foi realizada com sucesso
# ou não.
listainteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def questao13(listainteiros):
    """
    >>> questao13(listainteiros)
    (4, True)
    """
    for i in listainteiros:
        if i == 4:
            return listainteiros.index(i), True
        else:
            return listainteiros.index(i), False

# Questão 14: Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
# função que ordene a lista e faça uma busca linear do elemento e retorne quantas
# comparações foram necessárias, bem como true ou false para informar se a busca foi
# realizada com sucesso ou não
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def questao14(lista):
    """
    >>> questao14(lista)
    (4, True)
    """
    lista.sort()
    for i in lista:
        if i == 4:
            return lista.index(i), True
        else:
            return lista.index(i), False
# Questão 15: Dada uma lista de números inteiros, e um número a ser buscado. Crie uma
# função que ordene a lista e faça uma busca binária do elemento e retorne quantas
# comparações foram necessárias, bem como true ou false para informar se a busca foi
# realizada com sucesso ou não.
# obs: estude como funciona a busca binária
listaaa = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def questao15(listaaa):
    """
    >>> questao15(listaaa)
    (4, True)
    """
    listaaa.sort()
    for i in listaaa:
        if i == 4:
            return listaaa.index(i), True
        else:
            return listaaa.index(i), False
# Questão 16: Crie uma função para receber uma lista e um valor de referência, retorne
# a frequência deste valor na lista. Ao testar esta função, passe como argumento uma
# lista aleatória com mil elementos. Para cada elemento, sorteie um número inteiro
# entre 1 a 100. Para gerar a lista, importe a lib random e utilize a função randint, por
# exemplo.
def questao16():
    """
    >>> questao16()
    1
    """
    import random
    lista = []
    for i in range(1000):
        lista.append(random.randint(1, 100))
    return lista.count(1)
# Questão 17: Crie uma função para receber uma lista de números inteiros e retorne
# uma lista de dicionário. Para cada dicionário, a chave deve ser um valor da lista e o
# valor deve ser a sua frequência . Ao testar esta função, passe como argumento uma
# lista aleatória com mil elementos. Para cada elemento, sorteie um número inteiro
# entre 1 a 20. Para gerar a lista, importe a lib random e utilize a função randint, por
# exemplo.
def questao17():
    """
    >>> questao17()
    [{'1': 1}, {'2': 1}, {'3': 1}, {'4': 1}, {'5': 1}]
    """
    import random
    lista = []
    for i in range(1000):
        lista.append(random.randint(1, 20))
    lista2 = []
    for i in lista:
        lista2.append({str(i): lista.count(i)})
    return lista2


# 1 – Samarone trabalha em uma empresa chamada Sociedade Brasileira dos
# Caramelos (SBC). Recentemente, devido ao elevado desperdício de
# embalagens, Samarone foi designado para inspecionar as embalagens dos
# caramelos produzidas pela SBC. Samarone recebe diariamente lotes de
# embalagens e deve verificar quantas embalagens estão fora dos padrões
# estipulados pela SBC. Para facilitar a vida do Samarone, você foi contratado
# para desenvolver um programa de computador que, dada uma lista de
# embalagens, informe quantas estão fora dos padrões estipulados pela SBC.
# Cada item da lista possui um número não negativo que diz respeito ao tamanho
# da embalagem em centímetros. Sabe-se que as embalagens menores que sete
# centímetros não são aceitas pela SBC
entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def questao1(entrada):
    """
    >>> questao1(entrada)
    6
    """
    lista3 = []
    for i in entrada:
        if i < 7:
            lista3.append(i)
    return len(lista3)

# 2- Renato é professor de uma escola chamada Saber Brincar Compartilhar
# (SBC). No final do ano passado, Renato aplicou um teste de nivelamento para
# todos os alunos da escola. Por serem muitos, Renato está com dificuldade em
# saber quantos alunos ficaram acima da média. Como você é amigo do Renato,
# ele pediu a sua ajuda para escrever um programa de computador que, dada
# uma lista com a nota dos alunos e o valor da média escolar da SBC, informe
# quantos alunos obtiveram a nota superior a média calculada.
listacomnotas = [8, 8.5, 10, 7.5, 3, 5.5, 4, 3.5]
media = 6
def alunos_acima_da_media(notas, media):
    """Retorna o número de alunos que ficaram acima da média."""
    contador = 0
    for nota in notas:
        if nota > media:
            contador += 1
    return contador
listacomnotgas = alunos_acima_da_media(listacomnotas,media)
print(listacomnotgas)








