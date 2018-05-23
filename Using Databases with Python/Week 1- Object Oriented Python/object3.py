# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:42:27 2018

@author: Jimit
"""

class PartyAnimal:
    x = 0
    name = ''
    
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')
        
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count:', self.x)
        
s = PartyAnimal('Sally')
s.party()

j = PartyAnimal('Jim')
j.party()
s.party()

PartyAnimal.party(j)    