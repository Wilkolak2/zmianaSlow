import sys


from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.zmien.clicked.connect(self.zmien)


    def zmien(self):
        size = "none"
        if self.ui.male.isChecked():
            size = self.ui.value1.text()
            self.ui.value2.setText(size.lower())

        if self.ui.duze.isChecked():
            size = self.ui.value1.text()
            self.ui.value2.setText(size.upper())

        if self.ui.odwrotnie.isChecked():
            size = self.ui.value1.text()
            self.ui.value2.setText(size[::-1])




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myForm()
    sys.exit(app.exec())
