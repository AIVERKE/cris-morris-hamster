from game.utils import print_slow
from game.audio import stop_music
from game.texts import texts


def intro():
    print_slow(texts["intro_title"])
    print_slow(texts["intro_1"])
    print_slow(texts["intro_2"])
    print_slow(texts["intro_3"])
    print_slow(texts["intro_4"])
    print_slow(texts["intro_5"])
    print_slow(texts["intro_6"])
    print_slow(texts["intro_choice"])


def first_choice():
    print(texts["choice_1"])
    print(texts["choice_2"])
    choice = input("Elige una opción (1 o 2): ")

    if choice == "1":
        stay_inside()
    elif choice == "2":
        escape_to_garden()
    else:
        print(texts["invalid_choice"])
        first_choice()


def stay_inside():
    print_slow(texts["stay_1"])
    print_slow(texts["stay_2"])
    print(texts["stay_choice_1"])
    print(texts["stay_choice_2"])
    choice = input("Elige una opción (1 o 2): ")

    if choice == "1":
        escape_to_garden()
    elif choice == "2":
        print_slow(texts["stay_end_1"])
        print_slow(texts["stay_end_2"])
        print_slow(texts["stay_end_3"])
        stop_music()
    else:
        print(texts["invalid_choice"])
        stay_inside()


def escape_to_garden():
    print_slow(texts["escape_1"])
    print_slow(texts["escape_2"])
    print(texts["escape_choice_1"])
    print(texts["escape_choice_2"])
    choice = input("Elige una opción (1 o 2): ")

    if choice == "1":
        chow_chow_memory()
    elif choice == "2":
        neighbor_garden()
    else:
        print(texts["invalid_choice"])
        escape_to_garden()


def chow_chow_memory():
    print_slow(texts["chow_1"])
    print_slow(texts["chow_2"])
    print_slow(texts["chow_3"])
    print_slow(texts["chow_4"])
    print_slow(texts["chow_5"])
    print(texts["chow_choice_1"])
    print(texts["chow_choice_2"])
    choice = input("Elige una opción (1 o 2): ")

    if choice == "1":
        neighbor_garden()
    elif choice == "2":
        peaceful_end()
    else:
        print(texts["invalid_choice"])
        chow_chow_memory()


def neighbor_garden():
    print_slow(texts["garden_1"])
    print_slow(texts["garden_2"])
    print_slow(texts["garden_3"])
    print_slow(texts["garden_4"])
    print_slow(texts["garden_5"])
    print_slow(texts["garden_6"])
    input(texts["end_input"])
    stop_music()


def peaceful_end():
    print_slow(texts["peaceful_1"])
    print_slow(texts["peaceful_2"])
    print_slow(texts["peaceful_3"])
    print_slow(texts["peaceful_4"])
    input(texts["end_input"])
    stop_music()
