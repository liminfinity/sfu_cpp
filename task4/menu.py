from PyQt5.QtWidgets import QWidget, QGridLayout, QMessageBox
from ui import create_button
from inflection import underscore
from widgets import SettingsWidget, PlayWidget, RatingWidget
from lib import load_rating
from constants import DEFAULT_RATING_PATH


class Menu(QWidget):
    """Меню."""

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.play_widget = None
        self.settings_widget = None
        self.rating_widget = None

    def init_ui(self):
        """Инициализация пользовательского интерфейса."""
        self.setWindowTitle("Меню")
        self.setGeometry(300, 300, 300, 100)
        self.setStyleSheet("background-color: #ffdab9; font-size: 18px;")
        self.create_controls()
        self.create_layout()

    def create_controls(self):
        """Создание элементов управления."""
        self.play_button = create_button(self, "Играть", self.play_clicked)
        self.settings_button = create_button(self, "Настройки", self.setting_clicked)
        self.rating_button = create_button(self, "Статистика", self.rating_clicked)

    def create_layout(self):
        """Создание макета для размещения элементов."""
        layout = QGridLayout(self)
        layout.addWidget(self.play_button, 0, 0)
        layout.addWidget(self.settings_button, 1, 0)
        layout.addWidget(self.rating_button, 2, 0)

    def play_clicked(self):
        """Обработка нажатия кнопки 'Играть'."""
        self.show_widget(PlayWidget)

    def setting_clicked(self):
        """Обработка нажатия кнопки 'Настройки'."""
        self.show_widget(SettingsWidget)

    def rating_clicked(self):
        """Обработка нажатия кнопки 'Статистика'."""
        
        rating_path = self.settings_widget.rating_path if self.settings_widget else DEFAULT_RATING_PATH
        try:
            ratings = load_rating(rating_path)
            self.show_widget(RatingWidget, ratings)
        except FileNotFoundError:
            QMessageBox.critical(self, "Ошибка", "Файл рекордов не найден")
            return None

    def closeEvent(self, event):
        """Закрытие всех открытых окон при закрытии основного окна."""
        self.close_open_widgets()
        event.accept()

    def show_widget(self, widget_class, *args):
        """Отображение указанного виджета, если он не открыт."""
        widget_name = underscore(widget_class.__name__)
        widget = getattr(self, widget_name, None)
        if widget is None:
            widget = widget_class(*args)
            setattr(self, widget_name, widget)
        widget.show()

    def close_open_widgets(self):
        """Закрытие всех открытых виджетов."""
        for attr_name in dir(self):
            widget = getattr(self, attr_name)
            if isinstance(widget, QWidget) and widget.isVisible():
                widget.close()
