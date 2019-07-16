class Persona:      # Definimos la clase, una receta para crear un objeto
                    # o también la clase es pla "plantilla"
    edad = 0        # Atributo de clase o propiedad del objeto que vamos a crear

    def __init__(self, un_nombre):  #__init__ es el método constructor
                                    # métodos --> funciones dentro de una clase
        self.mi_nombre = un_nombre  # Usamos self para referirnos al objeto mismo
        print("Hola, nací, me llamo", self.mi_nombre)
    
    def cumple(self):               # Cumple es un método de la clase Persona
        self.edad = self.edad + 1   # que aumenta la propiedad edad en 1

    def asignar_edad(self,mi_edad): # Es un método que recibe un argumento
        self.edad = mi_edad         # y asigna a la propiedad edad del objeto
        print("Mi edad es", self.edad, "años")
    
    def fav_color(self,color):
        self.color_favorito = color
        print("Mi color favorito es", self.color_favorito)

    def altura(self,altura_cm):
        self.mi_altura = altura_cm
        print("Mido", self.mi_altura,"cm")

    def asignar_nac(self, mi_nacionalidad):
        self.nacionalidad = mi_nacionalidad

    def saludo(self):
        print("Hola, soy", self.mi_nombre, "y mi nacionalidad es", self.nacionalidad)

pepe = Persona("Pepito")
pepe.asignar_edad(22)
pepe.fav_color("azul")
pepe.altura(170)

# Ej. Agregar un método a la clase Persona que asigne una nacionalidad
# y otro método Saludo que imprima "Hola, soy _nombre_ y mi nacionalidad 
# es _nacionalidad__"

pepe.asignar_nac("paraguaya")
pepe.saludo()