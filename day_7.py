# For numbers 1 to N
# if number divisible by 3, print "fizz"
# if number divisible by 5, print "buzz"
# if number divisible by 3 and 5, print "fizzbuzz"
# else print the number

# Input: integer > 0
# Output: print stuff based on rules above

# while True:
#     number = int(input("Number: "))
#     if number >= 1:
#         if number%3 == 0 and number%5 == 0:
#             print("fizzbuzz")
#         elif number%3 == 0:
#             print("fizz")
#         elif number%5 == 0:
#             print("buzz")
#         else:
#             print(number)
#     else:
#         print("The number is out of range")

# Hacer una clase que se llame vehículo y que uno de ellos sea cantidad_ruedas
# y un método que sea definir_tipo_vehiculo que me diga si es "bicicleta,
# triciclo, auto" de acuerdo a la cantidad de ruedas.

class Vehiculo:
    ruedas = 0
    motor = False
    asientos = 0

    def __init__(self):
        print("Se ha creado un objeto del tipo Vehículo")
    
    def asignar_ruedas(self, cant_de_ruedas):
        self.ruedas = cant_de_ruedas
        print("El vehículo tiene", self.ruedas, "ruedas")
    
    def asignar_asientos(self, cant_de_asientos):
        self.asientos = cant_de_asientos
        print("El vehículo tiene", self.asientos, "asientos")
    
    def asignar_motor(self,tip_motor):
        if tip_motor == "si":
            self.motor = True
            print("El vehículo posee motor")
        else:
            self.motor = False
            print("El vehículo no posee motor")

    def definir_tipo_vehiculo(self):
        if self.ruedas == 2 and self.motor == True and self.asientos == 1:
            print("El vehículo es una motocicleta")
        elif self.ruedas == 2 and self.motor == False and self.asientos == 1:
            print("El vehículo es una bicicleta")
        elif self.ruedas == 3 and self.asignar_asientos == 1:
            print("El vehículo es un triciclo")
        elif self.ruedas == 4 and self.motor == True and self.asientos == 4:
            print("El vehículo es un automóvil")
        elif self.ruedas == 4 and self.motor == True and self.asientos == 5:
            print("El vehículo es una camioneta")
        elif self.ruedas == 4 and self.motor == True and self.asientos >= 10:
            print("El vehículo es un bus")
        else:
            print("No se reconoce el tipo de vehículo")

vehiculo_de_pepe = Vehiculo()
vehiculo_de_pepe.asignar_ruedas(4)
vehiculo_de_pepe.asignar_motor("si")
vehiculo_de_pepe.asignar_asientos(4)
vehiculo_de_pepe.definir_tipo_vehiculo()