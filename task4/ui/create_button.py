from PyQt5.QtWidgets import QPushButton, QWidget

def create_button(parent_widget: QWidget, title: str, clickedCb=None) -> QPushButton:
    """Создание кнопки.
    Args:
        parent_widget (QWidget): Родительский виджет для кнопки.
        title (str): Заголовок кнопки.
        clickedCb (function, optional): Обработчик нажатия кнопки.
    Returns:
        QPushButton: Кнопка.
    """
    button = QPushButton(title, parent_widget)
    button.setStyleSheet("background-color: #f0e68c;")
    if clickedCb is not None:
        button.clicked.connect(clickedCb)
    
    return button