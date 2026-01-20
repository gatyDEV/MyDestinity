#main.py
#Importando librerias necesarias para el uso de este script
import os
from scripts.engine.logic import run_logic, screen
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Configuraciones rapidas
os.system('cls')
os.system('title My Destinity')

#Detectamos si todo se ejecuta en este script
if __name__ == "__main__":
    run_logic(screen)