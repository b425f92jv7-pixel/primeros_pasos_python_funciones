# *************funcion for*************
def capturar_datos():
    numeros = []  

    for i in range(0, 10, 2):
        print("Digite el Numero " + str(i+1) + ": ")
        numero = int(input())
        numeros.append(numero)

    return numeros
def analizar_datos(lista):
    suma = 0
    for num in lista:
        suma += num
    return suma

def imprimir_mensaje(total):
    print("La sumatoria total es: " + str(total))


# ************* CODIGO CENTRAL MAIN *************
total_numeros = capturar_datos()     
mensaje = analizar_datos(total_numeros)  
imprimir = imprimir_mensaje(mensaje)        
