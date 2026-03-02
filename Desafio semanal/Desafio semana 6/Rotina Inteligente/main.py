import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from nucleo.aplicacao import Aplicacao


def main():
    app = Aplicacao()
    app.iniciar()


if __name__ == "__main__":
    main()
