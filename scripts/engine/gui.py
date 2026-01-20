#gui.py
#Importando librerias necesarias para el uso de este script
from colorama import Fore, Back, Style, init
init(autoreset=True)

def menus(player, screen):
    #---Pantalla principal---
    if screen == 1:
        print(Fore.WHITE + "---=MyDestinity=---\n" + Fore.YELLOW + f"|Nombre: {player.name} | Edad: {player.age} años|\n|Pais: {player.country}| Dinero: {player.money}|\n|Felizidad: {player.happiness} | Salud: {player.salud}|\n" + Fore.BLUE + "[0]-quit-:|Salir del programa|   [1]-next_year-:|Subir de año|   [2]-activity-:|Entrar a Actividades|\n[]-relacion-:|ver relaciones|")
    
    #---Pantalla de actividad ----ACTIVITY--- ---
    elif screen == 2:
        print(Fore.WHITE + "---=MyDestinity=---\n" + Fore.YELLOW + f"|Nombre: {player.name} | Edad: {player.age} años|\n|Pais: {player.country}| Dinero: {player.money}|\n|Felizidad: {player.happiness} | Salud: {player.salud}|\n" + Fore.BLUE + "[0]-principal-:|Entrar a Principal|   [1]-eat-:|Comer algo|   [2]-ejercicios-:|Ejercitarse|\n[3]-Salir de casa-:|Salir a caminar|    []-delito-:|Hacer un delito|")

paises = ["Argentina", "Brasil", "Bolivia", "Colombia", "Chile", "Ecuador", "Uruguay", "Paraguay", "Venezuela", "Guatemala", "El salvador", "Costa rica", "Haiti", "Nicaragua", "Honduras", "panama", "EEUU", "mexico", "peru", "cuba", "canada"]


noticias = [
    "Hubo un incendio en un edificio del centro.",
    "Canadá entró en guerra contra un país desconocido.",
    "Cuatro ladrones robaron un banco ayer por la noche.",
    "Se descubrió un nuevo planeta habitable.",
    "El precio del peso argentino volvió a bajar.",
    "Un famoso actor fue arrestado por conducir borracho.",
    "Un meteorito cayó cerca de una ciudad pequeña.",
    "Un científico creó una nueva tecnología revolucionaria.",
    "Se declaró una epidemia leve en una ciudad vecina.",
    "Un político renunció tras un escándalo.",
    "Un millonario donó toda su fortuna a la caridad.",
    "Un perro fue elegido alcalde de un pueblo.",
    "Una inteligencia artificial comenzó a escribir novelas.",
    "Un apagón dejó sin luz a todo el país por horas.",
    "Se encontró un tesoro enterrado en una playa."
]