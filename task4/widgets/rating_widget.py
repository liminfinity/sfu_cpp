from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class RatingWidget(QWidget):
    def __init__(self, ratings):
        super().__init__()
        self.init_ui(ratings)

    
    def init_ui(self, ratings):
        """Инициализация пользовательского интерфейса."""
        self.setWindowTitle("Статистика игры")
        self.setGeometry(300, 300, 300, 100)
        self.setStyleSheet("background-color: #ffdab9; font-size: 18px;")
        self.layout = QVBoxLayout(self)
        self.display_ratings(ratings)

    def display_ratings(self, ratings):
        """Отображение рекордов в виде меток."""
        for rating in ratings:
            self.add_rating_label(rating)

    def add_rating_label(self, rating):
        """Добавление метки с записью в макет."""
        label_text = f"{rating['name']}: {rating['score']}"
        label = QLabel(label_text)
        self.layout.addWidget(label)
