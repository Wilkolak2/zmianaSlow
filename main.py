import sys


from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class myForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        # self.ui.zmien.clicked.connect(self.zmien)
        self.ui.value1.textChanged.connect(self.zmien)


    def zmien(self):
        text = self.ui.value1.text()
        result = text
        if self.ui.male.isChecked():
            result = text.lower()
            self.ui.value2.setText(text.lower())

        if self.ui.duze.isChecked():
            result = ste
            self.ui.value2.setText(text.upper())

        if self.ui.odwrotnie.isChecked():
            text = self.ui.value1.text()
            self.ui.value2.setText(text.swapcase())






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = myForm()
    sys.exit(app.exec())

