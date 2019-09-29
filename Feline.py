#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:36:18 2019

@author: Ben
Feline implements all the remaining methods that Animal does not.
"""

from Animal import Animal

class Feline(Animal):
    
    def __init__(self, name, eatBehavior):
        super().__init__(name, eatBehavior)
    
    def makeNoise(self):
        print(self.name + " the " + self._type + " let out a big roar!")
     
    def roam(self):
        print(self.name + " the " + self._type + " walked around their territory.")