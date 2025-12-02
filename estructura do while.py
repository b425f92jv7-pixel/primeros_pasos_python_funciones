#*********zona funcional********

def capturar_datos():
    print("Digita la letra A para actualizar sistemas")
    print("Digita la letra E para eliminar catalogo")
    print("Digita la letra C para crear productos")
    print("Digite la letra S para salir del programa")
    
    letra=input("seleciona su opcion: ")
    return letra.upper()

def analizar_datos (opcion):
    if opcion == "A":
        return "usted eligio actualizar sistema"
    elif opcion == "E":
        return "usted eligio eliminar catalogo"
    elif opcion == "C":
        return "usted eligio crear productos"
    elif opcion == "S":
        return "S"
    else:
        return "la informacion no es valida, ingrese su opcion de nuevo"
    
def mostrar_datos(mensaje):
    print(mensaje)
    
    
#*********codigo principal**************
while True:
    opcion=capturar_datos()
    mensaje =analizar_datos(opcion)
    
    if mensaje == "S":
       print("finalizo el programa con exito")
       break
    
    mostrar_datos(mensaje)
    print("el do-while a finalizado")
    