# Exemplo prático de Programação Orientada a Objetos (POO) em Python

class Personagem:
    """
    Classe Personagem representa um personagem com nome e vida, utilizando encapsulamento para proteger seus atributos.
    Atributos Privados:
        __nome (str): Nome do personagem.
        __vida (int): Quantidade de vida do personagem.
    Métodos:
        __init__(nome, vida):
            Inicializa um novo personagem com nome e vida especificados.
        atacar():
            Exibe uma mensagem indicando que o personagem atacou.
        get_vida():
            Retorna o valor atual da vida do personagem.
        set_vida(nova_vida):
            Atualiza o valor da vida do personagem, garantindo que não seja negativo.
    """
    def __init__(self, nome, vida):
        # Atributos privados (encapsulamento)
        self.__nome = nome
        self.__vida = vida

    def atacar(self):
        print(f"{self.__nome} atacou!")

    # Método getter para vida
    def get_vida(self):
        return self.__vida

    # Método setter para vida
    def set_vida(self, nova_vida):
        if nova_vida >= 0:
            self.__vida = nova_vida
        else:
            print("A vida não pode ser negativa.")

# Criando instâncias da classe Personagem
heroi = Personagem("Arthur", 100)
vilao = Personagem("Morgana", 80)

# Usando métodos
heroi.atacar()
vilao.atacar()

print(f"Vida do herói: {heroi.get_vida()}")
print(f"Vida do vilão: {vilao.get_vida()}")

# Modificando a vida do herói
heroi.set_vida(90)
print(f"Vida do herói após dano: {heroi.get_vida()}")

# Tentando definir vida negativa (não permitido)
vilao.set_vida(-10)
print(f"Vida do vilão após tentativa inválida: {vilao.get_vida()}")