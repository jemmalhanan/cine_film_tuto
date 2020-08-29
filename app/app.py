from PySide2 import QtWidgets, QtGui, QtCore


class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        pass


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
