def exibir_menu():
    print('\n===menu cadastro===')
    print('1 - Cadastrar')
    print('2 - Listar cadastros')
    print('3 - Sair')

def adicionar_cadastro():
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    telefone = input('Digite seu telefone: ')

    with open('cadastro.txt', 'a') as arquivo:
        arquivo.write(f'{nome},{email},{telefone}\n')
    print('Cadastro adicionado com sucesso!')

def listar_cadastros():
    try:
        with open('cadastro.txt','r') as arquivo:
            cadastros = arquivo.readlines()
        print('\n===Lista de cadastros===')
        print('nome, email, telefone')
        for linha in cadastros:
            linha = linha.strip()
            print(linha)
    except FileNotFoundError:
        print('Nenhum cadastro encontrado.')

def main():
    while True:
        exibir_menu()
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            adicionar_cadastro()
        elif opcao == '2':
            listar_cadastros()
        elif opcao == '3':
            print('Saindo do programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')

if __name__ == '__main__':
    main()
    
            