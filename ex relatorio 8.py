class aluno:
    def __init__(self, nome, idade, turma):
        self.nome = nome
        self.idade = idade
        self.turma = turma

    def apresentar(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Turma: {self.turma}')

    def fazer_prova(self):
        print(f'{self.nome} está fazendo a prova.')

aluno1 = aluno('João', 20, '3A')
aluno2 = aluno('Maria', 22, '3B')

aluno1.apresentar()
aluno1.fazer_prova()
aluno2.fazer_prova()


