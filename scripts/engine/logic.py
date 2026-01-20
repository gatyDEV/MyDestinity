#logic.py
#Importando librerias necesarias para el uso de este script
import os, json
import random
from .gui import menus, noticias, paises
from .entity.entitys import Character
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Bienvenida
print(Fore.MAGENTA + "---Bienvenido A MyDestinity---\nUn simulador de vida.\nCree su personaje primero")

#---Configurando Variables---
nombre = input(Fore.LIGHTRED_EX + "Escriba un nombre: ")
while any(c.isdigit() for c in nombre):
    nombre = input(Fore.LIGHTRED_EX + "El nombre no puede tener números. Intente otra vez: ")


screen = 1 #Variable que controle el menu

#Elejimos un pais random
pais_elejido = random.choice(paises)

#------Funciones------

#Funcion que borra la consola
def update():   
    os.system('cls')

#---Creaciones---

player = Character(nombre, pais_elejido)

#Funcion principal que ejecuta toda la logica del programa
def run_logic(screen):
    menus(player, screen)
    #Detectamos si esta vivo
    if player.alive == True:
        
        #Si de tecta que esta vivo se activa el bucle infinito DETECTA: entrada y salida
        while True:
            #Eventos Aleatorios
            #La entrada del usuario
            command = input(Fore.GREEN + ">>> ")
            
            #Noticias randoms
            noticia = random.choice(noticias)
            print(Fore.MAGENTA + noticia)

            #Revisamos si murio el usuario
            if not player.alive:
                print("El personaje está muerto.")
                break
    #----------------COMADOS-------------------------
        #---Comandos para el uso del usuario---
            
            #Comandos para ejecutar en la primera pantalla
            if screen == 1:

                if command.lower() == "0": #Comando para salir 
                    break

                elif command.lower() == "1": #Comando para avansar la edad
                    update()
                    menus(player, screen)
                    noticia = random.choice(noticias)
                    print(noticia)
                    player.age_up()
                
                elif command.lower() == "2": #Comando para ir ala segunda pantalla
                    screen = 2
                    update()
                    menus(player, screen)
                    noticia = random.choice(noticias)
                    print(noticia)

            #Comandos para ejecutar en la segunda pantalla
            elif screen == 2:
                
                if command.lower() == "0": #Comando para ir ala primera pantalla
                    screen = 1
                    update()
                    menus(player, screen)
                    noticia = random.choice(noticias)
                    print(noticia)
                
                elif command.lower() == "1": #Comando para comer
                    update()
                    menus(player, screen)
                    player.eat()
                    noticia = random.choice(noticias)
                    print(noticia)
                
                elif command.lower() == "2": #Comando para ejercitarse
                    update()
                    menus(player, screen)
                    player.exercise()
                    noticia = random.choice(noticias)
                    print(noticia)

                elif command.lower() == "3": #Salir a caminar
                    update()
                    menus(player, screen)
                    player.explorer()
                    print("¡Saliste a caminar")
                    noticia = random.choice(noticias)
                    print(noticia)
            

    #Que no aga mas nada
    else:
        pass
        
