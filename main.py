#import
import random

#variables
jugador1: str =""
jugador2: str =""
puntosJugador1: int =""
puntosJugador2: int =""
contador: int =""
PartidosJugador1: int=""
confirmacion1: str =""
confirmacion2: str =""
jugador1Ventaja= 0
jugador2Ventaja = 0 
partidasGanadas = {"Jugador 1": 0, "Jugador 2": 0}


#Funciones

"""
Titulo: 
    Configuraciones del usuario.
Descripcion:
    Este bloque de codigo se encarga de dar la bienvenida a los 
    usuarios y de configurar sus nombre.
"""

print("Bienvenidos!!")

def menu(jugador1: str , jugador2: str,):
    invitado: str = "Sin asignar nombre"
    print("Configuraciones")
    print("Jugador 1:")
    jugador1: str = input()
    print("Jugador 2:")
    jugador2: str = input()
    print("Que empieze el juego")
    if jugador1 =="":
        print(invitado + " VS " + jugador2 )
    if jugador2 =="":
        print(jugador1 + " VS " + invitado )
    elif jugador1 or jugador2 == input():
        print(jugador1 + " VS " + jugador2) 


menu(jugador1, jugador2)


"""
Titulo: 
    Introduccion
Descripcion:
    Este bloque de codigo da una introduccion antes de empezar
    Para que los jugadores confirmen su participacion,
    Tambien les muestra como es la dinamica de los turnos.
"""

def introduccion(confirmacion1: str, confirmacion2: str):
    print("Cada jugador debera elegir un numero del 1 a 10")
    print("los turno tendran un porcentaje de acierto del 50% ")
    print("Este acierto es totalmente aleatorio.")
    print("Cada jugador debe confirmar su participacion.")
    print("Para confirmar el encuentro digite 1 si no desea continuar digite 0")
    print("jugador1")
    confirmacion1 = input()
    print("jugador2")
    confirmacion2 = input()

    if confirmacion1 and confirmacion2 == "1":
        print("Empezemos!!")
    if confirmacion1 and confirmacion2 == "0":
        print("Ooh parece que jugaremos en otra ocasion, hasta pronto! :( ") 
        return exit()       
        


introduccion(confirmacion1, confirmacion2)

"""
Titulo: 

Descripcion:

"""

def puntuacionTenis(puntosJugador1, puntosJugador2, jugador1Ventaja=False, jugador2Ventaja=False):

    # Diccionario de puntos
    puntos = {0: 0, 1: 15, 2: 30, 3: 40}

    # Ingresar los puntos de cada jugador
    puntosJugador1 = input("Ingrese los puntos del Jugador 1: ")
    puntosJugador2 = input("Ingrese los puntos del Jugador 2: ")

    # Verificar si los puntos son números válidos
    if not puntosJugador1.isnumeric() or not puntosJugador2.isnumeric():
        return print("Los puntos de jugador 1 y jugador 2 deben ser números válidos.")
        
    # Convertir los puntos a enteros
    puntosJugador1 = int(puntosJugador1)
    puntosJugador2 = int(puntosJugador2)
    
    # Verificar si hay ventaja
    if puntosJugador1 >= 4 and puntosJugador1 >= puntosJugador2 + 2:
        return print("Jugador 1 gana el juego")
    elif puntosJugador2 >= 4 and puntosJugador2 >= puntosJugador1 + 2:
        return print("Jugador 2 gana el juego")
    elif puntosJugador1 == 3 and puntosJugador2 == 3:
        return print("Deuce")
    elif puntosJugador1 == puntosJugador2:
        return f"{puntos[puntosJugador1]} iguales"
    elif puntosJugador1 > puntosJugador2:
        if puntosJugador1 == 4:
            return print("Ventaja Jugador 1")
        else:
            return f"{puntos[puntosJugador1]}-{puntos[puntosJugador2]}"
    else:
        if puntosJugador2 == 4:
            return print("Ventaja Jugador 2")
        else:
            return f"{puntos[puntosJugador1]}-{puntos[puntosJugador2]}"


puntuacionTenis(puntosJugador1, puntosJugador1, jugador1Ventaja, jugador2Ventaja)


"""




"""



def sumarVentaja(puntosJugador1, puntosJugador2):
    global jugador1Ventaja, jugador2Ventaja, partidasGanadas

    partidasGanadas = {"Jugador 1": 0, "Jugador 2": 0}


    if puntosJugador1 == "Jugador 1":
        jugador1Ventaja += 1
        if jugador1Ventaja >= 4:
            partidasGanadas["Jugador 1"] += 1
            print("Jugador 1 gana la partida!")
            jugador1Ventaja = 0
            jugador2Ventaja = 0
    elif puntosJugador2 == "Jugador 2":
        jugador2Ventaja += 1
        if jugador2Ventaja >= 4:
            partidasGanadas["Jugador 2"] += 1
            print("Jugador 2 gana la partida!")
            jugador1Ventaja = 0
            jugador2Ventaja = 0

    print("Partidas ganadas: ", partidasGanadas)

sumarVentaja(jugador1, jugador2)













































__name__ == '__main__'