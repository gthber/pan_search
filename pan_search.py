#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import urllib2
import sys
import os
import signal

def signal_handler(sig,frame):
    sys.exit(0)
signal.signal(signal.SIGINT,signal_handler)

reload(sys)
sys.setdefaultencoding('utf-8')
#os.system('CHCP 65001')
#os.system('cls')
pankey = ''


try:
    print "#search#>",
    pankey = sys.stdin.readline()
except KeyboardInterrupt:
    sys.exit(0)



while True:
    if str(pankey) != "":
	try:
	    for num in range(1,2):
		#site = "http://www.panduoduo.net/s/comb/n-"+urllib2.quote(pankey)+"&s-size1&f-f4/"+str(num)
		site = "http://www.panduoduo.net/s/comb/n-"+str(pankey)+"&s-vcnt1&ty-bd/"+str(num)
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		       'Accept-Encoding': 'none',
		       'Accept-Language': 'en-US,en;q=0.8',
		       'Connection': 'keep-alive'}


		req = urllib2.Request(site,headers=hdr)
		bt_page = urllib2.urlopen(req).read()

		i=1
		while True:
		    try:		
			print str(bt_page.split("<div class=\"search-page\">")[1].split("<a target=\"_blank\" title=")[i].split("\"")[1])
			subhref = bt_page.split("<div class=\"search-page\">")[1].split("<a target=\"_blank\" title=")[i].split("href=")[1].split("\"")[1]
			req2 = urllib2.Request("http://www.panduoduo.net"+str(subhref),headers=hdr)
			bt_page2 = urllib2.urlopen(req2).read()
			print str(bt_page2.split("class=\"dbutton2\"")[1].split("href=\"")[1].split("\"")[0])
			print ''
			i += 1

		    except:
			break
		    
	except:
	    print ""
	    print "#search#>",
	    pankey = sys.stdin.readline()
	    continue		    
    try:
	print ""
	print "#search#>",
	pankey = sys.stdin.readline()
	continue
    except KeyboardInterrupt:
	sys.exit(0)	
