def space():
    print("--------------------------------------------------------------------------------")

############### CONDICIONALES ###############
# == igual
# > mayor que
# < menor que
# >= mayor o igual
# <= menor o igual
# != distinto

a = 3

if a>3:
    print("Si, es mayor")
    print("Chau")
else:
    print("No, a no es mayor a 3")
if a==3:
    print("a es igual a 3")

nota = 72

if nota > 60:
    print("Pasasteeee!")
else:
    print("Hule ya:(")

# Ej. Crear una función que reciba como parametro una nota
# e imprima si pasaste o te aplazaste

def resultado(valor_nota):
    if valor_nota>60:
        print("Aprobado")
    else:
        print("Reprobado")

resultado(nota)

space()

if a > 5 and a < 10:
    print("a es mayor a 5 y menor a 10")
else:
    print("a no está en el rango 5-10")

if a > 5 or a < 10:
    print("a es mayor a 5 o menor a 10")
else:
    print("a no es mayor que 5 ni menor que 10")

space()

edad = 4

if edad > 18:
    print("Debería estar en la universidad")
elif edad > 13:
    print("Debería estar en secundaria")
elif edad > 6:
    print("Debería estar en primaria")
else:
    print("No está en edad escolar")

space()

# Ej. Crear función puntaje que reciba como parámetro una nota del 1 al 100
# e imprima qué nota sacaste
# nota < 60 ----> Aplazado
# nota < 70 ----> 2
# nota < 80 ----> 3
# nota < 90 ----> 4
# nota < 100 ----> 5

parcial1 = 55
parcial2 = 100
final = 100

Nota = int((((parcial1+parcial2)/2)*0.4) + (final*0.6))

def calif(valor):
    if valor>=0 and valor<=100:
        if valor<=60:
            return "Aplazado"
        elif valor<=70:
            return 2
        elif valor<=80:
            return 3
        elif valor<=90:
            return 4
        else:
            return 5
    else:
        print("Nota fuera de rango")

print(calif(Nota))

space()

# Imprimir elementos de dos listas diferentes con el mismo for
nombres=["Ale","José","Pepe"]
nota=[3,1,4]

if len(nombres)==len(nota): # Nos aseguramos de que haya la misma cantidad de nombres y notas
    for x in range(len(nombres)): # Range sería la longitud de la lista de nombres
        print(nombres[x], nota[x]) # El índice de las listas es la variable del for

space()

#nombre = input("Name please :")
#print("Hola", nombre)

#num1 = input("1st number: ")
#num2 = input("2nd number: ")
#print("El resultado es", int(num1)+int(num2))

# int() función que convierte a integer
# str() función que convierte a string

space()

# Ej. Pedir al usuario que ingrese tres números y multiplicarlos
# entre sí, imprimir el resultado

#print("Ingresar números para multiplicar")
#num1 = int(input("1st: "))
#num2 = int(input("2nd: "))
#num3 = int(input("3rd: "))

#print("El resultado de la multiplicación es:", num1*num2*num3)

space()

# Ej. Pedir al usuario un número del 1 al 100 y llamar a la
# función que retornaba la nota que creamos hace un rato

#print("Por favor, ingresa el puntaje alcanzado")
#puntaje = int(input("Tu puntaje: "))
#print("Tu nota final es:", calif(puntaje))

space()

# Función para saber si un año es bisiesto
# Un año bisiesto es divisible entre 4 y no entre 100
# % es el operador mod que me devuelve el resto de la división

#year = int(input("Año: ")) # Se ingresa un año por teclado

# Se pone la condición divisible entre 4 y no divisible entre 100
#if year%4==0 and year%100!=0:
#    print("Es bisisesto") 
#else:
#    print("No es bisieto")

space()

########## Bucle while == mientras ##########

# x=0
# while x != 5:
#     print("Hola, esto es un bucle while")
#     x = int(input("Ingresa un número: "))

space()

contador = 0

while contador < 10:
    print("Sigo en el bucle while")
    contador = contador + 1
    print("Se repitió", contador, "veces")

space()

# Ej. Usando while pedir al usuario 5 ingredientes para hacer una piza y
# agregar a una lista, al final imprimir la lista

# ingredientes = []
# print("Se requiere que ingrese los ingredientes para la pizza")
# while len(ingredientes)<5:
#     ing = input("Ingrediente: ")
#     ingredientes.append(ing)

space()

# print("La lista de ingredientes es")
# for i in ingredientes:
#     print("-",i)

# ing = []
# cont = 0
# print("Se requiere que ingrese los ingredientes para la pizza")
# while cont < 5:
#     ingr = input("Ingrediente: ")
#     ing.append(ingr)
#     cont = cont + 1

# print("La lista de ingredientes es",ing)

space()

# número_secreto = 7
# adivino = False

# while adivino==False:
#     apuesta = int(input("Adivina el número secreto del 1 al 10: "))

#     if apuesta==número_secreto:
#         print("Adivinaste")
#         adivino = 1
#     else:
#         print("Segui participando nde aruinado")

space()

# Ej. Crear un juego de adivinar el número como el de arriba y
# darle pistas al usuario si el número que ingresó es mayor o menor
# que el número que debe adivinar

# número_secreto = 56
# adivino = False

# while adivino==False:
#     apuesta = int(input("Adivina el número secreto del 1 al 100: "))

#     if apuesta==número_secreto:
#         print("Adivinaste")
#         adivino = 1
#     elif apuesta<número_secreto:
#         print("Prueba un número mayor")
#     elif apuesta>número_secreto:
#         print("Prueba un número menor")

# Ej. Crear un juego igual al anterior pero con un número aleatorio
# para el valor del número secreto
from random import randint

# número_secreto = randint(0,100)
# adivino = False

# while adivino==False:
#     apuesta = int(input("Adivina el número secreto del 1 al 100: "))

#     if apuesta==número_secreto:
#         print("Adivinaste")
#         adivino = 1
#     elif apuesta<número_secreto:
#             print("Prueba un número mayor")
#     elif apuesta>número_secreto:
#             print("Prueba un número menor")


space()

# Este juego cambia el valor del número secreto cada vez que el jugador
# no lo adivina

número_secreto = randint(0,100)
adivino = False

while adivino==False:
    apuesta = int(input("Adivina el número secreto del 1 al 100: "))

    if apuesta==número_secreto:
        print("Adivinaste")
        adivino = 1
    else:
        número_secreto = randint(0,100)
        if apuesta<número_secreto:
            print("Prueba un número mayor")
        elif apuesta>número_secreto:
            print("Prueba un número menor")