
def dsa_contar_pares_impares(numeros):
    pares = 0
    impares = 0

    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return {
        "pares": pares,
        "impares": impares
    }


print("===== CONTADOR DE NÚMEROS =====")
numeros = []

while True:
    valor = input("Digite um número inteiro ou 'sair' para finalizar: ")

    if valor.lower() == "sair":
        break

    try:
        numeros.append(int(valor))
        print("Número adicionado!")
    except ValueError:
        print("Digite um número inteiro válido.")

resultado = dsa_contar_pares_impares(numeros)

print("\n===== RESULTADO FINAL =====")
print("Lista de números:", numeros)
print("Números pares:", resultado["pares"])
print("Números ímpares:", resultado["impares"])
print("Total de números:", len(numeros))
