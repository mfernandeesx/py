# Solicita o nome do usuário
nome = input("qual é o seu nome?")
# Loop para garantir que a idade seja um número válido e não negativo
while True:
    try:
        idade = int(input("qual é a sua idade?"))
        if idade >= 0:
            break
        else:
            print("por favor insira uma idade válida")
    except ValueError:
        print("por favor, insira um número válido")
# Verifica se o usuário é menor de idade
if idade < 18:
    print("acesso negado")
else:
    print("acesso permitido")
# Solicita o número de viagens no tempo que o usuário deseja fazer
viagens = int(input("quantas vezes você deseja viajar no tempo?"))
registro_viagens = []
# Loop para registrar cada viagem no tempo
for i in range(1, viagens + 1):
    ano = input("digite o ano da viagem, {}: ".format(i))
    direcao = input("será para o 'passado' ou 'futuro'? ").strip()
    registro_viagens.append((ano, direcao))
# Lista para armazenar eventos históricos
eventos_historicos = []
# Loop para exibir o menu de opções e executar as ações correspondentes
while True:
    print("\nmenu de opções:")
    print("1-registrar evento histórico")
    print("2-mostrar lista de eventos")
    print("0-sair")
    opcao = input("escolha uma opcao: ")
    # Registra um novo evento histórico
    if opcao == "1":
        evento = input("descreva o evento histórico: ")
        eventos_historicos.append(evento)
        print("evento registrado com sucesso")
    # Mostra a lista de eventos históricos registrados
    elif opcao == "2":
        if eventos_historicos:
            print("\nlista de eventos históricos:")
            for idx, evento in enumerate(eventos_historicos, start=1):
                print(f"{idx}. {evento}")
        else:
            print("nenhum evento registrado").end
    # Sai do programa
    elif opcao == "0":
        print("saindo do programa")
        break
    # Opção inválida
    else:
        print("opção inválida, tente novamente").end