# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue May 29 19:38:28 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName(_fromUtf8("main_window"))
        main_window.resize(800, 600)
        self.centralwidget = QtGui.QWidget(main_window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.user_input = QtGui.QLineEdit(self.centralwidget)
        self.user_input.setGeometry(QtCore.QRect(90, 20, 113, 31))
        self.user_input.setObjectName(_fromUtf8("user_input"))
        self.password_input = QtGui.QLineEdit(self.centralwidget)
        self.password_input.setGeometry(QtCore.QRect(90, 60, 113, 31))
        self.password_input.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText)
        self.password_input.setText(_fromUtf8(""))
        self.password_input.setEchoMode(QtGui.QLineEdit.Password)
        self.password_input.setObjectName(_fromUtf8("password_input"))
        self.size_limit_input = QtGui.QLineEdit(self.centralwidget)
        self.size_limit_input.setGeometry(QtCore.QRect(310, 20, 111, 31))
        self.size_limit_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.size_limit_input.setObjectName(_fromUtf8("size_limit_input"))
        self.type_except_input = QtGui.QLineEdit(self.centralwidget)
        self.type_except_input.setGeometry(QtCore.QRect(580, 60, 111, 31))
        self.type_except_input.setText(_fromUtf8(""))
        self.type_except_input.setObjectName(_fromUtf8("type_except_input"))
        self.type_only_input = QtGui.QLineEdit(self.centralwidget)
        self.type_only_input.setGeometry(QtCore.QRect(390, 60, 111, 31))
        self.type_only_input.setObjectName(_fromUtf8("type_only_input"))
        self.ok = QtGui.QPushButton(self.centralwidget)
        self.ok.setEnabled(True)
        self.ok.setGeometry(QtCore.QRect(550, 100, 95, 31))
        self.ok.setDefault(True)
        self.ok.setObjectName(_fromUtf8("ok"))
        self.path = QtGui.QLineEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(90, 100, 381, 31))
        self.path.setReadOnly(True)
        self.path.setObjectName(_fromUtf8("path"))
        self.select_path_button = QtGui.QPushButton(self.centralwidget)
        self.select_path_button.setGeometry(QtCore.QRect(480, 100, 61, 31))
        self.select_path_button.setObjectName(_fromUtf8("select_path_button"))
        self.progress = QtGui.QPlainTextEdit(self.centralwidget)
        self.progress.setGeometry(QtCore.QRect(30, 140, 751, 391))
        self.progress.setObjectName(_fromUtf8("progress"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 51, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 31, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 66, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 30, 81, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 30, 221, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(210, 20, 20, 71))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 70, 161, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(510, 70, 71, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(700, 70, 31, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(560, 540, 221, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.cancel_button = QtGui.QPushButton(self.centralwidget)
        self.cancel_button.setEnabled(False)
        self.cancel_button.setGeometry(QtCore.QRect(704, 100, 71, 31))
        self.cancel_button.setObjectName(_fromUtf8("cancel_button"))
        self.checkBox = QtGui.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(650, 30, 151, 26))
        self.checkBox.setChecked(True)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(main_window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QObject.connect(self.ok, QtCore.SIGNAL(_fromUtf8("clicked()")), main_window.submit)
        QtCore.QObject.connect(self.select_path_button, QtCore.SIGNAL(_fromUtf8("clicked()")), main_window.select_path)
        QtCore.QObject.connect(self.cancel_button, QtCore.SIGNAL(_fromUtf8("clicked()")), main_window.cancel_run)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        main_window.setWindowTitle(QtGui.QApplication.translate("main_window", "清华学堂信息获取器", None, QtGui.QApplication.UnicodeUTF8))
        self.user_input.setText(QtGui.QApplication.translate("main_window", "zyk11", None, QtGui.QApplication.UnicodeUTF8))
        self.size_limit_input.setText(QtGui.QApplication.translate("main_window", "1000000", None, QtGui.QApplication.UnicodeUTF8))
        self.type_only_input.setText(QtGui.QApplication.translate("main_window", "(例:) ppt doc ", None, QtGui.QApplication.UnicodeUTF8))
        self.ok.setText(QtGui.QApplication.translate("main_window", "开始获取", None, QtGui.QApplication.UnicodeUTF8))
        self.path.setText(QtGui.QApplication.translate("main_window", "C:\\", None, QtGui.QApplication.UnicodeUTF8))
        self.select_path_button.setText(QtGui.QApplication.translate("main_window", "浏览", None, QtGui.QApplication.UnicodeUTF8))
        self.progress.setPlainText(QtGui.QApplication.translate("main_window", "v 0.2 new:\n"
"    1.修复了某些情况下保存路径乱码的问题。\n"
"    2.修复了下载时关闭窗口下载无法停止的问题。\n"
"    3.增加了停止下载的按钮。\n"
"    4.增加了新版本检测功能。\n"
"    5.改进了UI。\n"
"    6.应该没了。\n"
"\n"
"对使用者人身经济安全造成的任何后果概不负责\n"
"\n"
"\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("main_window", "用户名", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("main_window", "密码", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("main_window", "保存路径", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("main_window", "不下载大于", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("main_window", "字节的课程文件（0表示不限制）", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("main_window", "下载格式过滤： 仅下载", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("main_window", "或  不下载", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("main_window", "格式", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("main_window", "Written By BlahGeek@Gmail.com", None, QtGui.QApplication.UnicodeUTF8))
        self.cancel_button.setText(QtGui.QApplication.translate("main_window", "停止", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("main_window", "仅处理本学期课程", None, QtGui.QApplication.UnicodeUTF8))

