import re
def main():
    while True:
        op = menu()
        if op == '1':
            cadastrar()
        elif op == '2':
            listar
        else:
            break

def menu():
    return input('1 - cadastrar \n 2 - listar \n*- Sair')


def cadastrar():
    nome = input("Digite seu nome: ")
    telefone = input("Digite seu telefone")
    email = input("Digite seu email: ")
    with open("bd_cadastros.txt", 'a', encoding= "utf-8") as f:
        f.write(f'{nome}, {telefone},{email}')
        f.write("\n")
    
def listar():
    with open("bd_cadastros.txt", 'r', encoding="utf-8") as f:
        lista = [formatar(linha) for linha in f]
        print(*lista)


def formatar(linha):
    import re
    return re.sub(','',''\t', linha)

main()