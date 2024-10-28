from PyQt5.QtWidgets import QLineEdit, QLabel, QWidget


def create_input(
    parent_widget: QWidget, has_label: bool, title: str = ""
) -> QLineEdit | tuple[QLineEdit, QLabel]:
    """Создание элемента ввода.

    Args:
        parent_widget (QWidget): Родительский виджет для элемента ввода.
        has_label (bool): Наличие метки.
        title (str): Заголовок метки.

    Returns:
        QLineEdit: Элемент ввода,
        QLabel: Метка, если она есть.
    """

    q_input = QLineEdit(parent_widget)
    q_input.setStyleSheet("font-size: 18px; background-color: white;")

    if has_label:
        label = QLabel(title, parent_widget)
        label.setStyleSheet("font-size: 18px")
        label.mousePressEvent = lambda _: q_input.setFocus()
        return q_input, label
    else:
        return q_input
