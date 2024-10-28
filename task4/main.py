import sys
from PyQt5.QtWidgets import QApplication
from menu import Menu

def main():
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()