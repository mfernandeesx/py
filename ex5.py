# ex 1
# Solicita ao usuário um número para verificar se é positivo, negativo ou zero
print("Olá! Informe um número para saber se é positivo, negativo ou zero.")
numero = float(input("Digite um número: "))

# Função para verificar se o número é positivo, negativo ou zero
def verificar_numero(numero):
    if numero > 0:
        return "Positivo"  # Retorna "Positivo" se o número for maior que zero
    elif numero < 0:
        return "Negativo"  # Retorna "Negativo" se o número for menor que zero
    else:
        return "Zero"  # Retorna "Zero" se o número for igual a zero

# Chama a função e armazena o resultado
resultado = verificar_numero(numero)
# Exibe o resultado ao usuário
print(f"O número é {resultado}.")
print("Fim do programa.")  # Indica o fim do programa



    