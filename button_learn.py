from PySide2 import QtWidgets, QtGui
import sys
import requests

class ButtonApp(QtWidgets.QMainWindow):
    text = 'str'
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt For Python按钮控件")
        self.setFixedSize(500, 200)  # 设置窗口固定大小
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.btn_1 = QtWidgets.QPushButton("按钮一")
        self.btn_1.setEnabled(False)

        self.btn_2 = QtWidgets.QPushButton()
        self.btn_2.setText("按钮二")

        self.btn_3 = QtWidgets.QPushButton("按钮三") # 创建按钮3
        icon_img = QtGui.QIcon("./icon.png") # 实例化一个QIcon对象
        self.btn_3.setIcon(icon_img) # 设置按钮的图标

        self.btn_4 = QtWidgets.QPushButton("切换至普通拍照")
        self.btn_4.setFixedSize(80,80) # 设置按钮的固定大小
        self.btn_4.clicked.connect(self.clicks) # 连接点击信号到响应方法

        #self.go_button = QtWidgets.QPushButton("Go", ButtonApp)
        self.go_button = QtWidgets.QPushButton('&Go') #如果我们想为按钮设置一个键盘快捷键，如Alt-G，我们可以在‘Go’前添加一个‘&G’：
        self.go_button.setDefault(True) #设置为默认按钮
        self.go_button.clicked.connect(self.clicks) # 连接点击信号到响应方法

        self.textEdit = QtWidgets.QTextEdit()
        #self.document = QtGui.QTextDocument()
        #self.textEdit.setDocument(self.document)
        self.textEdit.setText(self.text)  # 普通文本设定
        # QTextEdit.toPlainText()


        self.main_layout.addWidget(self.btn_1)
        self.main_layout.addWidget(self.btn_2)
        self.main_layout.addWidget(self.btn_3)
        self.main_layout.addWidget(self.btn_4)
        self.main_layout.addWidget(self.go_button)
        self.main_layout.addWidget(self.textEdit)

        self.setCentralWidget(self.main_widget)

    # 点击响应方法
    def clicks(self):
        self.text = '点击成功'
        print('点击成功')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = ButtonApp()
    gui.show()
    sys.exit(app.exec_())