#!/usr/bin/env python
#  -*- coding: utf-8 -*-
from builtins import print, tuple

# la grille de jeu virtuelle est composée de 10 x 10 cases
# une case est identifiée par ses coordonnées (no ligne, no colonne),
# mais pour le joueur une colonne sera identifiée par une lettre (de 'A' à 'J')

GRID_SIZE = 10

# détermination de la liste des lettres utilisées pour identifier les colonnes :
LETTERS = "ABCDEFGHIJ"

# chaque navire est constitué d'une structure de données permettant de
# connaitre l'état (intact ou touché) de chaque partie (case)
# du navire le constituant

# les navires suivants sont disposés de façon fixe dans la grille :
#      +---+---+---+---+---+---+---+---+---+---+
#      | A | B | C | D | E | F | G | H | I | J |
#      +---+---+---+---+---+---+---+---+---+---+
#      | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10|
# +----+---+---+---+---+---+---+---+---+---+---+
# |  1 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  2 |   | o | X | o | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  3 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  4 | o |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  5 | o |   | o |   |   |   |   | o | o | o |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  6 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  7 | o |   | o |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  8 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# |  9 |   |   |   |   | o | o |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
# | 10 |   |   |   |   |   |   |   |   |   |   |
# +----+---+---+---+---+---+---+---+---+---+---+
aircraft_carrier = {(2, 2): True, (2,3): True, (2, 4): True, (2, 5): True, (2, 6): True}  # porte_avion en B2
cruiser          = {(4, 1): True, (5, 1): True, (6, 1): True, (7, 1): True}  # croiseur en A4
destroyer        = {(5, 3): True, (6, 3): True, (7, 3): True}  # contre_torpilleur en C5
submarine        = {(5, 7): True, (5, 8): True, (5,9): True}  # sous_marin en H5
torpedo_boat     = {(9, 5): True, (9, 6): True}  # torpilleur en E9
ships_list = [aircraft_carrier, cruiser, destroyer,submarine, torpedo_boat]


while len(ships_list) >0:
    nb = input("Entrer les coordonnées d'un tir 99(max) :")
    nb = (int(nb[0]), int(nb[1]))
    for ships in ships_list:
        if nb in ships:
            ships[nb[0], nb[1]] = False
            print("touché", nb)
            if all(value is False for value in ships.values()):
                print("coulé")
                ships_list.remove(ships)
                print(ships_list)
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

