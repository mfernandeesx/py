# Define o saldo inicial da conta de João
saldo_joao = 1000

# Inicia um loop infinito para processar os saques de João
while True:
    try:
        # Solicita ao João o valor do saque
        valor_saque = float(input("João, digite o valor do saque: (ou 0 para sair): "))
        
        # Verifica se o valor do saque é 0 ou negativo para encerrar a operação
        if valor_saque == 0 or valor_saque < 0:
            print("Operação finalizada, João.")
            break
        # Verifica se o valor do saque é maior que o saldo disponível
        elif valor_saque > saldo_joao:
            print("Saldo insuficiente, João.")
        # Caso contrário, realiza o saque e atualiza o saldo
        else:
            saldo_joao -= valor_saque
            print(f"João, seu saldo atual é: {saldo_joao}")
    except ValueError:
        # Trata erros de entrada inválida (não numérica)
        print("Por favor, João, insira um valor numérico válido.")
    
    # Este bloco de código é redundante e será executado novamente após o loop
    valor_saque = float(input("João, digite o valor do saque: (ou 0 para sair): "))
    if valor_saque == 0 or valor_saque < 0:
        print("Operação finalizada, João.")
        break
    elif valor_saque > saldo_joao:
        print("Saldo insuficiente, João.")
    else:
        saldo_joao -= valor_saque
        print(f"João, seu saldo atual é: {saldo_joao}")
    
    
        