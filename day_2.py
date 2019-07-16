def space():
    print("--------------------------------------------------------------------------------")

# Tipo de dato String/cadena de texto/str
"This is a String"
# Tipo de dato Integer/entero/int
105
# Listas
list0 = [] # Lista vacía
list1 = ["José", 22] # Lista de 2 elementos
# Variables
name = "José"
age = 22
age_bad_format = "20+2"
sample_list = ["Hola", name, 99]
# Acceder a un elemento de la lista
print(sample_list[0], age, sample_list[2])
# Acciones/operaciones sobre listas
sample_list.append("Nothing") # Agregar elemento a la lista
sample_list.pop() # Eliminar el último elemento de la lista
sample_list[2] = 22
print(sample_list)
sample_list[2] = "Bye"
print(sample_list)

# Bucles/Loops/Ciclos
print(len(sample_list))
# Imprimir cada elemento de una lista
for sample in sample_list:
    print(sample)

# Imprimir los números del 1 al 10
for numbers in range(1,11):
    print(numbers)

space()

# Imprimir el último elemento de una lista sin saber
# cuántos elementos tiene
another_list = [5, "Hola", "Bye", 4]
# Imprime el elemento de la lista cuyo índice es igual a la logitud
# de la lista menos 1 (porque el contéo inicia en 0)
print(another_list[len(another_list)-1])

another_list.append("AAAAAAAAA")
print(another_list[len(another_list)-1])

############ FUNCIONES ############

def sample_function(argumentos): # Definición de la función sample_function
    print("Sample", argumentos)

def saludo(pname):
    print("Hola", pname)

saludo("José")

# Ejemplo 1
def adition1(num1,num2):
    resultado=num1+num2
    return resultado
print(adition1(15,30))

# Ejemplo 2
def adition2(num1,num2):
    resultado=num1+num2
    print("El resultado de",num1,"+",num2, "es igual a", resultado)
adition2(15,30)

# Ejemplo 3
def adition3(num1,num2):
    return num1 + num2
print(adition3(15,30))

space()
# Ej. Crear una función que reciba como parámetro dos numeros
# y retornar la resta de los números, luego llamar a la función
# e imprimir el resultado

def substraction(numS1, numS2):
    return numS1-numS2

print(substraction(651,561))
print(substraction(354,64859))
print(substraction(9842,214))
print(substraction(546,46))

space()

# Crear una funcion salu2 que reciba como parámetro nombre y edad e imprimir
# "Hola, soy ___ y tengo ___ años"

def salu2(name, age):
    print("Hola, soy", name, "y tengo", age, "años")

salu2("José", 22)


space()

def rango(start,end):                   # Creamos función rango desde el valor start hasta el valor end
    lista_num = []                      # Creamos una lista vacía
    condition=start                     # Declaramos una variable
    while condition<end+1:              # Función para condicionar a menor que end+1
        lista_num.append(condition)     # Agregamos los valores a la lista que creamos antes
        condition=condition+1           # Acumulamos los valores para que vayan aumentando
    return lista_num                    # Retornamos la lista

range_list=rango(7,21)                  # Declaramos la variable range_list igual a la lista creada
print(range_list)                       # Imprimimos la lista

space()

# Ej. Crear una función sum_list que reciba como argumento una lista de números
# y retorne la suma de sus elementos

numbers_list1 = [1,2,3,4,5,6,7,8,9,10]
numbers_list2 = [6,4,8,2,6,4,19,8,5,2]

# Función que halla la suma de los elementos de la lista
def sum_list(list_sample):
    x = 0
    for sum in list_sample:
        x = x + sum
    return x

Suma_de_lista1 = sum_list(numbers_list1)
print("La suma de los elementos de la lista es",Suma_de_lista1)

Suma_de_lista2 = sum_list(numbers_list2)
print("La suma de los elementos de la lista es",Suma_de_lista2)

space()

# Función que halla la suma de los cuadrados de los elementos de la lista
def sum_list_sqr(list_sample):
    x=0
    for sum in list_sample:
        x = x + (sum*sum)
    return x

Suma_de_lista1 = sum_list_sqr(numbers_list1)
print("La suma de los cuadrados de los elementos de la lista es",Suma_de_lista1)

Suma_de_lista2 = sum_list_sqr(numbers_list2)
print("La suma de los cuadrados de los elementos de la lista es",Suma_de_lista2)

space()

# Función que eleva al cuadrado todos los elementos de la lista
def sqr_list(list_sample):
    list_sqr = []
    s = 0
    for sqr in list_sample:
        s = sqr * sqr
        list_sqr.append(s)
    return list_sqr

Cuadrado_de_lista1 = sqr_list(numbers_list1)
print(Cuadrado_de_lista1)

Cuadrado_de_lista2 = sqr_list(numbers_list2)
print(Cuadrado_de_lista2)

space()

grupo5 = ["N","F1","F2","A"]
print(grupo5)
for J in grupo5:
    print("Hola", J)
for DEL in range(len(grupo5)):
    print(grupo5)
    grupo5.pop()

print(grupo5)
grupo5.append("P")
print(grupo5)