# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 22:49:37 2017

@author: Jimit
"""

import json
data = '''{
    "name": "Chuck",
    "phone" : {
        "type": "intl",
        "number": "+1 734 303 4456"
        },
    "email" : {
        "hide" : "yes"
        }
    }'''
    
info = json.loads(data)
print(type(info))
print('Name:', info["name"])
print("Hide:", info["email"]["hide"])
