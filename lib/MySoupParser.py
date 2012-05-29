#!/usr/bin/env python
# -*- coding=UTF-8 -*-
# Created at May 29 15:48 by BlahGeek@Gmail.com

import sys
if hasattr(sys, 'setdefaultencoding'):
	sys.setdefaultencoding('UTF-8')

import re
from handle_str import *
from BeautifulSoup import BeautifulSoup
class courselist_parser_soup(BeautifulSoup):
	def __init__(self, feed_data):
		BeautifulSoup.__init__(self, feed_data)
		self.courses = tuple()
		_courselist = self.findAll(name="tr", attrs={"class":re.compile("info_tr.*")})
		for i in _courselist:
			tmp = i.find(name='a')
			course_dict = urldecode(tmp.get("href"))
			course_dict['name'] = tmp.text.rpartition('(')[0].rpartition('(')[0]
			course_dict['homework'] = i.find(name="span", attrs={"class":"red_text"}).text
			self.courses += (course_dict, )

class itemlist_parser_soup(BeautifulSoup):
	def __init__(self, feed_data, itemtype):
		BeautifulSoup.__init__(self, feed_data)
		_itemlist = self.findAll(name="tr", attrs={"class":re.compile("tr[12]")})
		self.items = tuple()
		for i in _itemlist:
			tmp = i.find("a")
			item_dict = urldecode(tmp.get("href"))
			item_dict['name'] = tmp.text
			if itemtype == 'homework':
				if i.findAll(name="td")[3].text==u'已经提交':
					item_dict['is_submit'] = '1'
				else:
					item_dict['is_submit'] = '0'
				item_dict['time'] = i.findAll(name="td")[2].text
			self.items += (item_dict, )
