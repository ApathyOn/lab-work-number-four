from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton,
    QVBoxLayout, QWidget, QTextEdit, QInputDialog
)
from string import ascii_lowercase, ascii_uppercase
import sys
import random

# Импорт генераторов
from generators.abs_range import abs_range
from generators.pairwise_products import pairwise_products
from generators.password_generator import password_generator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Generator App")

        # Виджет для вывода результатов
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        # Кнопки для задач
        self.button_task1 = QPushButton("Задание 1: Модули чисел")
        self.button_task1.clicked.connect(self.run_task1)

        self.button_task2 = QPushButton("Задание 2: Пароли")
        self.button_task2.clicked.connect(self.run_task2)

        self.button_task3 = QPushButton("Задание 3: Попарное умножение")
        self.button_task3.clicked.connect(self.run_task3)

        # Разметка
        layout = QVBoxLayout()
        layout.addWidget(self.button_task1)
        layout.addWidget(self.button_task2)
        layout.addWidget(self.button_task3)
        layout.addWidget(self.output_text)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def run_task1(self):
        a, ok1 = QInputDialog.getInt(self, "Задание 1", "Введите a:")
        if not ok1:
            return
        b, ok2 = QInputDialog.getInt(self, "Задание 1", "Введите b (b > a):")
        if not ok2:
            return
        gen = abs_range(a, b)
        values = [str(next(gen)) for _ in range(min(4, abs(b - a) + 1))]
        self.output_text.setPlainText("Результаты задания 1:\n" + ", ".join(values))

    def run_task2(self):
        chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
        gen = password_generator(chars)
        passwords = [next(gen) for _ in range(5)]
        self.output_text.setPlainText("Результаты задания 2:\n" + "\n".join(passwords))

    def run_task3(self):
        list1_str, ok1 = QInputDialog.getText(
            self, "Задание 3", "Введите первый список чисел через пробел:"
        )
        if not ok1:
            return
        list2_str, ok2 = QInputDialog.getText(
            self, "Задание 3", "Введите второй список чисел через пробел:"
        )
        if not ok2:
            return
        try:
            list1 = [int(x) for x in list1_str.split()]
            list2 = [int(x) for x in list2_str.split()]
        except ValueError:
            self.output_text.setPlainText("Ошибка: нужно вводить только числа.")
            return
        gen = pairwise_products(list1, list2)
        values = [str(next(gen)) for _ in range(3)]
        self.output_text.setPlainText("Результаты задания 3:\n" + ", ".join(values))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())