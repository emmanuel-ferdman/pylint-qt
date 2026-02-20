"""Test that built-in widget signals are recognized."""
# pylint: disable=missing-docstring
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QComboBox, QLineEdit, QPushButton


def test_widget_signals():
    btn = QPushButton()
    btn.clicked.connect(lambda: None)

    edit = QLineEdit()
    edit.textChanged.connect(lambda: None)

    combo = QComboBox()
    combo.currentIndexChanged.connect(lambda: None)

    timer = QTimer()
    timer.timeout.connect(lambda: None)
