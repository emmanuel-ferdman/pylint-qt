"""Test that Signal.connect is recognized."""
# pylint: disable=missing-docstring,too-few-public-methods
from PySide2.QtCore import QObject, Signal

class MyWidget(QObject):
    my_signal = Signal()

    def setup(self):
        self.my_signal.connect(self.handler)
        self.my_signal.disconnect()
        self.my_signal.emit()

    def handler(self):
        pass
