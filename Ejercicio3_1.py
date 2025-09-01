#Isai Dueñas Padron

#Navegación en un Almacén. En este ejercicio, el personaje es un robot que debe recoger productos en un almacén. El almacén está representado como una cuadrícula (grid), donde cada celda puede estar vacía (.), contener un obstáculo (#), o contener un producto (P), el inicio siempre es la posición 0,0. El robot comienza en la esquina superior izquierda del almacén y puede moverse hacia la derecha (R), abajo (D), izquierda (L), arriba(U). El objetivo es recoger todos los productos siguiendo una secuencia de movimientos dados y luego retornar al punto de inicio. 
#NOTA: LOS MOVIMIENTOS IZQUIERDA (L) Y ARRIBA (U) SE ACTIVAN SOLO PARA RETORNAR AL PUNTO DE INICIO.
#Crear el Almacén: Representa el almacén como una lista de listas (una matriz) donde cada sublista es una fila del almacén.
#Registrar Movimientos: Implementa una función que tome la lista de movimientos y verifique si el robot recoge todos los productos y retorna al punto de inicio sin chocar con obstáculos.
#Verificar Obstáculos: Si el robot encuentra un obstáculo durante su camino, el movimiento es inválido.
#Retornar Resultado: La función debe retornar True si los movimientos son válidos, recogen todos los productos y llevan al robot de vuelta al punto de inicio, o False en caso contrario.


def VerifReProduc(almacen , movimiento):
    
    almc = almacen
    mov = movimiento
    
    filas, columnas = len(almc), len(almc[0])
    x, y = 0, 0
    ProducRecogidos = set()
    TotalDProductos = sum(row.count('P') for row in almc)


    for mov in mov:
        if mov == 'R':
            y += 1
        elif mov == 'D':
            x += 1
        elif mov == 'L':
            y -= 1
        elif mov == 'U':
            x -= 1


        if x < 0 or x >= filas or y < 0 or y >= columnas:
            return False
        if almc[x][y] == '#':
            return False
        if almc[x][y] == 'P':
            ProducRecogidos.add((x, y))


    #Aqui verifica si tomotodos los productos y regresa al principio
    return len(ProducRecogidos) == TotalDProductos and (x, y) == (0, 0)


almacen = [
    
    ['.', '.', '#', 'P'],
    ['.', '#', '.', '.'],
    ['P', '.', 'P', '.'],
    ['#', '.', '#', '.']
]



mov_correctos = ['D',
                         'D',
                         'R',
                         'R',
                         'U',
                         'R',
                         'U',
                         'D',
                         'L',
                         'D',
                         'L',
                         'L',
                         'U',
                         'U']

print("el orden es correcto?")
print(VerifReProduc(almacen, mov_correctos))
