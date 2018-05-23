# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:23:19 2018

@author: Jimit
"""

class PartyAnimal:
    x = 0
    
    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

an = PartyAnimal()

an.party()  #Equivalent to PartyAnimal.party(an)
an.party()
an.party()
PartyAnimal.party(an)

print('Type:', type(an))
print('Dir:', dir(an))