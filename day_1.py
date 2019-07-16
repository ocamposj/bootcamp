def space():
    print("--------------------------------------------------------------------------------")

print(3.14*2.5) #non-int multiplication
print("Hello World " + "sdvnsoidvn") #str concatenation
print("Hello " * 10) 
a = 2
b = 12
c = "I want my degree"
print(a*b)
print(c)
print(a, b)

# Ej.1 Crear una variable NOMBRE y otra EDAD e imprimir
# Hola, me llamo____ y tengo____ años
name = "José"
age = 22
print("Hola, me llamo", name, "y tengo", age, "años")

# Ej. 1.1 Crear una variable HOBBY e imprimir
# Hola, me llamo____ y tengo____ años y mi hobby es___
hobby = "//information_not_available//"
print("Hola, me llamo", name, "y tengo", age, "años y mi hobby es", hobby)

listx = [1,b,8,6,12]
print(listx[0])
print(listx[1])

# Ej. Crear una lista, primer elemento = NAME,
#segundo elemento = AGE
#Imprimir "Hola, me llamo ___ y tengo ___ años"

data = ["José", 22]
print("Hola, me llamo", data[0], "y tengo", data[1], "años")

list2 = [0,1,2,3]
list3 = [4,5,6]
list4 = [1,2,5,4,6,4,8,2,3,4,56,5,4,56,5,6,4,8]

print(list2[2]*list3[1])
print(list4[list2[2]*list3[1]])

print(list2)
list2[0] = 7
print(list2)
list2.append(15)
print(list2)

# Ej. Agregar una profesión y un hobby a la lista data
# [listname.append]

data.append("Estudiante")
data.append("//information_not_available//")
print(data)
data.insert(4, 15)
print(data)

data.pop()
print(data)
data.remove(22)
print(data)
data.insert(1,22)

# Función len() => length

print(data)
print(len(data))
saludo = "Hello there"
print(len(saludo))

# Ej. Obtener la dimensión  de la lista de data e imprimir
# "La lista data tiene ___ elementos"

data_length = len(data)
print("La lista data tiene", data_length, "elementos")

# Ej. Imprimir el último elemento de una lista larga
# sin saber cuántos elementos tiene
listb = [1,2,5,8,6,4,9,5,2,3,15,4,9,6,4,5,2,1,5,6,4,30,9,8,2,6,5,4,2,6,5,7]
print(listb[len(listb)-1])
print(len(listb))
listb_length = (len(listb)-2)/3
print(listb_length)
print(listb[int(listb_length)], listb[int(listb_length)*2+1])

########### Bucles/Loops/Ciclos/Iteraciones ###########

list_subjects = ["Variables", "Listas", "Tipos de datos"]

for concept in list_subjects:
    print("Hoy aprendí", concept)
    print("Nice")
print("That's what I learned today")

# Recorrer una lista e imprimir en cada ciclo el valor del elemento
# con 3 signos de admiración y al final, fuera del bucle "FIN."

for admirationsgn in list_subjects:
    print(admirationsgn,"!!!")
print("FIN.")

X_axis = ["x1","x2","x3"]
Y_axis = ["y1","y2","y3"]
Z_axis = ["z1","z2","z3"]
State = [0,1,0]

for displayX in X_axis:
    for displayY in Y_axis:
        for displayZ in Z_axis:
            for state_value in State:
                print(displayX,displayY,displayZ,state_value)

space()

# Ej. Imprimir los números del 1 al 100 usando for y range
# Ej. Imprimir el resultado de la suma de los números del 1 al 100
sum_x = 0
for x in range(1,101):
    sum_x = x + sum_x
print(sum_x)

space()

# Fibonacci sucesion
a=0
b=1
c=0
for x in range(10):
    c=a+b
    print(c)
    a=b
    b=c