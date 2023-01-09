def main():
    numero = int(input("Digame cuantas palabnras tiene la lista: "))

    if numero < 1:
        print("Imposible")
    else:
        lista = []
        for i in range(numero):
            palabra = input(f"Digame la palabra{1 + 1}: ")
            lista += [palabra]
        print(f"La lista creada es: {lista}")

        buscar = input("Susitutir la palabra: ")
        sustituir = input("Por la palabra: ")
        for i in range(len(lista)):
            if lista[1] == buscar:
                lista[1] = sustituir
        print(f"La lista es ahora: {lista}")


if __name__ == '__main__':
    main()