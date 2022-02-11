from PyQt5.Qt import QMainWindow

from ..ui import UIMainWindow


class AppMainWindow(QMainWindow, UIMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setFixedSize(self.width(), self.height())
        self._init()

    def _init(self):
        self._init_button_plus()

    def _init_button_plus(self):
        self.button_plus.clicked.connect(self._event_calculate_result)

    def _event_calculate_result(self):
        a = int(self.text_first.toPlainText())
        b = int(self.text_second.toPlainText())
        self.text_result.setPlainText(str(a + b))