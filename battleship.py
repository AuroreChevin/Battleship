#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from builtins import print

# la grille de jeu virtuelle est composée de 10 x 10 cases
# une case est identifiée par ses coordonnées (no ligne, no colonne),
# mais pour le joueur une colonne sera identifiée par une lettre (de 'A' à 'J')
GRID_SIZE = 10
# détermination de la liste des lettres utilisées pour identifier les colonnes :
LETTERS = "ABCDEFGHIJ"

# (tableau indexé par chacun de ces états)
SQUARE_STATE_REPR = [' ', 'X', '#', '-']
played_shots = set()
# def grid_square_state(coord):




def display_grid():
    """Affichage de la grille de jeu."""
    print('    ', end='')
    for x in range(GRID_SIZE):
        letter = LETTERS[x]
        print(' {}  '.format(letter), end='')
    print()
    print('  ', '+---' * GRID_SIZE + '+')
    for line_no in range(1, GRID_SIZE + 1):
        print('{:>2} |'.format(line_no), end='')
        for column_no in range(1, GRID_SIZE + 1):
            coord = (line_no, column_no)
            square_state = grid_square_state(coord)
            state_str = SQUARE_STATE_REPR[0]
            print(' {} |'.format(' '), end='')
        print()
        print('  ', '+---' * GRID_SIZE + '+')


aircraft_carrier = {(2, 2): True, (2, 3): True, (2, 4): True, (2, 5): True, (2, 6): True}  # porte_avion en B2
cruiser = {(4, 1): True, (5, 1): True, (6, 1): True, (7, 1): True}  # croiseur en A4
destroyer = {(5, 3): True, (6, 3): True, (7, 3): True}  # contre_torpilleur en C5
submarine = {(5, 8): True, (5, 9): True, (5, 10): True}  # sous_marin en H5
torpedo_boat = {(9, 5): True, (9, 6): True}  # torpilleur en E9
ships_list = [aircraft_carrier, cruiser, destroyer, submarine, torpedo_boat]
SEA = 0
MISSED_SHOT = 1
HIT_SHOT = 2
SUNK_SHOT = 3

def grid_square_state(coord):
 for x in played_shots:
    print(x, "x")

def ask_coord():
    shot_coord: str = input("Entrer les coordonnées d'un tir 99(max) :")
    shot_coord = (int(shot_coord[0]), int(shot_coord[1:]))
    played_shots.add(shot_coord)
    return shot_coord


def ship_is_hit(ship, coord):
    if coord in ship:
        ship[coord[0], coord[1]] = False
        return True


def ship_is_sunk(ship):
    if all(value is False for value in ship.values()):
        return True


def analyze_shot(ship, coord):
    if ship_is_hit(ship, coord):
        print("touché")
        if ship_is_sunk(ships):
            print("coulé")
            ships_list.remove(ships)
            print(ships_list)
        return True
    return False


while ships_list:
    display_grid()
    coord = ask_coord()
    for ships in ships_list:
        if analyze_shot(ships, coord):
            break
    else:
        print("raté")
else:
    print("terminé")

# aircraft_carrier = {(2, 2): True, (2, 3): True, (2, 4): True, (2, 5): True, (2, 6): True}  # porte_avion en B2
# aircraft_carrier[(2, 3)]  # connaitre l'état de la case C2
#
# aircraft_carrier[(2, 3)] = False  # indiquer que cette case est touchée
#
# (2, 3) in aircraft_carrier  # savoir si (2, 3) (case C2) fait partie des clés de ce dictionnaire
#
# (2, 7) in aircraft_carrier  # savoir si (2, 7) (case G2) fait partie des clés de ce diictionnaire
