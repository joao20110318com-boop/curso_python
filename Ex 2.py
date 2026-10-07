def tabuada(numero):
    for i in range(1,11):
        print(numero,"x",i,"=",numero * i)


numero = int(input("digite um número:"))
tabuada(numero)