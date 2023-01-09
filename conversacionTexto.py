numero = int(input("Proporciona un valor 1 y 3: "))
if numero == 1:
    numeroTexto = 'numero uno'
elif numero == 2:
    numeroTexto = 'numero dos'
elif numero == 3:
    numeroTexto = 'numero tres'
else:
    numeroTexto = 'numero no reconocido'
print(f'Numero proporcionado: {numero}: {numeroTexto}')