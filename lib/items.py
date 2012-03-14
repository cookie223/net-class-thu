#!/usr/bin/python
# -*- coding=UTF-8 -*-

baseurl = 'http://learn.tsinghua.edu.cn/MultiLanguage'
loginurl = baseurl + '/lesson/teacher/loginteacher.jsp'
courselist_url = baseurl + '/lesson/student/MyCourse.jsp?language=cn'
noticelist_url = baseurl + '/public/bbs/getnoteid_student.jsp'
downloadlist_url = baseurl + '/lesson/student/download.jsp'
homeworklist_url = baseurl + '/lesson/student/hom_wk_brw.jsp'
homework_url = baseurl + '/lesson/student/hom_wk_detail.jsp'
notice_url = baseurl + '/public/bbs/note_reply.jsp'
download_url = 'http://learn.tsinghua.edu.cn/uploadFile/downloadFile_student.jsp'
url_dict = locals()
version_news_url = 'http://learn.tsinghua.edu.cn:8080/2011011262/version_news'

item_name_dict = {'download':u'课程文件', 
									'homework':u'课程作业', 
									'notice':u'课程公告'}

import urllib
import cookielib
import urllib2
from MyParser import *

def login(user, password):
	try:
		opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
		urllib2.install_opener(opener)
		para = urllib.urlencode({'userid':user, 'userpass':password})
		urllib2.urlopen(loginurl, para)
		return courselist_parser(urllib2.urlopen(courselist_url).read()).courses
	except urllib2.HTTPError:
		raise RuntimeError(u'用户名密码错误\n')

class course:
	def __init__(self, course_dict):
		self.course_dict = course_dict
	def get_item_list(self, itemtype):
		url = url_dict[itemtype+'list_url'] + '?' + urllib.urlencode(self.course_dict)
		f = urllib2.urlopen(url).read()
		f = f.replace(r'&nbsp;', ' ')
		return itemlist_parser(f, itemtype).items

import subprocess
import os, sys, tempfile
html_dumper = ['w3m', '-T', 'text/html', '-dump']
class item:
	def __init__(self, item_dict, itemtype):
		self.item_dict = item_dict
		self.itemtype = itemtype
	def get_data(self, if_format = True, out = sys.stdout):
		url = url_dict[self.itemtype + '_url'] + '?' + urllib.urlencode(self.item_dict)
		out.write(u'\t正在获取  '+item_name_dict[self.itemtype]+'   '+self.item_dict['name'].decode('UTF-8')+'...\n')
		data = urllib2.urlopen(url).read()
		if(if_format and (self.itemtype == 'notice' or self.itemtype == 'homework')):
			fout = tempfile.TemporaryFile()
			fout.write(data)
			fout.seek(0)
			try:
				data = subprocess.check_output(html_dumper, stdin=fout)
			except OSError:
				raise RuntimeError(u'依赖w3m程序，请安装\n')
		out.write(u'\t\t成功\n\n')
		return data
	def download_data(self, filepath, size_limit=0, type_except=tuple(), type_only=tuple(), out = sys.stdout):
		if self.itemtype == 'homework':
			return self.download_attachment(filepath, out = out)
		url = url_dict[self.itemtype + '_url'] + '?' + urllib.urlencode(self.item_dict)
		obj = urllib2.urlopen(url)
		filename = os.path.join(filepath, obj.info().get('Content-Disposition').partition('filename="')[2][:-1].decode('gb2312'))
		obj_type = filename.rpartition('.')[2]
		out.write(u'\t正在处理  ' + item_name_dict[self.itemtype] +'   '+ self.item_dict['name'].decode('UTF-8') + '...\n' )
		if os.path.exists(filename) and int(os.path.getsize(filename)) == int(obj.info().get('Content-Length')):
			out.write(u'\t\t文件已存在，忽略 \n\n')
			return 
		if size_limit != 0  and int(obj.info().get('Content-Length')) > size_limit:
			out.write(u'\t\t文件太大，忽略\n\n')
			return 
		if (len(type_only) !=0 and obj_type not in type_only) or obj_type in type_except:
			out.write(u'\t\t文件类型不匹配，忽略 \n\n')
			return 
		fout = open(filename, 'wb')
		fout.write(obj.read())
		fout.close()
		out.write(u'\t\t下载成功。\n\n')
	def download_attachment(self, filepath, out = sys.stdout):
		attach_url = urllib2.urlopen(url_dict[self.itemtype+'_url']+'?'+urllib.urlencode(self.item_dict)).read().partition('<a target="_top" href="')[2].partition('">')[0]
		if attach_url == '':
			out.write(u'\t正在处理  ' + item_name_dict[self.itemtype] +'   '+ self.item_dict['name'].decode('UTF-8') + '...\n')
			out.write(u'\t\t无附件\n\n')
			return
		attach_dict = urldecode(attach_url)
		attach_dict['name'] = self.item_dict['name']
		return item(attach_dict, 'download').download_data(filepath, out = out)

import pickle
def get_version_news():
	try:
		data = urllib2.urlopen(version_news_url, timeout = 3)
		return pickle.load(data)
	except:
		return None
