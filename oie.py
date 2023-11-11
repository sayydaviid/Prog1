
#Hidaka fez em aula
def validar_nascimento(data):
    try:
        # Verificar se a data é composta apenas por dígitos
        if not data.isdigit():
            raise ValueError("Nascimento inválido: A data deve conter apenas dígitos.")

        # Converter a data para inteiro
        ano_nascimento = int(data)

        # Verificar se o ano está dentro de um intervalo razoável
        if not (1900 <= ano_nascimento <= 2023):
            raise ValueError("Nascimento inválido: Ano fora do intervalo válido.")

    except ValueError as e:
        print(e)
    else:
        print("Nascimento OK")

# Exemplo de uso
data_nascimento = input("Digite o ano de nascimento: ")

validar_nascimento(data_nascimento)
