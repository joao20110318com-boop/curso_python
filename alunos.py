alunos = []

def cadastrar():

    nome = input("Nome do aluno: ").strip()

    if nome == "":

        print("Nome não pode ficar vazio!")

        return

    nota1 = float(input("Nota 1: "))

    nota2 = float(input("Nota 2: "))

    alunos.append({

        "nome": nome,

        "nota1": nota1,

        "nota2": nota2

    })

    print("Aluno cadastrado!")


def buscar():

    nome = input("Nome para buscar: ").strip().lower()

    for aluno in alunos:

        if aluno["nome"].lower() == nome:

            print(aluno)

            return

    print("Aluno não encontrado!")


def atualizar():

    nome = input("Nome do aluno: ").strip().lower()

    for aluno in alunos:

        if aluno["nome"].lower() == nome:

            aluno["nome"] = input("Novo nome: ").strip()

            aluno["nota1"] = float(input("Nova nota 1: "))

            aluno["nota2"] = float(input("Nova nota 2: "))

            print("Cadastro atualizado!")

            return

    print("Aluno não encontrado!")


def excluir():

    nome = input("Nome do aluno: ").strip().lower()

    for aluno in alunos:

        if aluno["nome"].lower() == nome:

            confirmacao = input("Deseja excluir? (s/n): ").lower()

            if confirmacao == "s":

                alunos.remove(aluno)

                print("Aluno excluído!")

            return

    print("Aluno não encontrado!")


def ranking():

    ranking_alunos = sorted(

        alunos,

        key=lambda aluno: (aluno["nota1"] + aluno["nota2"]) / 2,

        reverse=True

    )

    for aluno in ranking_alunos:

        media = (aluno["nota1"] + aluno["nota2"]) / 2

        print(aluno["nome"], "- Média:", media)


def estatisticas():

    aprovados = 0

    reprovados = 0

    for aluno in alunos:

        media = (aluno["nota1"] + aluno["nota2"]) / 2

        if media >= 6:

            aprovados += 1

        else:

            reprovados += 1

    print("Aprovados:", aprovados)

    print("Reprovados:", reprovados)


while True:

    print("\n--- MENU ---")

    print("1 - Cadastrar")

    print("2 - Buscar")

    print("3 - Atualizar")

    print("4 - Ranking")

    print("5 - Excluir")

    print("6 - Estatísticas")

    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        cadastrar()

    elif opcao == "2":

        buscar()

    elif opcao == "3":

        atualizar()

    elif opcao == "4":

        ranking()

    elif opcao == "5":

        excluir()

    elif opcao == "6":

        estatisticas()

    elif opcao == "0":

        break

    else:

        print("Opção inválida!")