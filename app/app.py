from PySide2 import QtWidgets, QtGui, QtCore
from film import Film, get_movies


class App(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ciné Film')
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()
        self.resize(500, 200)

    def setup_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.le_movie_title = QtWidgets.QLineEdit()
        self.btn_add_movie = QtWidgets.QPushButton("Ajouter film")
        self.list_movies = QtWidgets.QListWidget()
        self.list_movies.setSelectionMode(
            QtWidgets.QListWidget.ExtendedSelection)
        self.btn_delete_movie = QtWidgets.QPushButton(
            "Supprimer le(s) film(s)")

        self.main_layout.addWidget(self.le_movie_title)
        self.main_layout.addWidget(self.btn_add_movie)
        self.main_layout.addWidget(self.list_movies)
        self.main_layout.addWidget(self.btn_delete_movie)

    def setup_connections(self):
        self.btn_add_movie.clicked.connect(self.add_movie)
        self.btn_delete_movie.clicked.connect(self.delete_movie)
        self.le_movie_title.returnPressed.connect(self.add_movie)

    def populate_movies(self):
        movies = get_movies()
        for movie in movies:
            list_item = QtWidgets.QListWidgetItem(movie.title)
            list_item.setData(QtCore.Qt.UserRole, movie)
            self.list_movies.addItem(list_item)

    def add_movie(self):
        movie_title = self.le_movie_title.text()

        if not movie_title:
            return False
        else:
            movie = Film(movie_title)
            resultat = movie.add_to_movies()
        if resultat:
            list_item = QtWidgets.QListWidgetItem(movie.title)
            list_item.setData(QtCore.Qt.UserRole, movie)
            self.list_movies.addItem(list_item)
        self.le_movie_title.setText("")

    def delete_movie(self):
        for selected_item in self.list_movies.selectedItems():
            movie = selected_item.data(QtCore.Qt.UserRole)
            movie.delete_from_movies()
            self.list_movies.takeItem(self.list_movies.row(selected_item))


app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()
