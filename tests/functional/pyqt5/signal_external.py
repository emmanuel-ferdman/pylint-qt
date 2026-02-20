"""Test that signals accessed externally are recognized."""
# pylint: disable=missing-docstring,too-few-public-methods,unused-argument
from PyQt5.QtCore import QObject, pyqtSignal

class Sender(QObject):
    value_changed = pyqtSignal(int)

def handler(value):
    pass

sender = Sender()
sender.value_changed.connect(handler)
sender.value_changed.emit(42)
