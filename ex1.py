def classificar_triangulo(a,b,c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

a = float(input("Digite o primeiro lado: "))

b = float(input("Digite o segundo lado: "))

c = float(input("Digite o terceiro lado: "))

resultado = classificar_triangulo(a, b, c)

print("O triângulo é:", resultado)