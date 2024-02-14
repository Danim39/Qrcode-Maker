from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
import sys
import qrcode
from PyQt6.QtWidgets import QWidget

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)

        self.setWindowTitle("Qrcode Maker")

        man_layout=QGridLayout()
        box_layout=QGridLayout()
        button_layout=QGridLayout()

        man_layout.addLayout(button_layout,1,0,1,1)
        man_layout.addLayout(box_layout,0,0,1,1)
        self.setLayout(man_layout)


        self.txturl=QLineEdit()
        box_layout.addWidget(self.txturl,0,1,1,1)

        self.txtname=QLineEdit()
        box_layout.addWidget(self.txtname,1,1,1,1)

        self.button=QPushButton()
        self.button.setText("Make my Qrcode")
        button_layout.addWidget(self.button,0,0,1,1)
        self.button.clicked.connect(self.qrcod)
        self.button.clicked.connect(self.message)
        self.txturl.textChanged.connect(self.check_fields)
        self.txtname.textChanged.connect(self.check_fields)
        
        url=QLabel()
        url.setText("URL :")
        box_layout.addWidget(url,0,0,1,1)

        name=QLabel()
        name.setText("Name for Save :")
        box_layout.addWidget(name,1,0,1,1)

    def qrcod(self):
        if self.txturl.text() != "":
    
            qr = qrcode.make(self.txturl.text())
        qr.save(self.txtname.text() +".png")
        
    def message(self):
        message="success full"
        msg_box=QMessageBox()
        msg_box.setText(message)
        msg_box.show()
        msg_box.exec()

    def message2(self):
        if self.txturl and self.txtname=="":
            messag=QMessageBox()
            messag.setText("Enter url and name ")

    def check_fields(self):
        if self.txturl.text() and self.txtname.text():
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)
app=QApplication(sys.argv)
form=Form()
form.show()
sys.exit(app.exec())