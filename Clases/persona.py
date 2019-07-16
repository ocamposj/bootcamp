class Persona:
    edad = 0

    def __init__(self, un_nombre):
        self.mi_nombre = un_nombre
        print("Hola, nací, me llamo", self.mi_nombre)
    
    def cumple(self):
        self.edad = self.edad + 1
    
    def fav_color(self,color):
        self.color_favorito = color
        print("Mi color favorito es", self.color_favorito)

pepe = Persona("Pepito")
pepe.cumple()

print("Acabo de cumplir", pepe.edad)
pepe.fav_color("azul")