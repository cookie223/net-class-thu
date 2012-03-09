#!/usr/bin/python
# -*- coding: UTF-8 -*-
from items import *
import sys, os
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
					'type_except':tuple(), }

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
	unread_files = tuple()

	try:
		courses = login(user, password)
	except:
		print u'用户名密码错误或网络连接失败。'
		sys.exit()
	for i in courses:
		print u'正在处理课程 ', i['name'].decode('UTF-8'), ' ...'
		thiscourse = course(i)
		for itemtype in item_name_dict:
			for j in thiscourse.get_item_list(itemtype):
				thisitem = item(j, itemtype)
				thispath = os.path.join(option['path'], i['name'].decode('UTF-8'), item_name_dict[itemtype])
				if not os.path.exists(thispath):
					os.makedirs(thispath)
				if itemtype == 'download' or itemtype == 'homework':
					thisitem.download_data(thispath, size_limit = option['size_limit'], \
							type_only = option['type_only'], type_except = option['type_except'])
				if itemtype == 'homework' or itemtype == 'notice':
					thisitempath = os.path.join(thispath, '_'.join([j['name'].decode('UTF-8'), j['course_id'], j['id']])+'.txt')
					if not os.path.exists(thisitempath):
						unread_files += (thisitempath, )
						fout = open(thisitempath, 'w')
						fout.write(thisitem.get_data())
						fout.close()
	
	os.system('clear')
	if len(unread_files) == 0 :
		sys.exit(1)
	print u'\n\n\n下载完成，有', len(unread_files), u'个新公告/作业，是否阅读？ y/n'
	choice = raw_input()
	if choice.startswith('y') or choice.startswith('Y'):
		for i in unread_files:
			os.system('clear')
			fin = open(i)
			print fin.read()
			fin.close()
			raw_input()
