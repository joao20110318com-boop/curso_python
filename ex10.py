
import random

numero_secreto = random.randint(1, 20)
tentativas = 5

print("=" * 35)
print("   JOGO DE ADIVINHAÇÃO")
print("=" * 35)
print("O computador escolheu um número de 1 a 20.")
print("Você tem 5 tentativas para acertar!\n")

for tentativa in range(1, tentativas + 1):
    try:
        palpite = int(input(
            f"Tentativa {tentativa}/{tentativas} - "
            "Digite seu palpite: "
        ))
    except ValueError:
        print("Digite um número inteiro válido!")
        continue

    if palpite < 1 or palpite > 20:
        print("Escolha um número entre 1 e 20.")
        continue

    if palpite == numero_secreto:
        print("\nParabéns! Você acertou!")
        print(f"O número secreto era {numero_secreto}.")
        print(f"Você acertou na tentativa {tentativa}!")
        break

    elif palpite < numero_secreto:
        print("Muito baixo! Tente um número maior.\n")

    else:
        print("Muito alto! Tente um número menor.\n")

else:
    print("\nSuas tentativas acabaram!")
    print(f"O número secreto era {numero_secreto}.")

print("\nFim do jogo!")
