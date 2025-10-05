import csv  # Importa o módulo csv para manipulação de arquivos CSV

# Solicita ao usuário que digite seu nome, idade e salário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
salario = input("Digite seu salário: ")

# Abre (ou cria) o arquivo CSV em modo de adição ('a')
with open('novo_arquivo.csv', mode='a', newline='') as arquivo:
    escritor = csv.writer(arquivo)  # Cria um objeto para escrever no arquivo CSV
    escritor.writerow(['Nome', 'Idade', 'Salário'])  # Escreve o cabeçalho no arquivo
    escritor.writerow([nome, idade, salario])  # Escreve os dados informados pelo usuário

    # Exibe mensagem de sucesso ao criar o arquivo
    print('arquivo em excel criado com sucesso!')





