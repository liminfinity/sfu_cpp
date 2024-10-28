from PyQt5.QtWidgets import QWidget, QGridLayout, QMessageBox
from lib import validate_json_file
from ui import create_button, create_input
from constants import DEFAULT_RATING_PATH

class SettingsWidget(QWidget):
    """Настройки."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.rating_path = DEFAULT_RATING_PATH
        self.init_ui()
        
    def create_controls(self):
        """Создание элементов управления."""
        self.path_input, self.path_label = create_input(self, True, "Путь к файлу рекордов: ")
        self.save_button = create_button(self, "Сохранить", self.save_path)

    def create_layout(self):
        """Создание макета для размещения элементов."""
        layout = QGridLayout(self)
        layout.addWidget(self.path_label, 0, 0)
        layout.addWidget(self.path_input, 0, 1)
        layout.addWidget(self.save_button, 1, 0, 1, 2)

    def get_rating_path(self):
        return self.rating_path

    def init_ui(self):
        """Инициализация пользовательского интерфейса."""
        self.setWindowTitle("Настройки")
        self.setGeometry(300, 300, 300, 100)
        self.setStyleSheet("background-color: #ffdab9; font-size: 18px;")
        self.create_controls()
        self.create_layout()

    def save_path(self):
        """Обработчик нажатия кнопки сохранения."""
        path = self.path_input.text()
        
        is_valid, errors = self.is_valid_file(path)
        if is_valid:
            self.rating_path = path 
            QMessageBox.information(self, "Успех", "Путь сохранен")
            self.close()
        else:
            QMessageBox.critical(self, "Ошибка", "\n".join(errors))


    def is_valid_file(self, path):
        """Проверяет, существует ли путь, является ли он файлом и валиден ли файл."""
        try:
            is_valid, errors = validate_json_file(path, ['name', 'score'])
        except Exception as e:
            return False, [f"Ошибка при валидации файла: {str(e)}"]
        
        return is_valid, errors
