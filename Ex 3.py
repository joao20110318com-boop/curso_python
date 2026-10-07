def alunos_acima_da_media():
    alunos = {}

    quantidade = int(input("Quantos alunos serão cadastrados? "))

    for i in range(quantidade):
        nome = input(f"\nDigite o nome do aluno {i + 1}: ")
        nota = float(input(f"Digite a nota de {nome}: "))
        alunos[nome] = nota

    media = sum(alunos.values()) / len(alunos)

    print(f"\nMédia da turma: {media:.2f}")
    print("Alunos acima da média:")

    for nome, nota in alunos.items():
        if nota > media:
            print(nome)


alunos_acima_da_media()