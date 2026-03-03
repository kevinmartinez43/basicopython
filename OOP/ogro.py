from enemigo import *
import random

class Ogro(Enemigo):

    def __init__(self, puntos_energia=20, ataque=3):
        super().__init__(tipo_enemigo='Ogro', puntos_energia=puntos_energia, ataque=ataque)
        
    def habla(self):
        print("Ogro aplastar todo!!!")
        
    def ataque_especial(self):
        print("Ogro ataque especial")
        funciona_ataque_especial = random.random() < 0.20
        if funciona_ataque_especial:
            self.ataque += 4
            print("Ogro enojado y incremento su ataque por 4")
