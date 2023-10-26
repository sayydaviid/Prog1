def validar_nascimento(data):
    try:
        if not data.isdigit():
            raise Exception("nascimento invalido")
        if 1900 > int(data) > 2023:
            raise Exception("nascimento invalido")
    except Exception as e:
        print(e)
    else:
        print("nascimenento ok")
#         try:
# for item in data:
#             if len(item) > 4:
#                 return("idade certa")
#     except:
#         print("Ano de nascimento inválido")

# a = int(input("Digite o ano que você nasceu: "))

# if validar_nascimento(a):
#     print("Idade certa")
# else:
#     print("Idade errada")