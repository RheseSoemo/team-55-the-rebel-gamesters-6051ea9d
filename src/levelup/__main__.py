import sys
from levelup.ui import GameApp

#test

#this is a test 2

def main() -> None:
    app = GameApp()
    try:
        app.start()
    except KeyboardInterrupt:
        app.quit()
        sys.exit()


if __name__ == "__main__":
    main()
