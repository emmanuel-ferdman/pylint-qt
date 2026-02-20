"""Test signals with aliased imports."""
# pylint: disable=missing-docstring
from PySide6.QtCore import QTimer as Timer
from PySide6.QtWidgets import QLineEdit as Edit
from PySide6.QtWidgets import QPushButton as Btn

def test_aliased_imports():
    btn = Btn()
    btn.clicked.connect(lambda: None)

    edit = Edit()
    edit.textChanged.connect(lambda: None)

    timer = Timer()
    timer.timeout.connect(lambda: None)
