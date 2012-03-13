#!/usr/bin/python
# -*- coding: UTF-8 -*-
from lib.items import *
import sys, os
from lib.run_thread import mythread
try:
	from passwd import user, password
except ImportError:
	f = open('passwd.py', 'w')
	f.write('user = "abc01"\npassword = "YOUR_PASSWORD"\n')
	f.close()
	sys.stderr.write(u'请在passwd.py中填入用户名和密码。')
	sys.exit(-1)
if hasattr(sys, 'setdefaultencoding'):
	sys.setdefaultencoding('UTF-8')

option = {'path':'.', \
					'size_limit':'0', \
					'type_only':tuple(), \
					'type_except':tuple(), 
					'user':user, \
					'password':password }

class console_output:
	def write(self, msg):
		sys.stderr.write(msg)
	def finish(self, statu):
		if not statu:
			sys.exit(statu)

		unread_files = th.unread_files
		os.system('clear')
		if len(unread_files) == 0 :
			sys.exit(0)
		print u'\n\n\n下载完成，有', len(unread_files), u'个新公告/作业，是否阅读？ y/n'
		choice = raw_input()
		if choice.startswith('y') or choice.startswith('Y'):
			for i in unread_files:
				os.system('clear')
				fin = open(i)
				print fin.read()
				fin.close()
				raw_input()

if __name__ == '__main__':
	if '--help' in sys.argv :
		print u'''
清华网络学堂信息获取器

在passwd.py中填入用户名和密码
使用：net_class.py [--path][--size_limit][--type_only][--type_except]

	path:	文件保存路径，默认当前目录。将在此目录下为每个课程新建一个文件夹
				每个课程中新建课程文件，课程公告，课程作业三个文件夹
	size_limit: 限制课程文件的下载大小(bytes)
	type_only:仅下载给定的文件类型
	type_except:不下载给定的文件类型

例：net_class.py --path /tmp --size_limit 10000000 --type_only doc ppt

By BlahGeek@gmail.com '''
		exit()
	for i in sys.argv[1:]:
		if i.startswith('--'):
			thisoption = i[2:]
			continue
		if type(option[thisoption]) == type(tuple()):
			option[thisoption] += (i, )
			continue
		option[thisoption] = i

	option['size_limit'] = int(option['size_limit'])
	option['path'] = os.path.normpath(option['path'].decode('UTF-8'))

	th = mythread(option, console_output(), if_format = True)
	th.start()
