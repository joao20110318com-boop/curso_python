numeros = []

quantidade = int(input("Quantos números você quer digitar? "))

for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

quadrados = [numero ** 2 for numero in numeros if numero % 2 == 0]

print("Números digitados:", numeros)
print("Quadrados dos números pares:", quadrados)