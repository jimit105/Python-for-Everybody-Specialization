# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 19:50:52 2018

@author: Jimit
"""

# Inheritance

class PartyAnimal:
    x = 0
    name = ''
    
    def __init__(self, z):
        self.name = z
        print(self.name, 'constructed')
        
    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count:', self.x)
      
# FootballFan is a class that extends to PartyAnimal
# It has all capabilities of PartyAnimal and more..
class FootballFan(PartyAnimal):
    points = 0
        
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, 'points', self.points)
        
s = PartyAnimal('Sally')
s.party()

j = FootballFan('Jim')
j.party()
j.touchdown()



"""

OUTPUT

Sally constructed
Sally party count: 1
Jim constructed     # Since there is no constructor of FootballFan, so constructor of PartyAnimal is called
Jim party count: 1
Jim party count: 2
Jim points 7
"""