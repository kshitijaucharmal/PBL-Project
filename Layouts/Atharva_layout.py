import sys
from PyQt6.QtWidgets import QApplication, QFileDialog, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel
from pathlib import Path
import qdarktheme
from PyQt6.QtCore import Qt
import darkdetect   #To find if user is on dark theme

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.path = "PATH NOT PROVIDED"

        self.setWindowTitle('Result Converter')
        self.setGeometry(100, 100, 900, 150)
        if not darkdetect.isDark():                          #To set theme as per user's system theme:
            qdarktheme.setup_theme()
        else:
            qdarktheme.setup_theme("light")
        layout = QGridLayout()
        self.setLayout(layout)

        # file selection
        file_browse = QPushButton('Browse')
        file_browse.clicked.connect(self.open_file_dialog)
        file_save=QPushButton('Submit',self)
        file_save.clicked.connect(self.sav)
        Name_Label=QLabel("<h3>File:</h3>")
        Name_Label.setAlignment(Qt.AlignmentFlag.AlignCenter) #align file to center of gridbox

        self.filename_edit = QLineEdit()

        layout.addWidget(Name_Label, 0, 0)
        layout.addWidget(self.filename_edit, 0, 1,1,5)
        layout.addWidget(file_browse, 0, 8)
        layout.addWidget(file_save,2,3)

        self.show()

    def sav(self):
        print(self.path)

    def open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self,
            "Select a File",
            "/home/odin5133/Desktop/Practice/PBL-Project/",
            "pdf files (*.pdf)"
        )
        if filename:
            self.path = Path(filename)
            self.filename_edit.setText(str(self.path))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
