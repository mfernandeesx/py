def avaliacao(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def main():
    print("Olá! Vamos avaliar as médias dos alunos.")
    notas = []
    quantidade_de_alunos = int(input("Quantos alunos você deseja avaliar? "))
    
    for i in range(quantidade_de_alunos):
        print(f"\nAluno {i + 1}:")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        resultado = avaliacao(nota1, nota2, nota3)
        notas.append(resultado)
        print(f"Resultado do aluno {i + 1}: {resultado}")
    
    print("\nResultados finais:")
    for i, resultado in enumerate(notas, start=1):
        print(f"Aluno {i}: {resultado}")

if __name__ == "__main__":
    main()