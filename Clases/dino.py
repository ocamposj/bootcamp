class Animal:
    vivo = False

    def __init__(self):
        self.vivo = True

    def esta_vivo(self):
        print("Estoy vivo")
    
    def morir(self):
        self.vivo = False

class Dino(Animal):
    def __init__(self, un_nombre, un_color, canti_patas=2, un_genero=None):
        self.nombre = un_nombre
        self.color = un_color
        self.patas = canti_patas
        self.genero = un_genero
        print("Nací")

    def saludar(self):
        print("Hola, me llamo", self.nombre, "tengo", self.patas, "patas, soy", self.color, "y soy", self.genero)
    
    def cortar_pata(self, cantidad_de_patas_a_cortar = 1):
        print("Se quieren cortar", cantidad_de_patas_a_cortar, "patas")
        if self.patas > 0:
            self.patas = self.patas - cantidad_de_patas_a_cortar
            if self.patas <= 0:
                self.patas = self.patas + cantidad_de_patas_a_cortar
                print("Quieres cortar más patas de las que hay")
        

rex = Dino("Pepe", "azul",2,"macho")
rex.saludar()
print(rex.patas)
rex.cortar_pata(3)
print(rex.patas)

class TRex(Dino):

    def __init__(self, nombre, patas = 4, color = None):
        self.nombre = nombre
        self.patas = patas
        self.color = color
        print("Hola, soy un TRex y me llamo", self.nombre)

roberto = TRex("Roberto",4)
print(roberto.vivo)