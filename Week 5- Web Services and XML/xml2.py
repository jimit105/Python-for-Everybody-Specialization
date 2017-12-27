# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:57:53 2017

@author: Jimit
"""

import xml.etree.ElementTree as ET
input = '''<stuff>
    <users>
        <user x = "2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x = "7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count: ', len(lst))
#print(lst)

for item in lst:
    print('Name: ', item.find('name').text)
    print('ID: ', item.find('id').text)
    print('Attribute: ', item.get("x"))