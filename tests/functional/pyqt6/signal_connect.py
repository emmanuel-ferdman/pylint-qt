"""Test that pyqtSignal.connect is recognized."""
# pylint: disable=missing-docstring,too-few-public-methods
from PyQt6.QtCore import QObject, pyqtSignal


class MyWidget(QObject):
    my_signal = pyqtSignal()

    def setup(self):
        self.my_signal.connect(self.handler)
        self.my_signal.disconnect()
        self.my_signal.emit()

    def handler(self):
        pass
