"""Test QApplication signals are recognized."""
# pylint: disable=missing-docstring,unused-argument
from PyQt6.QtWidgets import QApplication

def on_focus_changed(old, new):
    pass

app = QApplication([])
app.focusChanged.connect(on_focus_changed)
app.aboutToQuit.connect(lambda: None)
