edad = int(input("Escrive tu edad: "))
mensaje = None
if 0 <= edad < 10:
    mensaje = "La infancia es increible...."
elif 10 <= edad < 20:
    mensaje = "Muchos cambios , muchos estudios----"
elif 20 <= edad < 30:
    mensaje = "amor y comienza el trabajo...."
else:
    mensaje = "Etapa vida No recopnocida..."
print(f"tu edad: {edad},{mensaje}")
