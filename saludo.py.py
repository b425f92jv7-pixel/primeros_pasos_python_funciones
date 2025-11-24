#********zona de funciones*******
#palabra_clave + nombre_funcion(verbo) + parametros(adjetivos)
def capturar_nombre():
    nombre_usuario = input ("escriba el nombre del cliente: ")
    return nombre_usuario

def capturar_rol():
    rol_usuario = input ("escriba su rol: ")
    return rol_usuario

def capturar_hora() :
    hora = int(input("escria la hora: ")) 
    if hora > 0  and hora < 12:
        mensaje_hora = ("buenos dias ")
    elif hora  >= 12 and hora < 18 :
         mensaje_hora = ("buenas tardes ") 
    elif hora  >= 18 and hora < 24 :
         mensaje_hora = ("buenas noches ") 
    else :
        print ("hora incorrecta")
    return mensaje_hora
          
          
def hacer_saludo(nombre_usuario, rol_usuario, dato_hora ):
    mensaje = "hola " + " " + str(mensaje_hora) + nombre_usuario + " rol: " + rol_usuario 
    return mensaje 

def imprimir_menaje(mensaje):
    print (mensaje) 
    
#********zona de codigo prrincipal *******
dato_nombre = capturar_nombre() 
dato_rol = capturar_rol()
mensaje_hora = capturar_hora()
dato_mensaje = hacer_saludo(dato_nombre, dato_rol, mensaje_hora)
imprimir_menaje(dato_mensaje)
