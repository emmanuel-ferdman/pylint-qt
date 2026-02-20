"""Test that inherited signals are recognized."""
# pylint: disable=missing-docstring,too-few-public-methods
from PyQt5.QtCore import QObject, pyqtSignal

class BaseObject(QObject):
    base_signal = pyqtSignal()

class DerivedObject(BaseObject):
    def setup(self):
        self.base_signal.connect(self.handler)
        self.base_signal.emit()

    def handler(self):
        pass
