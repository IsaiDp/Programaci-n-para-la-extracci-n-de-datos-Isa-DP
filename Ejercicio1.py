# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 21:01:32 2025

@author: duena
"""
# Isai Dueñas Padron, Grupo 942, 29/08/2025.

#Estadística Básica. Cree una clase llamada Estadística que contiene como atributo una lista de números naturales la cual puede contener repetidos. Debe contener los siguientes métodos:
#Frecuencia de Números. Dada la lista, devuelve una lista de tuplas con el número de veces que aparece cada número en la lista. La tupla debe tener el número y la cantidad de veces que aparece.
#Moda. Dada la lista, devuelva la moda de la lista (el valor más repetido). Puedes usar la función anterior como ayuda.
#Histograma. Dada la lista, muestra el histograma de la lista. Puedes reusar los métodos anteriores.


class ESTADISTICA:

    #Con esta función contamos cuántas veces aparece cada número en la lista y 
    #devuelve todos los números con su cantidad de apariciones.
    def frecuencia(lista):
        frec = {}
        for num in lista:
            frec[num] = frec.get(num, 0) + 1
        return sorted(frec.items())
    #En esta parte del codigo estamos buscando el numero y cuantas veces se 
    #repite, basicamente es lo que hace nuestro codigo de abajo, despues retorna 
    #el numero con mas repeticiones y esa es la moda.
    def moda(lista):
        frec = ESTADISTICA.frecuencia(lista)
        return max(frec, key=lambda x: x[1])[0]
    #Lo que hacemos con esta parte del codigo es representar cuantas veces 
    #aparece nuestro numero con asteriscos el cual lo denominamos como 
    #histograma
    def histograma(lista):
        for num, count in ESTADISTICA.frecuencia(lista):
            print(f"{num} {'*' * count}")

    #Hice todos los prints y lista en esta parte para tener todo un poco mas 
    #ordenado y poder en contrar mis posibles errores mas facilmente

if __name__ == "__main__":
    lista_numeros = [1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1]
    print("Frecuencia:", ESTADISTICA.frecuencia(lista_numeros))
    print("Moda:", ESTADISTICA.moda(lista_numeros))
    print("Histograma:") 
    ESTADISTICA.histograma(lista_numeros)
    
    #Profe sinceramente en este ejercicio me ayude un poco de chat porque 
    #habia algunas cosas que no recordaba y para darle un poco de limpieza al cd, 
    #pero trate de hacer todo lo posible por realizarlo casi completo y entenderlo.