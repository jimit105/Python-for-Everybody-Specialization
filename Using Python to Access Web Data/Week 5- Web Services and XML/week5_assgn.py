# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 16:09:16 2017

@author: Jimit
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

tree = ET.fromstring(data)

results = tree.findall('.//count')
#print(results)

sum = 0
for item in results:
    sum += int(item.text)

print('Count: ', len(results))
print('Sum: ',sum)