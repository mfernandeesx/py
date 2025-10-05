print('olá competidor! digite idade >5 e <18 para saber sua categoria')

# Lista de nomes de exemplo
nomes = ["Ana", "Carlos", "Beatriz", "João", "Mariana"]

# Itera sobre cada nome na lista
for nome in nomes:
    # Solicita ao usuário que insira a idade e converte para um número inteiro
    idade = int(input(f"{nome}, qual é a sua idade? "))

    # Verifica se a idade é menor que 5
    if idade < 5:
        # Caso a idade seja menor que 5, exibe mensagem indicando que está abaixo da categoria mínima
        print(f"{nome}, idade abaixo da categoria mínima")

    # Verifica se a idade está entre 5 e 7 anos (inclusive)
    elif idade >= 5 and idade <= 7:
        # Caso a idade esteja nesse intervalo, exibe a categoria "infantil A"
        print(f"{nome}, sua categoria é infantil A")

    # Verifica se a idade está entre 8 e 10 anos (inclusive)
    elif idade >= 8 and idade <= 10:    
        # Caso a idade esteja nesse intervalo, exibe a categoria "infantil B"
        print(f"{nome}, sua categoria é infantil B")

    # Verifica se a idade está entre 11 e 13 anos (inclusive)
    elif idade >= 11 and idade <= 13:
        # Caso a idade esteja nesse intervalo, exibe a categoria "juvenil A"
        print(f"{nome}, sua categoria é juvenil A")

    # Verifica se a idade está entre 14 e 17 anos (inclusive)
    elif idade >= 14 and idade <= 17:
        # Caso a idade esteja nesse intervalo, exibe a categoria "juvenil B"
        print(f"{nome}, sua categoria é juvenil B")

    # Caso nenhuma das condições anteriores seja atendida (idade maior ou igual a 18)
    else: 
        # Exibe a categoria "senior"
        print(f"{nome}, sua categoria é senior")
        

    