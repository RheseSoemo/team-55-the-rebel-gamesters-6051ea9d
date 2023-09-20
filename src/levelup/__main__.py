import sys
from levelup.ui import GameApp
<<<<<<< HEAD

#test
=======
#this is a test

>>>>>>> 4258045 (test1)
def main() -> None:
    app = GameApp()
    try:
        app.start()
    except KeyboardInterrupt:
        app.quit()
        sys.exit()


if __name__ == "__main__":
    main()
