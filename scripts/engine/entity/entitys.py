#character.py
#Importando librerias necesarias para el uso de este script
from colorama import Fore
import random as r

#Clase character
class Character:
    #Stats vida, alive, dinero etc
    def __init__(self, name, country, age=0):
        self.name = name #---nombre---
        self.country = country #---pais--
        self.age = age #---edad---
        self.salud = 100 #---salud---
        self.money = 0 #---dinero---
        self.happiness = 100 #---felizidad---
        self.alive = True #---vivo---
        
        #Detectamos que no se pase de salud

        if self.salud >= 100:
            self.salud = 100

        #Murio por mala salud
        if self.salud <= 0:
            self.die()
        elif self.salud <= 5:
            print(Fore.RED + f"!Peligro! tu salud es {self.salud}")

        #Murio por vejez
        if self.age >= 120:
            self.die()
            print(Fore.YELLOW + "murio por causas naturales")

#---------------METODOS PARA VIVIR---------------

    #---Metodo para subir de edad---
    def age_up(self):
        
        #Detetcamos si sigue con vida
        if not self.alive:
            return

        #Ajustamos stats edad, salud, felizidad
        self.age += 1
        self.salud -= 5
        self.happiness -= 2
        print(Fore.GREEN + f"Ahora tienes {self.age} años")

        # Muerte por salud
        if self.salud <= 0:
            self.die()
            return
        elif self.salud <= 5:
            print(Fore.RED + "⚠ ¡Peligro! Tu salud es muy baja")

        # Muerte por vejez
        if self.age >= 120:
            self.die()
            print(Fore.YELLOW + "Murió por causas naturales")

    #---Metodo de muerte---
    def die(self):
        self.alive = False
        print(Fore.YELLOW + "Murio por causas naturales")

#---------------METODOS PARA ACTIVIDADES---------------

    #---Hacer ejercisio---
    def exercise(self):
        if self.age >= 12:
            self.salud += 4
            print(Fore.GREEN + "¡Has hecho ejersicio!")
        else: 
            print(Fore.RED + "No puede hacer todavia ejercisio")
    
    #----Comer---
    def eat(self):
        #Ajustamos para que recopere felizidad y salud
        self.happiness += 9
        self.salud += 6
        print(Fore.MAGENTA + "¡Has comido :)!")
    
    #----Explorar----
    def explorer(self):
        self.happiness += 3
        self.salud += 1