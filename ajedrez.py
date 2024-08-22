def piezas():
    return {
        'peon_blanco': '♙', 'peon_negro': '♟',
        'torre_blanco': '♖', 'torre_negro': '♜',
        'caballo_blanco': '♘', 'caballo_negro': '♞',
        'alfil_blanco': '♗', 'alfil_negro': '♝',
        'reina_blanco': '♕', 'reina_negro': '♛',
        'rey_blanco': '♔', 'rey_negro': '♚'
    }

def tablero_vacio():
    return [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
    ]

def inicializar_tablero():
    tab = tablero_vacio()
    pzs = piezas()
    # Piezas blancas en la fila 1 y piezas negras en la fila 8
    tab[0] = [pzs['torre_negro'], pzs['caballo_negro'], pzs['alfil_negro'], pzs['reina_negro'], pzs['rey_negro'], pzs['alfil_negro'], pzs['caballo_negro'], pzs['torre_negro']]
    tab[1] = [pzs['peon_negro']] * 8
    # Piezas blancas en la fila 2 y piezas negras en la fila 7
    tab[6] = [pzs['peon_blanco']] * 8
    tab[7] = [pzs['torre_blanco'], pzs['caballo_blanco'], pzs['alfil_blanco'], pzs['reina_blanco'], pzs['rey_blanco'], pzs['alfil_blanco'], pzs['caballo_blanco'], pzs['torre_blanco']]
    return tab


def imprimir_tablero(tablero):
    for fila in tablero:
        print(' | '.join(map(lambda x: x if x else ' ', fila)))

#Movimiento del caballo
def mover_peon(tablero, origen, destino, es_primer_movimiento=False):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino
    pieza_origen = tablero[fila_origen][columna_origen]
    pieza_destino = tablero[fila_destino][columna_destino]

    movimiento_valido = False
    # Movimiento hacia adelante
    if columna_destino == columna_origen and pieza_destino is None:
        if pieza_origen in ['♙', '♟']:  # Verificar si es un peón
            avance = fila_destino - fila_origen
            if pieza_origen == '♙' and avance == 1 or (es_primer_movimiento and avance == 2):
                movimiento_valido = True
            elif pieza_origen == '♟' and avance == -1 or (es_primer_movimiento and avance == -2):
                movimiento_valido = True
    # Captura diagonal
    elif abs(columna_destino - columna_origen) == 1:
        if pieza_origen == '♙' and fila_destino - fila_origen == 1 and pieza_destino is not None:
            movimiento_valido = True
        elif pieza_origen == '♟' and fila_origen - fila_destino == 1 and pieza_destino is not None:
            movimiento_valido = True

    if movimiento_valido:
        if (pieza_origen == '♙' and fila_destino == 7) or (pieza_origen == '♟' and fila_destino == 0):
            # Determinar el color de la pieza para la promoción
            color_pieza = 'blanco' if pieza_origen == '♙' else 'negro'
            pieza_promocion = elegir_promocion(color_pieza)
            # Convertir clave de promoción a pieza correspondiente
            tablero[fila_destino][columna_destino] = piezas()[pieza_promocion]
        else:
            tablero[fila_destino][columna_destino] = pieza_origen
        tablero[fila_origen][columna_origen] = None
    else:
        print("Movimiento de peón no válido")

    return tablero


def elegir_promocion(color):
    if color == 'blanco':
        opciones = "reina_blanco, alfil_blanco, caballo_blanco, torre_blanco"
    elif color == 'negro':
        opciones = "reina_negro, alfil_negro, caballo_negro, torre_negro"
    else:
        raise ValueError("Color no válido. Debe ser 'blanco' o 'negro'.")
    
    print(f"Elige una pieza para la promoción ({color}): {opciones}")
    eleccion = input()
    
    # Validación básica de la elección
    if eleccion not in opciones.split(', '):
        print("Elección no válida. Intenta nuevamente.")
        return elegir_promocion(color)  # Llamada recursiva para corregir la elección
    return eleccion

