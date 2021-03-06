import sys
from PySide2 import QtCore, QtWidgets, QtGui
'''
#水平/垂直布局
class LayoutApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        main_widget = QtWidgets.QWidget() # 实例化一个widget控件
        main_layout = QtWidgets.QHBoxLayout() # 实例化一个水平布局层，垂直布局为QVBoxLayout()
        main_widget.setLayout(main_layout) # 设置widget控件布局为水平布局
        # 实例化3个按钮
        button_1 = QtWidgets.QPushButton('按钮一')
        button_2 = QtWidgets.QPushButton('按钮二')
        button_3 = QtWidgets.QPushButton('按钮三')
        # 将按钮添加到水平布局中
        main_layout.addWidget(button_1)
        main_layout.addWidget(button_2)
        main_layout.addWidget(button_3)

        self.setCentralWidget(main_widget) # 设置窗口的中央部件

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = LayoutApp()
    gui.show()
    sys.exit(app.exec_())
'''
'''
#网格布局
#网格布局与水平布局和垂直布局皆不一样，网格布局内部通过一个无形的网格来对其中的控件进行布局。
class LayoutApp2(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        main_widget = QtWidgets.QWidget() # 实例化一个widget控件
        main_layout = QtWidgets.QGridLayout() # 实例化一个垂直布局层
        main_widget.setLayout(main_layout) # 设置widget控件布局为水平布局
        # 实例化3个按钮
        button_1 = QtWidgets.QPushButton('按钮一')
        button_2 = QtWidgets.QPushButton('按钮二')
        button_3 = QtWidgets.QPushButton('按钮三')
        # 将按钮添加到水平布局中
        main_layout.addWidget(button_1,1,1,1,3) # 添加到第1行第1列，占1行占2列
        main_layout.addWidget(button_2,2,1,1,2) # 添加到第2行第1列，占1行占1列
        main_layout.addWidget(button_3,3,1,1,1) # 添加到第3行第2列，占1行占1列

        self.setCentralWidget(main_widget) # 设置窗口的中央部件

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = LayoutApp2()
    gui.show()
    sys.exit(app.exec_())
'''

#表单布局
#带两个参数的addRow()方法，会将第一个参数控件作为表单的标签进行布局，将第一个参数控件作为表单的输入控件进行布局；带一个参数的addRow()方法会将控件直接铺满一行；带一个参数的addWidget()方法则会留空表单标签的位置。
class LayoutApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        #要在主窗口中添加菜单栏，我们只需要实例化一个QMenuBar()类，然后向其中添加具体的菜单项即可
        file_menu = QtWidgets.QMenuBar(self) # 实例化一个菜单栏
        file_menu.setFixedWidth(200) # 设置菜单栏的宽度
        file_menu.addMenu("文件") # 添加一个菜单按钮
        file_menu.addMenu("编辑") # 添加一个菜单按钮
        file_menu.addMenu("关于") # 添加一个菜单按钮

        main_widget = QtWidgets.QWidget() # 实例化一个widget控件
        main_layout = QtWidgets.QFormLayout() # 实例化一个垂直布局层
        main_widget.setLayout(main_layout) # 设置widget控件布局为水平布局
        # 实例化3个按钮
        button_1 = QtWidgets.QLabel('按钮一')
        button_2 = QtWidgets.QPushButton('按钮二')
        button_3 = QtWidgets.QPushButton('按钮三')
        button_4 = QtWidgets.QPushButton('按钮四')
        # 将按钮添加到水平布局中
        main_layout.addRow(button_1,button_2)
        main_layout.addRow(button_3)
        main_layout.addWidget(button_4)
        '''
        Line_Edit_1 = QtWidgets.QLineEdit("设置文字")
        main_layout.addRow(Line_Edit_1)
        button_5 = QtWidgets.QPushButton('提交按钮')
        main_layout.addRow(button_5)
        button_5.clicked.connect(self.clicks)  # 连接点击信号到响应方法
        '''

        Line_Edit_1 = QtWidgets.QLineEdit("设置文字") # 控件创建
        main_layout.addRow(Line_Edit_1)
        Line_Edit_1.setText("设置文字1")  # 设置字符串
        Line_Edit_1.insert('插入的字符串')  # 从光标处插入字符串
        Line_Edit_1.text()  # 获取真是的文本字符
        Line_Edit_1.displayText()  # 获取用户能看到的字符串


        status = self.statusBar()
        status.showMessage("这是一个状态栏消息")

        self.setCentralWidget(main_widget) # 设置窗口的中央部件

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = LayoutApp()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
    