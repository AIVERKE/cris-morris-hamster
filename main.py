from game.audio import play_music, stop_music
from game.scenes import intro, first_choice
import os


def main():
    play_music("music/music.mp3")
    os.system("cls" if os.name == "nt" else "clear")
    intro()
    first_choice()


if __name__ == "__main__":
    main()
