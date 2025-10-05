# ex 2
# Solicita ao usuário três números para determinar qual é o maior
print('Olá! Peça três números para saber qual é o maior.')
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Função para encontrar o maior número entre três valores
def encontrar_maior(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1  # Retorna num1 se for o maior ou igual aos outros
    elif num2 >= num1 and num2 >= num3:
        return num2  # Retorna num2 se for o maior ou igual aos outros
    else:
        return num3  # Retorna num3 se for o maior

# Chama a função e armazena o maior número
maior = encontrar_maior(num1, num2, num3)
# Exibe o maior número ao usuário
print(f"O maior número é {maior}.")
print("Fim do programa.")  # Indica o fim do programa

