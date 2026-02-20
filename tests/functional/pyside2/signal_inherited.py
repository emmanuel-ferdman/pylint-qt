"""Test that inherited signals are recognized."""
# pylint: disable=missing-docstring,too-few-public-methods
from PySide2.QtCore import QObject, Signal

class BaseObject(QObject):
    base_signal = Signal()

class DerivedObject(BaseObject):
    def setup(self):
        self.base_signal.connect(self.handler)
        self.base_signal.emit()

    def handler(self):
        pass