#Movimiento del caballo
def mover_caballo(tablero, origen, destino):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino
    pieza_origen = tablero[fila_origen][columna_origen]
    pieza_destino = tablero[fila_destino][columna_destino]

    # Verificar si la pieza en la posición de origen es un caballo
    if pieza_origen not in ['♘', '♞']:  # '♘' para el caballo blanco, '♞' para el caballo negro
        print("La pieza en la posición de origen no es un caballo.")
        return tablero

    # Calcular la diferencia absoluta en filas y columnas entre el origen y el destino
    diff_filas = abs(fila_destino - fila_origen)
    diff_columnas = abs(columna_destino - columna_origen)

    # Verificar si el movimiento es válido para un caballo
    movimiento_valido = (diff_filas == 2 and diff_columnas == 1) or (diff_filas == 1 and diff_columnas == 2)

    if movimiento_valido:
        # Realizar el movimiento si el destino no contiene una pieza del mismo color
        if pieza_destino is None or (pieza_origen in ['♘'] and pieza_destino in ['♟', '♜', '♞', '♝', '♛', '♚']) or (pieza_origen in ['♞'] and pieza_destino in ['♙', '♖', '♘', '♗', '♕', '♔']):
            tablero[fila_destino][columna_destino] = pieza_origen
            tablero[fila_origen][columna_origen] = None
        else:
            print("Movimiento no válido. No puedes capturar tus propias piezas.")
    else:
        print("Movimiento de caballo no válido.")

    return tablero

#Movimiento del alfil
def es_diagonal(origen, destino):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino
    return abs(fila_destino - fila_origen) == abs(columna_destino - columna_origen)

def camino_despejado(tablero, origen, destino):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino
    paso_fila = 1 if fila_destino > fila_origen else -1
    paso_columna = 1 if columna_destino > columna_origen else -1
    fila_actual, columna_actual = fila_origen + paso_fila, columna_origen + paso_columna
    
    while fila_actual != fila_destino:
        if tablero[fila_actual][columna_actual] is not None:
            return False
        fila_actual += paso_fila
        columna_actual += paso_columna
    return True

def piezas_del_mismo_color(pieza):
    # Piezas blancas
    piezas_blancas = ['♙', '♖', '♘', '♗', '♕', '♔']
    # Piezas negras
    piezas_negras = ['♟', '♜', '♞', '♝', '♛', '♚']

    if pieza in piezas_blancas:
        return piezas_blancas
    elif pieza in piezas_negras:
        return piezas_negras
    else:
        raise ValueError("Pieza no reconocida")


def mover_alfil(tablero, origen, destino):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino
    pieza_origen = tablero[fila_origen][columna_origen]
    pieza_destino = tablero[fila_destino][columna_destino]

    if pieza_origen not in ['♗', '♝']:
        raise ValueError("La pieza seleccionada no es un alfil.")

    if not es_diagonal(origen, destino):
        raise ValueError("Movimiento de alfil no válido.")

    if not camino_despejado(tablero, origen, destino):
        raise ValueError("El camino está bloqueado.")

    if pieza_destino and pieza_destino in piezas_del_mismo_color(pieza_origen):
        raise ValueError("Movimiento inválido: no puedes capturar tus propias piezas.")

    tablero[fila_destino][columna_destino] = pieza_origen
    tablero[fila_origen][columna_origen] = None
    return tablero

#############################################################
#Movimiento de torre:
def is_path_clear(tablero, origen, destino, horizontal):
    paso = 1 if destino > origen else -1
    for i in range(origen + paso, destino, paso):
        index = i if horizontal else (origen, i) if horizontal else (i, origen)
        if tablero[index[0]][index[1]] is not None:
            return False
    return True

def mover_torre(tablero, origen, destino):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino
    pieza_origen = tablero[fila_origen][columna_origen]
    pieza_destino = tablero[fila_destino][columna_destino]

    if pieza_origen not in ['♖', '♜']:
        raise ValueError("La pieza seleccionada no es una torre.")

    if fila_origen != fila_destino and columna_origen != columna_destino:
        raise ValueError("Movimiento de torre no válido.")

    horizontal = fila_origen == fila_destino
    if not is_path_clear(tablero, columna_origen if horizontal else fila_origen, columna_destino if horizontal else fila_destino, horizontal):
        raise ValueError("El camino está bloqueado.")

    if pieza_destino is None or pieza_destino not in piezas_del_mismo_color(pieza_origen):
        tablero[fila_destino][columna_destino] = pieza_origen
        tablero[fila_origen][columna_origen] = None
    else:
        raise ValueError("Movimiento inválido: no puedes capturar tus propias piezas.")

    return tablero

