from PIL import Image
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QFileDialog, QPushButton, QGraphicsView, QGraphicsScene, QSizePolicy
from gui import *

class ExampleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.file_dialog = QFileDialog()
        self.ui.file_dialog.setFileMode(QFileDialog.ExistingFiles)
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.encrypt)
        self.ui.pushButton_2.clicked.connect(self.decrypt)
        self.ui.label.setWordWrap(True)

    def encrypt(self):
        img_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", '.', 'Изображение (*.png)')
        try:
            img = Image.open(img_path)
            pixels = img.load()
            width, height = img.size

            r, g, b = pixels[0, 0]

            def split(s):
                return [char for char in s]

            string = self.ui.lineEdit.text()
            t = split(string)

            size = len(t)

            if size < 255:
                pixels[0, 0] = (size, g, b)
            else:
                print("Too big message. Over 255 characters.")

            for y in range(len(t)):
                char = t[y]
                binary = format(ord(char), '08b')
                for x in range(len(binary)):
                    pixel = pixels[x + 1, y]
                    r, g, b = pixel[:3]  # Извлекаем только первые три значения, чтобы избежать ошибки
                    bit = int(binary[x])
                    r = ((r & ~1) | bit)
                    pixels[x + 1, y] = (r, g, b) + pixel[3:]  # Сохраняем остальные значения пикселя
            img.save('encrypted.png', 'PNG')
            pixmap = QPixmap(img_path)
            self.ui.label.setText("Image encrypted and saved as 1.png")

        except Exception as e:
            print(e)

    def decrypt(self):
        try:
            img_path, _ = QFileDialog.getOpenFileName(self, "Выберите файл", '.', 'Изображение (*.png)')
            img = Image.open(img_path)
            pixels = img.load()
            size, g, b = pixels[0, 0]
            binary_string = ""
            for y in range(size):
                char_binary = ""
                for x in range(8):
                    r, _, _ = pixels[x + 1, y]
                    char_binary += str(r & 1)
                binary_string += chr(int(char_binary, 2))

            pixmap = QPixmap(img_path)
            self.ui.label.setText(binary_string)


        except Exception as e:
            print (e)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())
