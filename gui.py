from PyQt6.QtWidgets import QFileDialog, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel, QProgressBar
from pathlib import Path
import qdarktheme
from PyQt6.QtCore import Qt
import os

#To find if user is on dark theme
import darkdetect

from converter import Converter

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Path to File
        self.path = ""
        self.progress = 0
        self.pages_to_be_skipped = []

        self.setWindowTitle('Result Converter')
        self.setGeometry(100, 100, 900, 210)

        # Dark Mode detection
        if darkdetect.isDark():
            qdarktheme.setup_theme()
        else:
            qdarktheme.setup_theme("light")

        # layout - Grid
        layout = QGridLayout()
        self.setLayout(layout)

        # file selection Button
        file_browse = QPushButton('Browse')
        # Connect to file selector
        file_browse.clicked.connect(self.open_file_dialog)

        # Save Button
        file_save = QPushButton('Submit',self)
        file_save.clicked.connect(self.submit)

        # Skip Pages text
        skip_text = QLabel("<h3>Skip:</h3>")
        skip_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.skipped_pages = QLineEdit()

        # Label To show file
        Name_Label=QLabel("<h3>File:</h3>")
        # Align file to center of grid box
        Name_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # file_name_location
        self.filename_edit = QLineEdit()
        # self.filename_edit.setText(str(self.path))

        # Progress bar
        self.progressbar = QProgressBar()

        # Info Text
        self.info_text = QLabel()
        self.give_info("Select Pdf File To Convert.")

        # Error text
        self.error_text = QLabel()
        self.give_error("Enter Pages to be skipped in a comma seperated format. For ex: 1,2,3,4")

        # Add all widgets
        layout.addWidget(Name_Label, 0, 0)
        layout.addWidget(skip_text, 1, 0)

        layout.addWidget(self.filename_edit, 0, 1, 1, 5)
        layout.addWidget(self.skipped_pages, 1, 1, 1, 5)
        layout.addWidget(file_browse, 0, 8)
        layout.addWidget(file_save, 2, 3)
        layout.addWidget(self.progressbar, 3, 2, 2, 3)
        layout.addWidget(self.info_text, 4, 2, 4, 3)
        layout.addWidget(self.error_text, 6, 2, 4, 3)

        # Show everything
        self.show()
        pass

    def give_info(self, text):
        self.info_text.setText(f'<center>{text}</center>')
        pass

    def give_error(self, text):
        self.error_text.setText(f'<b><center>{text}</center><b>')
        pass

    def print_pages(self):
        self.pages_to_be_skipped = list(map(int, self.skipped_pages.text().split(',')))

    def set_progress(self, val):
        if val >= self.progressbar.maximum():
            val = self.progressbar.maximum()
        self.progressbar.setValue(val)
        pass

    def submit(self):
        if self.path == '':
            self.give_info("No Path Provided")
            return

        self.print_pages()

        # Converter object
        csvpath = f'{os.getcwd()}/output.csv'
        converter = Converter(self.path, csvpath)

        n = converter.n_pages
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(n)
        self.progressbar.setRange(0,n)

        # Convert page by page
        for i in range(n):
            if (i+1) in self.pages_to_be_skipped:
                continue
            self.progressbar.setValue(i+1)
            converter.step(i)

        # Write to csv file
        converter.write()

        error = converter.report_errors()
            
        self.give_error(error)
        if '!!!' in error:
            self.give_info('')
            return

        info = f'Saved file {csvpath}'
        info += f'\n<b>Manually Skipped Pages: {self.pages_to_be_skipped}<b>'
        self.give_info(info)
        pass

    def open_file_dialog(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
            "Select a File",
            "", # Current directory if ""
            "pdf files (*.pdf)"
        )
        if filename:
            self.path = Path(filename)
            self.filename_edit.setText(str(self.path))
        pass
