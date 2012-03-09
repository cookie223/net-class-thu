# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created: Thu Mar  1 20:31:19 2012
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
  _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
  _fromUtf8 = lambda s: s

class Ui_read_window(object):
  def setupUi(self, read_window):
    read_window.setObjectName(_fromUtf8("read_window"))
    read_window.resize(800, 600)
    read_window.setWindowTitle(QtGui.QApplication.translate("read_window", "新作业公告阅读器", None, QtGui.QApplication.UnicodeUTF8))
    self.centralwidget = QtGui.QWidget(read_window)
    self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
    self.next_button = QtGui.QPushButton(self.centralwidget)
    self.next_button.setGeometry(QtCore.QRect(690, 20, 95, 31))
    self.next_button.setText(QtGui.QApplication.translate("read_window", "next", None, QtGui.QApplication.UnicodeUTF8))
    self.next_button.setObjectName(_fromUtf8("next_button"))
    self.text = QtGui.QTextBrowser(self.centralwidget)
    self.text.setGeometry(QtCore.QRect(10, 70, 781, 491))
    self.text.setObjectName(_fromUtf8("text"))
    self.pushButton = QtGui.QPushButton(self.centralwidget)
    self.pushButton.setGeometry(QtCore.QRect(570, 20, 95, 31))
    self.pushButton.setText(QtGui.QApplication.translate("read_window", "close", None, QtGui.QApplication.UnicodeUTF8))
    self.pushButton.setObjectName(_fromUtf8("pushButton"))
    self.label = QtGui.QLabel(self.centralwidget)
    self.label.setGeometry(QtCore.QRect(10, 20, 221, 31))
    font = QtGui.QFont()
    font.setPointSize(21)
    font.setBold(True)
    font.setWeight(75)
    self.label.setFont(font)
    self.label.setText(QtGui.QApplication.translate("read_window", "新课程公告/作业", None, QtGui.QApplication.UnicodeUTF8))
    self.label.setObjectName(_fromUtf8("label"))
    read_window.setCentralWidget(self.centralwidget)
    self.statusbar = QtGui.QStatusBar(read_window)
    self.statusbar.setObjectName(_fromUtf8("statusbar"))
    read_window.setStatusBar(self.statusbar)

    self.retranslateUi(read_window)
    QtCore.QObject.connect(self.next_button, QtCore.SIGNAL(_fromUtf8("clicked()")), read_window.next_file)
    QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), read_window.close)
    QtCore.QMetaObject.connectSlotsByName(read_window)
    read_window.setTabOrder(self.next_button, self.pushButton)
    read_window.setTabOrder(self.pushButton, self.text)

  def retranslateUi(self, read_window):
    pass

