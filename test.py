from PyQt4 import QtGui, QtCore
import sys, time, threading

class mythread(QtCore.QThread):
	def __init__(self):
		super(mythread, self).__init__()
		self.existing = False
	def run(self, a):
		while not self.existing:
			print a
			time.sleep(1)

class myline(QtGui.QPlainTextEdit):
	def print_(self, msg):
		self.appendPlainText(QtCore.QString(str(msg)))

myapp = QtGui.QApplication(sys.argv)
main = QtGui.QMainWindow()
output = myline(main)
main.show()
th = mythread()
th.start(3)
myapp.exec_()
th.existing = True
raw_input()
