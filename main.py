import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class ImageSizeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aspect Ratio Adjustment Calculator")
        self.setGeometry(100, 100, 400, 200)

        self.label_original = QLabel("Select original image size:")
        self.combo_original = QComboBox()
        self.combo_original.addItems(["512x512", "1024x1024"])

        self.label_width = QLabel("Enter new aspect ratio Width:")
        self.edit_width = QLineEdit()

        self.label_height = QLabel("Enter new aspect ratio Height:")
        self.edit_height = QLineEdit()

        self.btn_calculate = QPushButton("Calculate")
        self.btn_calculate.clicked.connect(self.calculate_new_size)

        self.label_result = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.label_original)
        layout.addWidget(self.combo_original)
        layout.addWidget(self.label_width)
        layout.addWidget(self.edit_width)
        layout.addWidget(self.label_height)
        layout.addWidget(self.edit_height)
        layout.addWidget(self.btn_calculate)
        layout.addWidget(self.label_result)

        self.setLayout(layout)

    def calculate_new_size(self):
        original_size = self.combo_original.currentText()
        width = int(self.edit_width.text())
        height = int(self.edit_height.text())

        if original_size == "512x512":
            total_pixels = 512 * 512
        elif original_size == "1024x1024":
            total_pixels = 1024 * 1024
        else:
            self.label_result.setText("Invalid original image size.")
            return

        new_width = int((total_pixels * width / height) ** 0.5)
        new_height = int(new_width * height / width)

        self.label_result.setText(f"New Size: {new_width}x{new_height} pixels")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = ImageSizeCalculator()
    calculator.show()
    sys.exit(app.exec_())
