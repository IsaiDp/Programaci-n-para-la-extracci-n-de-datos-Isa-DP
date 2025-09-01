# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 

@author: duena
"""

#Isai Dueñas Padron

#Sistema de Reserva. Desarrolla un sistema de reservas utilizando sets.
#Crea conjuntos para representar habitaciones disponibles y habitaciones
#reservadas en un hotel. Permite a los usuarios realizar reservas,
#liberar habitaciones y mostrar la disponibilidad actual. NOTA: No utilizar menú, 
#solo las funciones , realizar las pruebas necesarias para verificar funcionamiento adecuado.


habitaciones_disponibles = {1, 2, 3, 4, 5 }
habitaciones_reservadas = set()


def reservas():

    print("Habitaciones disponibles por el momento:\n ", habitaciones_disponibles)

    habitacion = int(input(" Seeleccione la habitacion a reservar: "))
    if habitacion in habitaciones_disponibles:
        habitaciones_disponibles.remove(habitacion)
        habitaciones_reservadas.add(habitacion)

        print(f"Reservacion de habitacion {habitacion} completada.")
    else:
        print("habitación no disponible.")


def liberar():
    habitacion = int(input("Habitacion a entregar: "))
    if habitacion in habitaciones_reservadas:
        habitaciones_reservadas.remove(habitacion)
        habitaciones_disponibles.add(habitacion)
        print(f"habitación {habitacion} disponible nuevamente ")
    else:
        print("Habitacopn aun no reservada.")


def disponibilidad():
    print("Habitaciones disponibles: ", habitaciones_disponibles)
    print()
    print("Habitaciones ya reserevadas: ", habitaciones_reservadas)


if __name__ == "__main__":
    reservas()
    disponibilidad()
    liberar()
  
