#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests
import sys
import os
import signal
import random
import time


def signal_handler(sig,frame):
	sys.exit(0)
signal.signal(signal.SIGINT,signal_handler)

os.system('CHCP 65001')
os.system('cls')
os.system('title 网盘搜索引擎(panda1987cs@gmail.com)')
os.system('color 0f')
pankey = ''

tlist = ['txt','pdf','chm','epub','mobi','mp3','flac','ape','wav','mp4','mkv','rmvb','jpg','png','gif','psd','rar','zip','7z']

def usage():
	global tlist
	print("支持多关键词和文件类型无序搜索")
	print("不输入文件类型，则为全局搜索")
	print("eg.epub mobi 西游记 pdf txt")
	print("eg.mkv 鹿鼎记 rmvb mp4")
	print("支持的格式:",end = '')
	for i in tlist:
		print (i,end = ',')
	print('\n')
	


try:
	usage()
	pankey = input("#search#>")
except KeyboardInterrupt:
	sys.exit(0)



while True:	
	t1 = str(pankey).split(" ")
	t2 = ""
	key = ""
	for j in t1:
		if j not in tlist:
			key +=" "+j
		else:
			t2 +=" "+j
	
			
	site = ""
	if str(pankey) != "":
		try:
			for num in range(1,2):
				#电影、电子书搜索优化
				d = [True for c in t1 if c in tlist]
				if d:					
					site = "http://www.rufengso.net/s/comb/n-"+str(key).strip()+"&f-"+str(t2).strip()+"/"+str(num)					
					#print (site)
									
				#全局搜索
				else:
					site = "http://www.rufengso.net/s/comb/n-"+str(key).strip()+"&nd-d&f-"+str(t2).strip()+"/"+str(num)
					#print (site)
					
					
				hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                       			'Accept-Encoding': 'none',
                       			'Accept-Language': 'en-US,en;q=0.8',
                       			'Connection': 'keep-alive'}


				req = requests.get(site,headers=hdr)
				bt_page = req.text
				print ("\n")
				i=1
				while True:
					try:		
						print (str(bt_page.split("<div class=\"search-page\">")[1].split("<a target=\"_blank\" title=")[i].split("\"")[1]))				
						subhref = str(bt_page.split("<div class=\"search-page\">")[1].split("<a target=\"_blank\" title=")[i].split("href=")[1].split("\"")[1])
						req2 = requests.get("http://www.rufengso.net"+str(subhref),headers=hdr)
						bt_page2 = req2.text
						print (str(bt_page2.split("class=\"dbutton2\"")[1].split("href=\"")[1].split("\"")[0])+"\n")
						i += 1
						
						
					except:
						break

		except:
			usage()
			print ("")
			pankey = input("#search#>")
			continue		    
	try:
		usage()
		print ("")
		pankey = input("#search#>")
		continue
	except KeyboardInterrupt:
		sys.exit(0)	
