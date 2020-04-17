#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import requests
import sys
import os
import signal


def signal_handler(sig,frame):
	sys.exit(0)
signal.signal(signal.SIGINT,signal_handler)

os.system('CHCP 65001')
os.system('cls')
os.system('title 网盘搜索引擎(panda1987cs@gmail.com)')
os.system('color 0f')
pankey = ''

tlist = ['txt','pdf','chm','epub','mobi','mp3','flac','ape','wav','mp4','mkv','rmvb','jpg','png','gif','psd','rar','zip','7z']
tbook = ['txt','pdf','chm','epub','mobi']
tvideo = ['mp3','flac','ape','wav','mp4','mkv','rmvb','rar','zip','7z']

def usage():
	global tlist
	print("\n程序使用说明:输入关键词+文件类型，多个文件类型之间用空格隔开")
	print("支持多关键词查找,关键词写前面，文件类型写后面")
	print("例如:西游记 pdf epub txt")
	print("例如:linux shell pdf epub mobi txt")
	print("不输入文件类型，则为全局搜索")
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
	i = 0
	for j in t1:
		if j not in tlist:
			i += 1
			
	try:
		key = "%20".join(t1[0:i])		
	except(EOFError):
		key = str(pankey)
	try:
		t2 = "%20".join(t1[i:])
	except(EOFError):
		t2 = ""
		pass
	site = ""
	if str(pankey) != "":
		try:
			for num in range(1,2):
				#电子书搜索优化
				d = [True for c in (t1[i:]) if c in tbook]
				e = [True for c in (t1[i:]) if c in tvideo]
				if d:					
					site = "http://www.rufengso.net/s/comb/n-"+str(key).rstrip("%20")+"&f-"+str(t2)+"/"+str(num)
					#print (site)
									
				#影视资源搜索优化					
				elif e:
					site = "http://www.rufengso.net/s/comb/n-"+str(key).rstrip("%20")+"&f-"+str(t2)+"/"+str(num)
					#print (site)
				#全局搜索
				else:
					site = "http://www.rufengso.net/s/comb/n-"+str(key).rstrip("%20")+"&nd-d&f-"+str(t2)+"/"+str(num)
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
						subhref = bt_page.split("<div class=\"search-page\">")[1].split("<a target=\"_blank\" title=")[i].split("href=")[1].split("\"")[1]
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
