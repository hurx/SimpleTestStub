#-*- coding:utf-8 -*-
import urllib2

url = "http://127.0.0.1:8083"

file_object = open(r'request.xml', 'r')

try:
	file_content = file_object.read()
finally:
	file_object.close()

req = urllib2.Request(url=url, headers={'Content-Type': 'text/xml'}, data=file_content)
response = urllib2.urlopen(req)
res = response.read()

print res.decode('utf-8')

