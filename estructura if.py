#***** estructura if elif else*****
#***** zona de funciones *****

def capturar_numero ():
    numero = int(input("escriba un numero: "))
    
    if numero > 0:
        print(" el numero es positivo. ")
    
    elif numero==0:
        print(" el numero es neutro. ")
        
    else: 
        print(" el numero es negativo. ")
    return numero
        
def hacer_mensaje (numero): 
    mensaje = str(numero)
    return

def imprimir_mensaje(mensaje):
    print (mensaje)

#********zona de codigo principal******

numero = capturar_numero()
dato_mensaje = hacer_mensaje(numero)
imprimir_mensaje(dato_mensaje) 