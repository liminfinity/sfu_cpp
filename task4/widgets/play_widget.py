from PyQt5.QtWidgets import QWidget

class PlayWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Игра")
        self.setGeometry(300, 300, 300, 300)
        self.setStyleSheet("background-color: #ffdab9; font-size: 18px;")