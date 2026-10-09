
pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Carlos", "idade": 18},
    {"nome": "Maria", "idade": 32},
    {"nome": "João", "idade": 21}
]

# Ordenar da pessoa mais nova para a mais velha
pessoas_ordenadas = sorted(pessoas, key=lambda pessoa: pessoa["idade"])

# Exibir o resultado
print("Pessoas ordenadas por idade:")
for pessoa in pessoas_ordenadas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}")
