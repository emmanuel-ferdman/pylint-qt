"""Functional tests for pylint-qt plugin."""

from pathlib import Path

import pytest
from pylint.testutils import FunctionalTestFile, LintModuleTest

HERE = Path(__file__).parent
FUNCTIONAL_DIR = HERE / "functional"
QT_MODULES = {
    "pyqt5": "PyQt5",
    "pyqt6": "PyQt6",
    "pyside2": "PySide2",
    "pyside6": "PySide6",
}


class PylintQtLintModuleTest(LintModuleTest):
    """LintModuleTest with pylint_qt plugin loaded."""

    def __init__(self, test_file, qt_module):
        super().__init__(test_file)
        self._linter.config.extension_pkg_allow_list.append(qt_module)
        self._linter.load_plugin_modules(["pylint_qt"])
        self._linter.load_plugin_configuration()


def get_functional_tests():
    """Collect all functional test files from Qt binding subdirs."""
    suite = []
    for qt_dir in FUNCTIONAL_DIR.iterdir():
        if qt_dir.is_dir() and not qt_dir.name.startswith("_"):
            for path in qt_dir.iterdir():
                if path.suffix == ".py" and not path.name.startswith("_"):
                    suite.append(FunctionalTestFile(str(qt_dir), str(path)))
    return suite


TESTS = get_functional_tests()
TESTS_NAMES = [f"{Path(t.base).parent.name}/{Path(t.base).stem}" for t in TESTS]


@pytest.mark.parametrize("test_file", TESTS, ids=TESTS_NAMES)
def test_functional(test_file):
    """Run functional test."""
    qt_binding = Path(test_file.base).parent.name
    qt_module = QT_MODULES[qt_binding]
    pytest.importorskip(qt_module)
    lint_test = PylintQtLintModuleTest(test_file, qt_module)
    lint_test.setUp()
    lint_test.runTest()
