from PyQt6.QtWidgets import QApplication
from gui import MainWindow
import sys

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()

if __name__ == '__main__':
    main()