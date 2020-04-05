import sys, time, random, threading, requests

from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtCore import QThread, Signal
from ui_mainwindow import Ui_MainWindow

test_dict = {
    'ISO_AUTO': 'http://www.baidu.com',
    'ISO_100': 'http://www.dji.com'
}

test_dict2 = {
    'SHUTTER_AUTO': 'http://www.csdn.net',
    'SHUTTER_1/5000': 'http://www.youku.com'
}

test_dict3 = {
    'Logo_On': 'http://www.bilibili.com',
    'Logo_Off': 'http://www.weibo.com'
}

set_dict = {}

class Runthread(QtCore.QThread):
    #  通过类成员对象定义信号对象
    _signal = Signal(str, str)

    def __init__(self):
        super(Runthread, self).__init__()

    def run(self):
        for i in range(10):
            dict_key = random.sample(set_dict.keys(), 1)
            model = dict_key[0]
            url = set_dict[model]

            response = requests.get(url)
            time.sleep(1)
            self._signal.emit(model, str(response))
        self._signal.emit(self, "done")
        '''for i in range(100):
            time.sleep(0.05)
            self._signal.emit(str(i))  # 注意这里与_signal = pyqtSignal(str)中的类型相同
        self._signal.emit(str(100))'''

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Camera Test")

        self.pushButton.clicked.connect(self.set_model)

    def set_model(self):
        if self.checkBox_2.isChecked() and self.checkBox_6.isChecked():
            self.textBrowser.append('开始了')
            self.pushButton.setEnabled(False)  # 开始按钮置灰
            set_dict.update(test_dict)
            set_dict.update(test_dict2)
            self.set_model_thread()
        elif self.checkBox_2.isChecked():
            self.textBrowser.append('开始了')
            self.pushButton.setEnabled(False) # 开始按钮置灰
            set_dict.update(test_dict)
            self.set_model_thread()

    def set_model_thread(self):

        self.thread = Runthread()
        # 开始线程
        self.thread._signal.connect(self.set_val)
        self.thread.start()

    def set_val(self, val, val2):
        self.textBrowser.append(val + val2)
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)  # 滑动至底部



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())