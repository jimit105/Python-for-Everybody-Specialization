# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:34:16 2018

@author: Jimit
"""

class PartyAnimal:
    x = 0
    
    # Constructor
    def __init__(self):
        print('I am constructed')
        
    # Method
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
        
    # Destructor
    def __del__(self):
        print('I am destructed', self.x)
        
an = PartyAnimal()
an.party()
an.party()

an = 42

print('an contains', an)
