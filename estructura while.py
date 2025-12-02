#*********zona de funciones***********

def tomar_numero():
    numero= int(input("dijite un numero: "))
    return numero

def identificar_numero(num):
    if num%2==0:
        return "El numero es par  "
    else:
        return "El numero es impar "

def enviar_mensaje(numero, num):
    mensaje= "el numero" + str(numero) + "es " + (num)
    return mensaje

def imprimir_mensaje(mensaje):
    print(mensaje)
    
#************codigo principal**********
numero=1;
while numero!=0:
     dato_numero= tomar_numero()
     tipo_numero= identificar_numero(dato_numero)
     dato_mensaje=enviar_mensaje(dato_numero, tipo_numero)
     imprimir_mensaje(dato_mensaje)
     print("finalizo el programa ")