############################################################
#Movimiento de una reyna
def is_path_clear2(tablero, origen, destino):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino

    if fila_origen == fila_destino:  # Movimiento horizontal
        paso = 1 if columna_destino > columna_origen else -1
        for columna in range(columna_origen + paso, columna_destino, paso):
            if tablero[fila_origen][columna] is not None:
                return False
    elif columna_origen == columna_destino:  # Movimiento vertical
        paso = 1 if fila_destino > fila_origen else -1
        for fila in range(fila_origen + paso, fila_destino, paso):
            if tablero[fila][columna_origen] is not None:
                return False
    else:  # Movimiento diagonal
        paso_fila = 1 if fila_destino > fila_origen else -1
        paso_columna = 1 if columna_destino > columna_origen else -1
        for f, c in zip(range(fila_origen + paso_fila, fila_destino, paso_fila), range(columna_origen + paso_columna, columna_destino, paso_columna)):
            if tablero[f][c] is not None:
                return False
    return True

def mover_reina(tablero, origen, destino):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino
    pieza_origen = tablero[fila_origen][columna_origen]
    pieza_destino = tablero[fila_destino][columna_destino]

    if pieza_origen not in ['♕', '♛']:  # '♕' para reina blanca, '♛' para reina negra
        raise ValueError("La pieza seleccionada no es una reina.")

    # Verificar si el movimiento es válido (horizontal, vertical o diagonal)
    if fila_origen != fila_destino and columna_origen != columna_destino and abs(fila_destino - fila_origen) != abs(columna_destino - columna_origen):
        raise ValueError("Movimiento de reina no válido.")

    if not is_path_clear2(tablero, origen, destino):
        raise ValueError("El camino está bloqueado.")

    if pieza_destino is None or pieza_destino not in piezas_del_mismo_color(pieza_origen):
        tablero[fila_destino][columna_destino] = pieza_origen
        tablero[fila_origen][columna_origen] = None
    else:
        raise ValueError("Movimiento inválido: no puedes capturar tus propias piezas.")

    return tablero
############################################################
#Movimientos del rey
def mover_rey(tablero, origen, destino):
    fila_origen, columna_origen = origen
    fila_destino, columna_destino = destino
    pieza_origen = tablero[fila_origen][columna_origen]
    pieza_destino = tablero[fila_destino][columna_destino]

    if pieza_origen not in ['♔', '♚']:  # '♔' para rey blanco, '♚' para rey negro
        raise ValueError("La pieza seleccionada no es un rey.")

    # Verificar si el movimiento es válido (una casilla en cualquier dirección)
    if not (abs(fila_destino - fila_origen) <= 1 and abs(columna_destino - columna_origen) <= 1):
        raise ValueError("Movimiento de rey no válido.")

    # Verificar que el destino no esté ocupado por una pieza del mismo color
    if pieza_destino is not None and pieza_destino in piezas_del_mismo_color(pieza_origen):
        raise ValueError("Movimiento inválido: no puedes capturar tus propias piezas.")

    # Realizar el movimiento
    tablero[fila_destino][columna_destino] = pieza_origen
    tablero[fila_origen][columna_origen] = None

    return tablero



#############################################################
#pruebas de  movimiento

tablero_inicial = inicializar_tablero()

# Imprimir el tablero inicial para mostrar el estado inicial del juego
print("Tablero inicial:")
imprimir_tablero(tablero_inicial)

# Mover un peón blanco de su posición inicial (ejemplo (6, 0) a (4, 0) como el primer movimiento que permite avanzar dos casillas)
nuevo_tablero = mover_peon(tablero_inicial, (6, 0), (4, 0), es_primer_movimiento=True)
print("\nTablero después del primer movimiento del peón blanco:")
imprimir_tablero(nuevo_tablero)


print("\nTablero después del movimiento del caballo:")
origen = (7, 1)  # Posición inicial de un caballo blanco
destino = (5, 2)  # Un movimiento válido en "L" que captura un caballo negro

tablero = mover_caballo(nuevo_tablero, origen, destino)
imprimir_tablero(tablero)