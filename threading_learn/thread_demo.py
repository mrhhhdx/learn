import sys, time, random, threading

from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import QThread, Signal
from ui_mainwindow import Ui_MainWindow


class Runthread(QtCore.QThread):
    _signal = Signal(str)

    def __init__(self):
        super(Runthread, self).__init__()

    def run(self):
        for i in range(100):
            time.sleep(0.05)
            self._signal.emit(str(i))  # 注意这里与_signal = pyqtSignal(str)中的类型相同
        self._signal.emit(str(100))

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Camera Test")

        self.pushButton.clicked.connect(self.set_model_thread())

    def set_model_thread(self):

        self.thread = Runthread()
        # 开始线程
        self.thread._signal.connect(self.set_val)
        self.thread.start()

    def set_val(self, val):
        self.textBrowser.append(val)
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)  # 滑动至底部
        self.pushButton.setEnabled(True)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())