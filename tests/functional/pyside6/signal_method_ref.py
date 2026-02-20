"""Test connecting signals to inherited method references."""
# pylint: disable=missing-docstring,too-few-public-methods
from PySide6.QtWidgets import QDialog, QPushButton

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        btn = QPushButton()
        btn.clicked.connect(self.accept)
        btn.clicked.connect(self.reject)
        btn.clicked.connect(self.close)
