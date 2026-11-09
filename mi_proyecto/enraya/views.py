from django.shortcuts import render

def comprobar_ganador(tablero, jugador):
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columnas
        [0, 4, 8], [2, 4, 6]             # Diagonales
    ]
    for linea in combinaciones:
        if tablero[linea[0]] == tablero[linea[1]] == tablero[linea[2]] == jugador:
            return True
    return False

def enraya(request):
    if request.method == 'POST':
        tablero_str = request.POST.get("tablero")
        turno = request.POST.get("turno")
        posicion = int(request.POST.get("posicion"))
        
        tablero = eval(tablero_str)

        terminado = False

        if tablero[posicion] == '-':
            tablero[posicion] = turno

            if comprobar_ganador(tablero, turno):
                mensaje = f'¡Ha ganado {turno}!'
                terminado = True
            elif '-' not in tablero:
                mensaje = '¡Empate!'
                terminado = True
            else:
                turno = 'O' if turno == 'X' else 'X'
                mensaje = f'Turno de {turno}'
        else:
            mensaje = f'Movimiento inválido. Turno de {turno}'

    else:
        tablero = ['-'] * 9
        turno = 'X'
        mensaje = 'Turno de X'
        terminado = False
                
    contexto = {
        'tablero': tablero,
        'turno': turno,
        'mensaje': mensaje,
        'terminado': terminado,
    }
    return render(request, 'enraya/index.html', contexto)
