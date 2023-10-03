# a funçao é definida por 3 parametros:
# entrada
# processamento
# saida

# sao 4 partes a definição de uma função
# def é a primeira
# o nome é a segunda
# os parametros são a terceira
# e a quarta é o começo do escopo :



def f2(a,b=0):
    return a+b

#esse numero dentro do pareteses escrito como =5 é chamado de nomeada
#a que esta do lado é posicional
#a posicional sempre tem que ficar a esquerda, e a nomeda a direita
x = f2(4,b=5)
print(x)



#função void é uma função sem retorno
def f22(a=2,*n,c):
    print(a)
    print(n)
    print(c)
f22(10,7,3,5,c=4)
# f22(a=3)


#a função print é igual o *n
print('c',2,4,'d',sep='-')
#sep serve pra mudar o tipo de formatação do print

print('a',2,sep='inzedamanga',end='.')
#como falado anteriormente sep é o espaço do print, cujo pode ser mudado
#end serve para formatar o fim da questão

def f23(a,b,c=4):
    return a,b+c
x = f23(2,3)
print(x)
print(type(x))

#o codigo nao é linear é quando usamos controle de fluxo 
#por exemplo if, else, elif, repetição, for, while