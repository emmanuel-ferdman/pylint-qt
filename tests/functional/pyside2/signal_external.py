"""Test that signals accessed externally are recognized."""
# pylint: disable=missing-docstring,too-few-public-methods,unused-argument
from PySide2.QtCore import QObject, Signal

class Sender(QObject):
    value_changed = Signal(int)

def handler(value):
    pass

sender = Sender()
sender.value_changed.connect(handler)
sender.value_changed.emit(42)
