# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 21:44:05 2025

@author: duena
"""

# Isai Dueñas Padron, Grupo 942, 29/08/2025.

#Historial de Cambios en una Hoja de Cálculo. Simula el historial de cambios en una hoja de cálculo, donde los usuarios pueden realizar cambios en las celdas. Usa una lista como pila para almacenar los cambios y permite a los usuarios deshacer múltiples cambios.
#Implementa funciones para registrar un cambio en la hoja de cálculo (por ejemplo, cambiar el valor de una celda) y deshacer el último cambio.
#Cada cambio debe incluir la celda modificada y el valor anterior.
#Simula una serie de cambios y la función de deshacer.


class hoja_calculo:

    #Esta solo es una lista que guarda el historial de cambios
    historial = []

    #Esta funcion registra los cambios 
    def registrar_cambio(celda, valor_anterior):
        hoja_calculo.historial.append((celda, valor_anterior))

    #Con esta funcion desasemos el ultimo cambio
    def deshacer_cambio():
        if hoja_calculo.historial: 
        #Esto solo es para verificar que 
        #efectivamente hay un cambio
            hoja_calculo.historial.pop()
        else:
            print("No hay cambios para quitar mijit@.")

    #Con esto mostramos el historial actual
    def mostrar_historial():
        print(hoja_calculo.historial)



if __name__ == "__main__":
    hoja_calculo.registrar_cambio('A1', 10)
    hoja_calculo.registrar_cambio('B2', 20)
    hoja_calculo.registrar_cambio('C3', 30)

    print("Historial después de cambios:")
    hoja_calculo.mostrar_historial()

    #Quitar el primer cambio
    hoja_calculo.deshacer_cambio()
    print("Historial después de quitar el primer cambio:")
    hoja_calculo.mostrar_historial()

    #Quitar el segundo cambio
    hoja_calculo.deshacer_cambio()
    print("Historial después de quitar el otro cambio:")
    hoja_calculo.mostrar_historial()
    
  