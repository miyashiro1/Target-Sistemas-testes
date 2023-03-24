# Pedimos o input do usuário, realizando um check para garantir que será uma string
while True:
    try:
        string_usuario = input("Digite uma string: ")
        break
    except ValueError:
        print("Erro! Por favor, apenas strings.")
str = ''

# Neste loop realizamos a inversão da string
for i in string_usuario:
    str = i+str

print(f'A string invertida é: {str}')