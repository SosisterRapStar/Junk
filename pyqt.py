from PyQt5.QtWidgets import QApplication, QWidget
import sys  # для доступа к аргументам  командной строки

# Приложению нужен один (и только один) экземпляр QApplication.
app = QApplication(sys.argv)
print(QApplication.__dict__)
# Создаём виджет Qt — окно.
window = QWidget()
# он создает сначала скрытое окно, чтобы вывести окно необходим show
window.show()
# Запуск цикла и программы
app.exec()
