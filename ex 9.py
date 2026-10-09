
def dsa_transformar_frases(frases):
    resultado = list(map(
        lambda frase: frase.upper() + " PYTHON",
        frases
    ))
    return resultado


# Programa interativo
print("=" * 35)
print("   TRANSFORMADOR DE FRASES")
print("=" * 35)
print("Digite suas frases.")
print("Digite 'fim' para terminar.\n")

frases = []

while True:
    frase = input("Digite uma frase: ").strip()

    if frase.lower() == "fim":
        break

    if frase:
        frases.append(frase)
        print("Frase adicionada com sucesso!")
    else:
        print("A frase não pode estar vazia.")

# Transformar as frases
resultado = dsa_transformar_frases(frases)

print("\n=== FRASES TRANSFORMADAS ===")

if resultado:
    for i, frase in enumerate(resultado, start=1):
        print(f"{i}. {frase}")
else:
    print("Nenhuma frase foi digitada.")

print(f"\nTotal de frases: {len(resultado)}")
print("Programa finalizado!")
