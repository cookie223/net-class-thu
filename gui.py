#!/usr/bin/python
# -*- coding: UTF-8 -*-
from ui.main_window import *
from PyQt4 import QtGui, QtCore
import sys
from lib.items import *
from ui.view_window import *
from lib.run_thread import mythread

__version__ = '0.2.1'
if hasattr(sys, 'setdefaultencoding'):
	sys.setdefaultencoding('UTF-8')

class read_window(QtGui.QMainWindow, Ui_read_window):
	def __init__(self):
		super(read_window, self).__init__()
		self.setupUi(self)
	def display(self, unread_files):
		self.show()
		self.unread_files = list(unread_files)
		self.next_file()
	def next_file(self):
		if len(self.unread_files) == 0:
			self.close()
			return
		i = self.unread_files[0]
		self.unread_files.remove(i)
		fin = open(i)
		tmp = fin.read()
		if 'gb2312' in tmp:
			tmp = tmp.decode('gb2312')
		else:
			tmp = tmp.decode('UTF-8')
		self.text.setHtml(QtCore.QString(tmp))
		fin.close()

class out_tunnel(QtCore.QObject):
	def __init__(self):
		super(out_tunnel, self).__init__()
		self.connect(self, QtCore.SIGNAL('write(QString)'), main.write)
		self.connect(self, QtCore.SIGNAL('finish(bool)'), main.finish)
	def write(self, msg):
		self.emit(QtCore.SIGNAL('write(QString)'), QtCore.QString(msg))
	def finish(self, statu):
		self.emit(QtCore.SIGNAL('finish(bool)'), statu)

import pickle
class main_window(QtGui.QMainWindow, Ui_main_window):
	def __init__(self):
		super(main_window, self).__init__()
		self.setupUi(self)
		try:
			fin = open('data')
			self.option = pickle.load(fin)
			fin.close()
			self.user_input.setText(QtCore.QString(self.option['user']))
			self.password_input.setText(QtCore.QString(self.option['password']))
			self.size_limit_input.setText(QtCore.QString(self.option['size_limit']))
			self.type_except_input.setText(QtCore.QString(' '.join(self.option['type_except'])))
			self.type_only_input.setText(QtCore.QString(' '.join(self.option['type_only'])))
			self.path.setText(QtCore.QString(self.option['path']))
		except:
			self.option = dict()
		self.show()
		version_news = get_version_news()
		if not version_news == None:
			self.write(version_news['all_msg'])
			if __version__ < version_news['newest']:
				self.write(version_news['newest_msg'])
			else:
				self.write(u'该版本已为最新版本\n\n')
	def finish(self, if_read_files):
		print if_read_files
		self.cancel_button.setEnabled(False)
		self.ok.setEnabled(True)
		if if_read_files:
			read_win.display(self.th.unread_files)
	def cancel_run(self):
		self.th.existing = True
	def submit(self):
		self.ok.setEnabled(False)
		self.cancel_button.setEnabled(True)
		self.option['user'] = str(self.user_input.text().toUtf8()).decode('UTF-8')
		self.option['password'] = str(self.password_input.text().toUtf8()).decode('UTF-8')
		self.option['size_limit'] = str(self.size_limit_input.text().toUtf8()).decode('UTF-8')
		self.option['type_only'] = tuple(str(self.type_only_input.text().toUtf8()).decode('UTF-8').split(' '))
		self.option['type_except'] = tuple(str(self.type_except_input.text().toUtf8()).decode('UTF-8').split(' '))
		self.option['path'] = str(self.path.text().toUtf8()).decode('UTF-8')
		self.option['if_this_only'] = self.checkBox.isChecked()
		if self.option['type_only'] == (u'', ):
			self.option['type_only'] = tuple()
		fout = open('data', 'w')
		pickle.dump(self.option, fout)
		fout.close()
		self.th = mythread(self.option, out_tunnel())
		self.th.start()
	def write(self, msg):
		self.progress.appendPlainText(msg)
	def select_path(self):
		self.path.setText(QtGui.QFileDialog.getExistingDirectory(self))

myapp = QtGui.QApplication(sys.argv)
main = main_window()
read_win = read_window()
sys.exit(myapp.exec_())
