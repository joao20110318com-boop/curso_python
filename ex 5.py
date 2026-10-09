
def dsa_calcula_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc


# Programa interativo
print("=== CÁLCULO DO IMC ===")

peso = float(input("Digite seu peso em kg: ").replace(",", "."))
altura = float(input("Digite sua altura em metros: ").replace(",", "."))

if peso > 0 and altura > 0:
    imc = dsa_calcula_imc(peso, altura)
    print(f"Seu IMC é: {imc:.2f}")
else:
    print("Erro: digite valores maiores que zero.")
