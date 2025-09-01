# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 

@author: duena
"""
#Isai Dueñas Padron

#Encriptación y Desencriptación de Mensajes Secretos. Tú y tu mejor amigo están creando un sistema secreto para enviar mensajes entre ustedes sin que nadie más pueda entenderlos. Deciden utilizar un método de encriptación y desencriptación basado en listas o diccionarios.
#Parte 1: Encriptación. Crear una función llamada encriptar_mensaje que tome como entrada un mensaje de texto y utilice un diccionario para reemplazar cada letra por un código secreto. El diccionario de encriptación debe asignar a cada letra una cadena de caracteres alfanuméricos aleatorios. Ejemplo de diccionario:
#diccionario_encriptacion = {'a': '$%3', 'b': '8@*', 'c': '2&9', ...}
#Parte 2: Desencriptación. Crear una función llamada desencriptar_mensaje que tome como entrada un mensaje encriptado y utilice el mismo diccionario para revertir el proceso y obtener el mensaje original.

#
diccionario = {
    'a': '111', 'b': '222', 'c': '333', 'd': '444', 'e': '555',
    'f': '666', 'g': '777', 'h': '888', 'i': '999', 'j': '000',
    'k': 'aaa', 'l': 'bbb', 'm': 'ccc', 'n': 'ddd', 'o': 'eee',
    'p': 'fff', 'q': 'ggg', 'r': 'hhh', 's': 'iii', 't': 'jjj',
    'u': 'kkk', 'v': 'lll', 'w': 'mmm', 'x': 'nnn', 'y': 'ooo',
    'z': 'ppp', ' ': '___'
}

# Diccionario de forma inversa
dic_inv = {v: k for k, v in diccionario.items()}

def encriptar(msj):
    encriptado = ""
    for letra in msj.lower():
        encriptado += diccionario.get(letra, letra)
    return encriptado

def desencriptar(msj_enc):
    desencriptado = ""
    for i in range(0, len(msj_enc), 3):  
        bloque = msj_enc[i:i+3]
        desencriptado += dic_inv.get(bloque, bloque)
    return desencriptado


texto = "hola amigo"
enc = encriptar(texto)
dec = desencriptar(enc)

print("Original:", texto)
print("Encriptado:", enc)
print("Desencriptado:", dec)

if __name__ == "__main__":
    encriptar()
    desencriptar()
