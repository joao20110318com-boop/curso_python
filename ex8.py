
def dsa_filtrar_emails(emails, dominio_desejado="gmail.com"):
    return [
        email for email in emails
        if email.lower().endswith("@" + dominio_desejado.lower())
    ]


# Programa interativo
print("=== FILTRO DE E-MAILS ===")

emails = []

while True:
    email = input("Digite um e-mail ou 'fim' para terminar: ")

    if email.lower() == "fim":
        break

    emails.append(email.strip())

dominio = input(
    "Digite o domínio desejado (Enter para gmail.com): "
).strip()

if dominio == "":
    dominio = "gmail.com"

resultado = dsa_filtrar_emails(emails, dominio)

print("\n=== RESULTADO ===")
print("E-mails encontrados:")

for email in resultado:
    print(email)

print("Total encontrado:", len(resultado))

