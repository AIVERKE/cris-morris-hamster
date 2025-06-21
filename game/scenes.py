from game.utils import print_slow
from game.audio import stop_music


def intro():
    print_slow("La Historia de Chris Morris, el Hámster Melódico\n")
    print_slow(
        "En un pequeño departamento de la ciudad, vivía Chris Morris, un hámster con una personalidad única.\n"
    )
    print_slow(
        "A pesar de su desaliño, siempre llevaba una cartera de colores vivos y un moño rosado.\n"
    )
    print_slow(
        "Podría parecer que solo quería impresionar, pero era su forma de mostrar que no le importaba lo que pensaran los demás.\n"
    )
    print_slow(
        "Chris compartía su hogar con su dueño, quien era fan de Radiohead. Cada tarde, mientras sonaban las melodías de la banda,\n"
    )
    print_slow(
        "Chris se movía inquieto en su rueda, sintiendo el pulso de la música que también le encantaba. Era su momento de libertad.\n"
    )
    print_slow(
        "Sin embargo, había una perra chow chow que capturaba su atención desde la ventana...\n"
    )
    print_slow("¿Qué decides hacer?\n")


def first_choice():
    print("1. Escuchar Radiohead desde el rincón de la jaula.")
    print("2. Escapar para explorar el jardín bajo la luz de la luna.")
    choice = input("Elige una opción (1 o 2): ")

    if choice == "1":
        stay_inside()
    elif choice == "2":
        escape_to_garden()
    else:
        print("Opción no válida. Elige de nuevo.\n")
        first_choice()


def stay_inside():
    print_slow("\nTe quedas en la jaula, moviendo tus patitas al ritmo de 'Creep'.")
    print_slow(
        "Aunque la música es reconfortante, algo dentro de ti te dice que esta noche es especial.\n"
    )
    print("1. Cambiar de opinión y escapar.")
    print("2. Quedarte y dormir.\n")
    choice = input("Elige una opción (1 o 2): ")

    if choice == "1":
        escape_to_garden()
    elif choice == "2":
        print_slow("\nTe duermes mientras la música sigue sonando...")
        print_slow(
            "Quizás nunca sabrás qué habría pasado si hubieras seguido ese instinto."
        )
        print_slow("Fin del juego. Chris Morris eligió la comodidad del hogar.")
        stop_music()


def escape_to_garden():
    print_slow("\nEmpujas la puerta de tu jaula y das un salto hacia la libertad.")
    print_slow(
        "El jardín se extiende ante ti, iluminado por la luna. El aire fresco llena tus pulmones.\n"
    )
    print("1. Ir al árbol donde conociste al chow chow.")
    print("2. Explorar las flores en el jardín de la vecina.\n")
    choice = input("Elige una opción (1 o 2): ")

    if choice == "1":
        chow_chow_memory()
    elif choice == "2":
        neighbor_garden()
    else:
        print("Opción no válida. Elige de nuevo.\n")
        escape_to_garden()


def chow_chow_memory():
    print_slow("\nTe acercas al árbol donde conociste al chow chow.")
    print_slow(
        "Recuerdas cómo te miraba con curiosidad, como si entendiera tu pequeño corazón."
    )
    print_slow(
        "Las hojas crujen bajo tus patas mientras un suave viento acaricia tu pelaje."
    )
    print_slow("De repente, escuchas a lo lejos 'Creep' nuevamente... es tu dueño.")
    print_slow("Sientes paz. Has vivido una buena vida.\n")
    print("1. Caminar hacia el jardín de la vecina.")
    print("2. Quedarte aquí y contemplar el cielo.\n")
    choice = input("Elige una opción (1 o 2): ")

    if choice == "1":
        neighbor_garden()
    elif choice == "2":
        peaceful_end()
    else:
        print("Opción no válida. Elige de nuevo.\n")
        chow_chow_memory()


def neighbor_garden():
    print_slow(
        "\nLlegas al jardín de la vecina. Las flores huelen dulces y el ambiente está en calma."
    )
    print_slow("Aquí fue donde conociste al chow chow por primera vez.")
    print_slow(
        "Te acurrucas entre las flores mientras escuchas los últimos acordes de 'Creep'."
    )
    print_slow("Recuerdas a tu dueño, la dueña del chow chow y a tu amiga peluda.\n")
    print_slow(
        "Cerrando los ojos por última vez, piensas: 'Qué vida tan maravillosa tuve.'\n"
    )
    print_slow(
        "Fin del juego. Chris Morris encontró su final en paz y rodeado de recuerdos hermosos."
    )
    input("Pulsa ENTER para salir")
    stop_music()


def peaceful_end():
    print_slow(
        "\nMiras las estrellas desde el árbol, sintiendo que esta es la última noche de tu vida."
    )
    print_slow(
        "Las memorias llenan tu corazón: el amor por la música, tus dueños, el chow chow..."
    )
    print_slow("Cerrando los ojos, te dejas llevar por la melodía de Radiohead.")
    print_slow(
        "Fin del juego. Chris Morris descansó en paz, celebrando una vida inolvidable."
    )
    input("Pulsa ENTER para salir")
    stop_music()
