"""Test that subscripted signals are recognized."""
# pylint: disable=missing-docstring
from PyQt5.QtWidgets import QComboBox, QSpinBox

def test_subscripted_signals():
    spin = QSpinBox()
    spin.valueChanged[int].connect(lambda x: None)

    combo = QComboBox()
    combo.currentIndexChanged[int].connect(lambda x: None)
    combo.activated[str].connect(lambda x: None)
