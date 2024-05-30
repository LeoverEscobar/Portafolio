# Aplicaciones/tictactoe/views.py
from django.shortcuts import render
from .models import Game
from django.http import JsonResponse

def display_board(request):
    game = Game.objects.first()
    return render(request, 'tictactoe/board.html', {'game': game})

def make_move(request):
    if request.method == 'POST':
        # Obtener los datos del movimiento del jugador desde la solicitud POST
        row = int(request.POST.get('row'))
        col = int(request.POST.get('col'))

        # Obtener el juego actual
        game = Game.objects.first()

        # Validar si el movimiento es válido y realizar la actualización del tablero
        if is_valid_move(game, row, col):
            update_board(game, row, col)

            # Verificar si hay un ganador después del movimiento
            winner = get_winner(game)
            if winner:
                return JsonResponse({'success': True, 'message': 'Move successful', 'winner': winner})
            
            # Verificar si el juego está empatado
            if is_draw(game):
                return JsonResponse({'success': True, 'message': 'Move successful', 'draw': True})

            # Cambiar al siguiente jugador
            game.current_player = 'O' if game.current_player == 'X' else 'X'
            game.save()

            # Devolver una respuesta JSON indicando éxito
            return JsonResponse({'success': True, 'message': 'Move successful'})

    # Si la solicitud no es POST o el movimiento no es válido, devolver una respuesta JSON de error
    return JsonResponse({'success': False, 'message': 'Invalid move'})

def is_valid_move(game, row, col):
    # Verificar si la celda está vacía
    index = row * 3 + col
    return game.board[index] == ' '

def update_board(game, row, col):
    # Actualizar la celda del tablero con el símbolo del jugador actual
    index = row * 3 + col
    game.board = game.board[:index] + game.current_player + game.board[index + 1:]

def get_winner(game):
    # Comprobar filas, columnas y diagonales para determinar si hay un ganador
    lines_to_check = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]

    for line in lines_to_check:
        symbols = set(game.board[i] for i in line)
        if len(symbols) == 1 and ' ' not in symbols:
            return game.current_player

    return None  # No hay ganador

def is_draw(game):
    # Verificar si el juego está empatado (todos los espacios ocupados)
    return ' ' not in game.board
