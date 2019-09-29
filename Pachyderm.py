#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:31:52 2019

@author: Ben
"""

from Animal import Animal
from EatBehavior import EatsVeggies

class Pachyderm(Animal):
    
    def __init__(self, name):
        #All pachyderms have the same eatBehavior so it is set here as EatsVeggies
        eatBehavior = EatsVeggies()
        super().__init__(name, eatBehavior)
    
    #Pachyderm implements roam for its subclasses
    def roam(self):
        print(self.name + " the " + self._type + " walked around their enclosure.")