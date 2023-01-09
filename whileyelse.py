# var1 = 1
# while var1 < 5:
#     print(var1)
#     var1 +=1
# else:
#     print("Else", var1)

def main():
    print("Diga si para continuar")
    respuesta = input("¿Desea continuar el programa?: ")

    while respuesta == "si":
        respuesta = input("Desea continuar el programa? ")

    print("Hasta la vista, baby")

if __name__ == '__main__':
    main()