from random import randint

"""Здоровье и сала удара игрока"""
"knight_health = randint(10, 50)"
"impact_force = randint(10, 50)"
"""Чудовище"""
"monster_counter = 10"
"monster_health = randint(0, 10)"
"monster_impact_force = randint(0, 10)"
""" Яблоко Здоровья"""
"apple_health = randint(0, 10)"
"Меч силы"
'sword = randint()'

"""Начало игры"""


def start_hero() -> None:
    knight_health = randint(10, 50)
    impact_force = randint(10, 50)


"Первый ход"


def player_run() -> str:
    player_move = input()
    while player_move != '1' and player_move != '2':
        player_move = input('Введите коректное значение хода:')
    return player_move

