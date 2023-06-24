from  PyQt6.QtWidgets import *
from PyQt6 import uic, QtGui
import sys
import os
import subprocess
from qt_material import apply_stylesheet
from PyQt5.QtGui import QPalette, QColor
import qdarktheme




app = QApplication(sys.argv)
# Apply the complete dark theme to your Qt App.
qdarktheme.setup_theme()




class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        apply_stylesheet(app=MyGUI, theme= 'dark_lightgreen.xml')
        uic.loadUi("imgviewer.ui", self)
        self.show()
        layout = QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle('PyQt File Dialog')
        #self.setGeometry(100, 100, 1000, 500 )

        
        self.current_file = "bg.jpg"
        pixmap = QtGui.QPixmap("self.current_file")
        pixmap = pixmap.scaled(self.width(), self.height())
        self.browse.clicked.connect(self.open_file)
        
        
       
        browse = QPushButton("Browse")
        browse.clicked.connect(self.open_file)



        n = 500 
        #n will be the total no. of files/entries
        self.progressbar = QProgressBar()
        self.progressbar.setMinimum(0)
        self.progressbar.setMaximum(n)
        self.progressbar.setRange(0,n)



    def open_file(self):
        response = QFileDialog.getOpenFileName(
                caption="open pdf",
                directory=os.getcwd(),
                filter="Data File (*.pdf)"
                )
        print(response)

        if response != "":
            file_0=response[0]
            print(file_0)
            self.current_file= file_0
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(self.width(), self.height())
            #self.label.setPixmap(pixmap)
            
            #subprocess.Popen([file_0], shell=True)
            mssg = QMessageBox()
            mssg.setText(file_0)
            mssg.exec()


        
        

        
    def resiseEvent(self, event):
        try:
            pixmap = QtGui.QPixmap(self.current_file)
        except:
            pixmap = QtGui.QPixmap("bg.jpg")
        pixmap = pixmap.scaled(self.width(), self.height())
        #self.label.setPixmap(pixmap)
        #self.label.resize(self.width(), self.height())

    
    

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec()
 
if __name__ == "__main__":
    main()   